#!/usr/bin/env python
"""
Security check script to detect potential API keys and sensitive information
before committing to GitHub.

Usage:
    python scripts/security_check.py [files_to_check]
"""

import os
import re
import sys
import glob
from pathlib import Path

# Patterns that could indicate sensitive information
PATTERNS = {
    "OpenAI API Key": r"sk-[a-zA-Z0-9]{48}",
    "Generic API Key": r"[a-zA-Z0-9_\-]{20,40}",
    "Webhook URL": r"https://hooks\.zapier\.com/hooks/catch/[a-zA-Z0-9/]+",
    "Basic Auth": r"Authorization: Basic [a-zA-Z0-9+/=]+",
    "Bearer Token": r"Bearer [a-zA-Z0-9\-._~+/]+=*",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Private Key": r"-----BEGIN [A-Z ]+ PRIVATE KEY-----",
    "Notion API Key": r"secret_[a-zA-Z0-9]{43}",
    "Environment Variable Setting": r"^[A-Z_]+=.+",
}

# Files and directories to exclude
EXCLUDED_PATHS = [
    ".git",
    "venv",
    ".env.example",
    "requirements.txt",
    "LICENSE",
    "README.md",
    "__pycache__",
    "*.pyc",
    ".gitignore",
    "scripts/security_check.py",  # Don't check this file itself
]

# Files to explicitly ignore from checking
SAFE_FILES = [
    ".env.example",
    "security_check.py",
    ".gitignore",
]

def is_excluded(path):
    """Check if a path should be excluded from scanning."""
    path_str = str(path)
    
    # Check each exclusion pattern
    for exclude in EXCLUDED_PATHS:
        if "*" in exclude:
            # Handle glob patterns
            if glob.fnmatch.fnmatch(path_str, exclude):
                return True
        elif exclude in path_str:
            return True
            
    # Check if it's a safe file
    for safe in SAFE_FILES:
        if path_str.endswith(safe):
            return True
            
    return False

def scan_file(file_path):
    """Scan a file for potential sensitive information."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        issue_found = False
        
        # Check for each pattern
        for name, pattern in PATTERNS.items():
            matches = re.finditer(pattern, content, re.MULTILINE)
            for match in matches:
                line_no = content[:match.start()].count('\n') + 1
                line_content = content.split('\n')[line_no - 1]
                
                # Skip if in a comment or if it's obviously a placeholder
                if "your_" in line_content.lower() or "placeholder" in line_content.lower():
                    continue
                if "example" in line_content.lower():
                    continue
                    
                print(f"⚠️  Potential {name} found in {file_path}:{line_no}")
                print(f"   {line_content.strip()}")
                print()
                issue_found = True
                
        return issue_found
        
    except UnicodeDecodeError:
        # Skip binary files
        return False
    except Exception as e:
        print(f"Error scanning {file_path}: {str(e)}")
        return False

def main():
    """Main function to scan files."""
    # Files provided as arguments
    files_to_check = sys.argv[1:] if len(sys.argv) > 1 else None
    
    if files_to_check:
        # Check specific files
        files = [Path(file) for file in files_to_check]
    else:
        # Check all files in current directory and subdirectories
        files = []
        for path in Path('.').rglob('*'):
            if path.is_file() and not is_excluded(path):
                files.append(path)
    
    issues_found = 0
    files_checked = 0
    
    for file in files:
        if is_excluded(file):
            continue
            
        files_checked += 1
        if scan_file(file):
            issues_found += 1
    
    print(f"\nSecurity check complete. Checked {files_checked} files.")
    
    if issues_found:
        print(f"⚠️  Found potential sensitive information in {issues_found} files.")
        print("Please review and fix these issues before committing.")
        sys.exit(1)
    else:
        print("✅ No sensitive information detected.")
        sys.exit(0)

if __name__ == "__main__":
    main() 