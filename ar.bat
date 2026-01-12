@echo off
REM Shortcut to run tests and serve Allure report
REM This version clears previous Allure results to avoid duplicates

REM 1️⃣ Activate virtual environment
call venv\Scripts\activate.bat

REM 2️⃣ Remove previous Allure results if exist
IF EXIST videos rmdir /s /q videos
IF EXIST screenshots rmdir /s /q screenshots
IF EXIST allure-results rmdir /s /q allure-results

REM 3️⃣ Create folders again
mkdir videos
mkdir screenshots
mkdir allure-results

REM 4️⃣ Run pytest with Allure results and video recording
pytest tests/ -s --alluredir=allure-results

REM 5️⃣ Serve Allure report
allure serve allure-results


pause

