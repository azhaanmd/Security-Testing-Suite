import subprocess

# ✅ Path to requirements file
REQUIREMENTS_FILE = "requirements.txt"

# ✅ Output report location
OUTPUT_FILE = "static_testing/safety_report.txt"

def run_safety_check():
    print("Scanning dependencies with Safety...")

    # 🔍 Safety command with JSON output (can use --full-report if needed)
    command = f"safety check --file={REQUIREMENTS_FILE} --output=text --save-json={OUTPUT_FILE}"
    subprocess.run(command, shell=True)

    print(f"Safety scan report saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    run_safety_check()