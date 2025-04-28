#!/usr/bin/env python
"""
Set up Git hooks for the project.
This script installs a pre-commit hook to check for sensitive information.

Usage:
    python scripts/setup_git_hooks.py
"""

import os
import stat
from pathlib import Path

PRE_COMMIT_HOOK = """#!/bin/sh
# Pre-commit hook to check for sensitive information

echo "🔒 Running security checks..."
python scripts/security_check.py

# Exit with the status from the security check
exit $?
"""

def main():
    """Set up Git hooks for the project."""
    # Find the .git directory
    git_dir = Path('.git')
    
    if not git_dir.exists():
        print("❌ This does not appear to be a Git repository (.git directory not found).")
        return False
        
    # Create hooks directory if it doesn't exist
    hooks_dir = git_dir / 'hooks'
    hooks_dir.mkdir(exist_ok=True)
    
    # Create pre-commit hook
    pre_commit_path = hooks_dir / 'pre-commit'
    
    try:
        with open(pre_commit_path, 'w') as f:
            f.write(PRE_COMMIT_HOOK)
            
        # Make the hook executable
        os.chmod(pre_commit_path, 
                 os.stat(pre_commit_path).st_mode | 
                 stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
                 
        print(f"✅ Pre-commit hook installed at {pre_commit_path}")
        print("The hook will run security checks before each commit.")
        return True
    except Exception as e:
        print(f"❌ Failed to install pre-commit hook: {str(e)}")
        return False
        
if __name__ == "__main__":
    main() 