# 🚀 Automation eBay Project

This is an automated testing project for eBay using **Playwright**, Python, and **Pytest**.  
It implements a Page Object Model (POM) architecture to manage pages, selectors, and test flows.



## 🔹 Prerequisites ✅

- 🐍 Python 3.11+
- 🌐 Node.js (required for Playwright)
- 🔧 Git (for version control)
- 💻 Recommended: VS Code or another IDE



## 🔹 Setting up the environment ⚙️

1. **Clone the repository** 

- git clone https://github.com/OsherBerger/automation-ebay.git
- cd automation-ebay

2. **Create and activate the virtual environment**

- python -m venv venv
- venv\Scripts\activate      # Windows
- source venv/bin/activate   # macOS / Linux

3. **Install dependencies**

- pip install -r requirements.txt
- playwright install


## 🔹 Running tests 🧪
    Run a single test:
- pytest tests/test_e2e_flow.py -s 
    Run all tests with Allure report:
- ar.bat # also 'ar' works   

Optional flags:

-s : Show print statements in real-time

--maxfail=1 : Stop after first failure

--alluredir=allure-results : Output for Allure reports

## 🔹 Allure CLI Setup ✨
To simplify Allure setup, the project includes a helper script:

- Windows: install_allure.bat

- macOS / Linux: install_allure.sh (if provided)

What it does:

1.Downloads the latest Allure CLI release.

2.Extracts it to a permanent folder (default: %USERPROFILE%\allure on Windows).

3.Adds allure/bin to your system PATH automatically.

Usage:

# Run in the project folder
install_allure.bat

# Check installation
allure --version


Notes:

- Run this script once per machine.

- If your PATH already includes Allure, you can skip this step.

- After setup, generate reports easily with:

ar.bat # also 'ar' works  (custom script to serve Allure reports)
    or
allure serve allure-results


⚠️ Important: The custom ar.bat script automatically clears previous results before serving the new report to avoid duplicates.

## 🔹 Architecture 🏗️

pages/ → Page Objects (CartPage, ItemPage, SearchPage, BasePage)

locators/ → All locators separated by page

tests/ → Test scripts using Pytest

utils/ → Helper functions (price parsing, CAPTCHA wait)

data/ → Test data JSON files

POM Pattern:

Each page class contains interactions for a specific page.
Selectors are stored in separate files for maintainability.


## 🔹 Known limitations / assumptions ⚠️
Login is stubbed; all flows assume guest users.

Prices are handled in USD/ILS; currency detection is minimal.

CAPTCHA requires manual solving.

Some dropdowns may be skipped if out-of-stock.

## 🔹 Screenshots & Reports 📸
Screenshots are saved in screenshots/ automatically.

Allure reports can be generated using:
- ar.bat # also 'ar' works
    or 
- pytest tests/ -s --alluredir=allure-results
- allure serve allure-results

## 🔹 Notes 📝
Temporary folders and files are excluded from Git via .gitignore to reduce noise:

venv/
screenshots/
allure-results/
playwright-profile*
ebay_profile/


## **.gitignore** 📂

### Python
_pycache__/
*.py[cod]
*.pyo
*.pyc
*.pyd
*.env
venv/
env/
*.egg-info/
dist/
build/

### Playwright
playwright-report/
screenshots/

### Allure reports
allure-report/
allure-results/

### Pytest
.cache/
.pytest_cache/

### IDEs / Editors
.vscode/
.idea/
*.sublime-project
*.sublime-workspace

### OS
.DS_Store
Thumbs.db

### Playwright user data / browser profiles
playwright-profile*/
ebay_profile/
