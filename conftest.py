import pytest
import shutil
from pathlib import Path

@pytest.fixture(scope="session", autouse=True)
def clean_artifacts():
    """
    Automatically cleans previous test artifacts before test session starts.

    Cleans the following folders:
        - allure-results/ : previous Allure data
        - screenshots/   : previous screenshots
        - videos/        : previous Playwright video recordings

    Behavior:
        - Ensures Allure report is not duplicated.
        - Ensures each test run starts fresh.
    """
    for folder in ["allure-results", "screenshots", "videos"]:
        if Path(folder).exists():
            shutil.rmtree(folder)
        Path(folder).mkdir(exist_ok=True)
