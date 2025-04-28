#!/usr/bin/env python
"""
Quick security check script to detect potential API keys and sensitive information.
This is a faster version that only checks key project files.

Usage:
    python scripts/quick_security_check.py
"""

import os
import re
import sys

# Patterns that could indicate sensitive information
PATTERNS = {
    "OpenAI API Key": r"sk-[a-zA-Z0-9]{48}",
    "Webhook URL": r"https://hooks\.zapier\.com/hooks/catch/[a-zA-Z0-9/]+",
    "Notion API Key": r"secret_[a-zA-Z0-9]{43}",
}

# Files to check (only the most important ones)
FILES_TO_CHECK = [
    "README.md",
    "requirements.txt",
    "LICENSE",
    ".gitignore",
    ".env.example",
    "docs/installation.md",
    "docs/security.md",
    "docs/workflow-diagram.md",
    "docs/linkedin-post.md",
    "scripts/setup_git_hooks.py",
    "scripts/security_check.py",
    "workflow_output/.gitkeep"
]

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
        
    except Exception as e:
        print(f"Error scanning {file_path}: {str(e)}")
        return False

def main():
    """Main function to scan files."""
    issues_found = 0
    files_checked = 0
    
    for file_path in FILES_TO_CHECK:
        if not os.path.exists(file_path):
            print(f"Skipping non-existent file: {file_path}")
            continue
            
        print(f"Checking {file_path}...")
        files_checked += 1
        if scan_file(file_path):
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