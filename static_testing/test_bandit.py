import os
import subprocess

# ✅ Target directory (parent folder of this script)
TARGET = "."

# ✅ Output report location
OUTPUT_FILE = "static_testing/bandit_report.txt"

# ✅ Folders to exclude (use forward slashes!)
EXCLUDED_DIRS = "../secenv,../.pytest_cache"

def run_bandit():
    print(f"Scanning {TARGET} for security issues...")

    # ✅ Bandit command with POSIX-compatible paths
    command = f"bandit -r {TARGET} --exclude {EXCLUDED_DIRS} -o {OUTPUT_FILE} -f txt"
    print(f"Running command: {command}")

    subprocess.run(command, shell=True)
    print(f"Report saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    run_bandit()