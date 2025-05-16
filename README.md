# 🔐 Security Testing Suite

Welcome to the **Security Testing Suite** — a powerful, automated security testing project built for modern QA and SDET workflows.

This suite is designed to demonstrate hands-on expertise in **security testing, CI/CD integration, static code analysis, and OWASP ZAP scans** — all configured to run in the cloud via GitHub Actions.


---

## 🚀 Key Features

- ✅ **OWASP ZAP baseline scan** with HTML, JSON, and Markdown reports
- ✅ **Fully automated GitHub Actions CI pipeline**
- ✅ **Static code analysis** using industry-standard tools (Bandit, Safety, Flake8, PyLint)
- ✅ **Dynamic testing** using OWASP ZAP against a live test site
- ✅ **Scans run in Docker containers — no local installation required**
- ✅ **Reports automatically committed back to the repo**
- ✅ Organized folder structure and beginner-friendly Python security tests

---

## 🧰 Tools & Technologies Used

| Tool            | Purpose                                        |
|-----------------|------------------------------------------------|
| 🕷️ OWASP ZAP     | Dynamic security scanning (baseline scan)      |
| 🐳 Docker         | Run scans in a containerized environment       |
| 🚦 GitHub Actions | CI/CD to automate ZAP scans & commits         |
| 🛡️ Bandit         | Static analysis for Python security issues     |
| 🧪 Safety         | Checks dependencies for known vulnerabilities |
| 🧹 Flake8         | Linting and code quality                      |
| 🧐 PyLint         | Static code analysis for code quality         |
| 📊 Markdown, HTML, JSON | ZAP Reports in multiple formats           |

---

## 📁 Folder Structure

```text
Security-Testing-Suite/
├── .github/
│   └── workflows/
│       └── zap_scan.yml          # CI workflow for OWASP ZAP scan
├── static_analysis/
│   ├── bandit_report.txt        # Bandit output
│   ├── safety_report.txt        # Safety output
│   ├── flake8_report.txt        # Flake8 output
│   └── pylint_report.txt        # PyLint output
├── zap_reports/
│   ├── zap_report_<run_id>.html # OWASP ZAP HTML report
│   ├── zap_report_<run_id>.md   # Markdown report
│   └── zap_report_<run_id>.json # JSON report
├── security_tests/
│   ├── test_headers.py          # Security header tests
│   ├── test_cookies.py          # Cookie security tests
│   ├── test_xss.py              # XSS vulnerability checks
│   └── test_injections.py       # SQL injection & blind SQLi
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── .gitignore

🔄 **CI/CD Workflow Summary**
The entire OWASP ZAP scan process is automated using GitHub Actions:

✅ Triggered manually via workflow_dispatch

🛠️ Sets up Git, Docker, and a reports folder

🕷️ Runs zap-baseline.py against the target site (e.g., http://testphp.vulnweb.com)

🗂️ Generates reports in HTML, JSON, and Markdown

📬 Commits the reports back to zap_reports/ directory in the repo

➕ **Want to view a report?**
Go to the zap_reports/ folder and open any .html file directly in your browser for a full interactive scan report.

**🧪 Security Tests Included**
- The security_tests/ folder includes lightweight, security-focused Python tests that simulate how a QA might manually or programmatically validate app security:

- Headers Testing: Checks for secure headers like Content-Security-Policy, Strict-Transport-Security, etc.

- Cookies Testing: Ensures HttpOnly, Secure, and SameSite attributes are set.

- XSS Testing: Tries to inject <script> and verifies output reflection.

- SQL Injection: Attempts vulnerable payloads and checks response behavior.

- Blind SQLi: Uses time-based queries to infer vulnerabilities without visible error messages.

⚔️ **Dynamic Security Testing with OWASP ZAP**
This project performs dynamic analysis using OWASP ZAP's zap-baseline.py script in a Docker container.
This means the scan behaves like a real attacker accessing a live site, uncovering runtime vulnerabilities such as:

- Missing security headers
- Outdated components
- XSS risks
- Cookie issues
- Directory traversal
And much more...

🌍 **Target Site for ZAP Scan**
This project uses the intentionally vulnerable site http://testphp.vulnweb.com provided by Acunetix for educational testing purposes.

🔧 You can customize the scan to target your own application or local test server by modifying the URL in zap_scan.yml.

🎯 **How to Use This Repo**
🧪 Manual Testing
Clone the repo, install Python dependencies, and run the security tests:
pip install -r requirements.txt
pytest security_tests/

🤖 **Run ZAP Scan in CI/CD**
Go to your GitHub repository → Actions tab → select and run the OWASP ZAP Scan workflow manually.

📂 Reports will be committed back automatically to the zap_reports/ folder after each execution.


🙌 Author
Made with passion by Azhaan — building a QA career through modern, advanced testing practices.


⭐️ If you found this useful
Please give this repo a ⭐️ — it helps others discover it and supports my learning journey!

---
