import subprocess
import os

def push_to_github():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN not found in environment.")
        return

    repo_url = f"https://{token}@github.com/replit-user/2captcha-multi-checker.git"
    
    commands = [
        ["git", "init"],
        ["git", "config", "--global", "user.email", "replit@example.com"],
        ["git", "config", "--global", "user.name", "Replit Agent"],
        ["git", "add", "."],
        ["git", "commit", "-m", "Initial commit for Render deployment"],
        ["git", "branch", "-M", "main"],
        ["git", "remote", "add", "origin", repo_url],
        ["git", "push", "-u", "origin", "main", "-f"]
    ]

    for cmd in commands:
        try:
            print(f"Executing: {' '.join(cmd[:2])}...") # Masking full command for safety
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Error executing command: {result.stderr}")
        except Exception as e:
            print(f"Exception occurred: {e}")

if __name__ == "__main__":
    push_to_github()
