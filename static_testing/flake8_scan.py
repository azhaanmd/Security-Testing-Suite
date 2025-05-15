import subprocess

TARGET = "."  # Target folder to scan
OUTPUT_FILE = "static_testing/flake8_report.txt"
EXCLUDED_DIRS = "secenv,__pycache__,.pytest_cache"

def run_flake8():
    print(f"Running Flake8 scan on {TARGET} ...")
    command = f"flake8 {TARGET} --exclude={EXCLUDED_DIRS} --output-file={OUTPUT_FILE}"
    subprocess.run(command, shell=True)
    print(f"Flake8 report saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    run_flake8()
