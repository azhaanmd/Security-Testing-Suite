import subprocess

TARGET = "."
OUTPUT_FILE = "static_testing/pylint_report.txt"
EXCLUDED_DIRS = ["secenv", "__pycache__", ".pytest_cache"]

def run_pylint():
    print(f"Running Pylint scan on {TARGET} ...")

    # Pylint doesn't have --exclude like flake8, so we build the command differently.
    # We'll use find to exclude folders (works in Unix-like OS).
    # For Windows, we can just scan but exclude via .pylintrc or ignore files.

    command = f"pylint {TARGET} --output-format=text > {OUTPUT_FILE}"
    subprocess.run(command, shell=True)
    print(f"Pylint report saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    run_pylint()
