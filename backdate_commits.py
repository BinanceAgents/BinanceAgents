#!/usr/bin/env python3
"""
Script to backdate commits for all files in a repository
Distributes commits randomly across the last 3 months
"""

import os
import subprocess
import random
from datetime import datetime, timedelta
from pathlib import Path

def get_all_files(repo_path):
    """Get all files in the repository, excluding .git directory"""
    files = []
    for root, dirs, filenames in os.walk(repo_path):
        # Skip .git directory
        if '.git' in dirs:
            dirs.remove('.git')
        
        for filename in filenames:
            file_path = os.path.join(root, filename)
            files.append(file_path)
    
    return files

def generate_random_dates(count, days_back=90):
    """Generate random dates within the last specified days"""
    now = datetime.now()
    dates = []
    
    for _ in range(count):
        random_days = random.randint(0, days_back)
        random_hours = random.randint(0, 23)
        random_minutes = random.randint(0, 59)
        
        random_date = now - timedelta(
            days=random_days,
            hours=random_hours,
            minutes=random_minutes
        )
        dates.append(random_date)
    
    # Sort dates chronologically (oldest first)
    dates.sort()
    return dates

def make_small_change(file_path):
    """Make a small change to a file (add a comment or whitespace)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add a comment at the end based on file type
        ext = os.path.splitext(file_path)[1]
        
        if ext in ['.py']:
            content += f'\n# Updated: {datetime.now().isoformat()}\n'
        elif ext in ['.js', '.ts', '.jsx', '.tsx', '.java', '.c', '.cpp']:
            content += f'\n// Updated: {datetime.now().isoformat()}\n'
        elif ext in ['.html', '.xml']:
            content += f'\n<!-- Updated: {datetime.now().isoformat()} -->\n'
        elif ext in ['.css', '.scss']:
            content += f'\n/* Updated: {datetime.now().isoformat()} */\n'
        else:
            # For other files, just add a newline
            content += '\n'
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error modifying {file_path}: {e}")
        return False

def create_backdated_commit(file_path, commit_date, repo_path):
    """Create a backdated commit for a specific file"""
    try:
        # Format date for git
        date_str = commit_date.strftime('%Y-%m-%d %H:%M:%S')
        
        # Get relative file path for commit message
        rel_path = os.path.relpath(file_path, repo_path)
        
        # Git commands
        subprocess.run(['git', 'add', file_path], cwd=repo_path, check=True)
        
        # Set both author and committer dates
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = date_str
        env['GIT_COMMITTER_DATE'] = date_str
        
        commit_message = f'Update {rel_path}'
        
        subprocess.run(
            ['git', 'commit', '-m', commit_message],
            cwd=repo_path,
            env=env,
            check=True
        )
        
        print(f"✓ Committed {rel_path} with date {date_str}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"✗ Error committing {file_path}: {e}")
        return False

def main():
    # Configuration
    repo_path = input("Enter the path to your local repository: ").strip()
    
    if not os.path.exists(repo_path):
        print(f"Error: Repository path '{repo_path}' does not exist!")
        return
    
    if not os.path.exists(os.path.join(repo_path, '.git')):
        print(f"Error: '{repo_path}' is not a git repository!")
        return
    
    print(f"\nScanning repository: {repo_path}")
    
    # Get all files
    files = get_all_files(repo_path)
    print(f"Found {len(files)} files")
    
    if not files:
        print("No files found to commit!")
        return
    
    # Generate random dates
    dates = generate_random_dates(len(files), days_back=90)
    
    # Shuffle files for random order
    random.shuffle(files)
    
    print(f"\nThis will create {len(files)} commits spread across the last 3 months.")
    confirm = input("Do you want to proceed? (yes/no): ").strip().lower()
    
    if confirm != 'yes':
        print("Aborted.")
        return
    
    print("\nCreating backdated commits...\n")
    
    successful = 0
    failed = 0
    
    for file_path, commit_date in zip(files, dates):
        # Make a small change to the file
        if make_small_change(file_path):
            # Create backdated commit
            if create_backdated_commit(file_path, commit_date, repo_path):
                successful += 1
            else:
                failed += 1
        else:
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"Summary:")
    print(f"  Successful commits: {successful}")
    print(f"  Failed commits: {failed}")
    print(f"{'='*50}")
    
    if successful > 0:
        print("\n⚠️  Important: To push these backdated commits to GitHub, use:")
        print(f"    cd {repo_path}")
        print("    git push --force origin main")
        print("\n⚠️  Warning: This will rewrite the repository history!")
        print("    Make sure you have a backup before force pushing.")

if __name__ == "__main__":
    main()

# Updated: 2025-10-08T19:59:22.047036
