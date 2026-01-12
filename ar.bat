@echo off
REM Shortcut to run tests and serve Allure report
REM This version clears previous Allure results to avoid duplicates

REM 1️⃣ Activate virtual environment
call venv\Scripts\activate.bat

REM 2️⃣ Remove previous Allure results if exist
if exist allure-results (
    rmdir /s /q allure-results
)

REM 3️⃣ Run pytest with Allure output
pytest tests/ -s --alluredir=allure-results

REM 4️⃣ Serve Allure report
allure serve allure-results

pause
