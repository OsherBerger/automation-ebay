# Automation eBay Project

This is an automated testing project for eBay using **Playwright**, Python, and **Pytest**.  
It implements a Page Object Model (POM) architecture to manage pages, selectors, and test flows.

---

## 🔹 Prerequisites

- Python 3.11+
- Node.js (required for Playwright)
- Git (for version control)
- Recommended: VS Code or another IDE

---

## 🔹 Setting up the environment (run commands via terminal)

1. **Clone the repository** 

git clone https://github.com/OsherBerger/automation-ebay.git
cd automation-ebay

2. **Create and activate the virtual environment**

python -m venv venv
venv\Scripts\activate      # Windows OS
source venv/bin/activate   # macOS / Linux OS

3. **Install dependencies**

pip install -r requirements.txt
playwright install


🔹 Running tests
Run the end-to-end flow:
pytest tests/test_e2e_flow.py -s

Optional:
-s : Show print statements in real-time
--maxfail=1 : Stop after first failure
--alluredir=allure-results : Output for Allure reports

🔹 Architecture
pages/ → Page Objects (CartPage, ItemPage, SearchPage, BasePage)

locators/ → All locators separated by page

tests/ → Test scripts using Pytest

utils/ → Helper functions (price parsing, CAPTCHA wait)

data/ → Test data JSON files

POM Pattern: Each page class contains interactions for a specific page.
Selectors are stored in separate files for maintainability.

🔹 Known limitations / assumptions
Login is stubbed; all flows assume guest users.

Prices are handled in USD/ILS; currency detection is minimal.

CAPTCHA requires manual solving.

Some dropdowns may be skipped if out-of-stock.

🔹 Screenshots & Reports
Screenshots are saved in screenshots/ automatically.

Allure reports can be generated using:
allure serve allure-results

🔹 Notes
Temporary folders and files are excluded from Git via .gitignore to reduce noise:

venv/
screenshots/
allure-results/
playwright-profile*
ebay_profile/


### **.gitignore**

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.env
*.venv
venv/
env/
*.swp

# Playwright
playwright-report/
playwright-profile*/  # temporary browser profiles

# Screenshots
screenshots/

# Allure reports
allure-results/

# IDE / Editor
.vscode/
.idea/

# eBay specific temp folder
ebay_profile/

# System files
.DS_Store
Thumbs.db
