import allure
from pathlib import Path
import random

class BasePage:
    """
    Base page object containing common methods for all pages.

    This class provides helper functions to take screenshots, attach videos
    to Allure reports, and common interactions that might be reused across
    different pages.
    """

    def __init__(self, page):
        """
        Initializes the BasePage.

        Args:
            page (Page): Playwright Page instance to interact with.
        """
        self.page = page


    def open(self, url: str):
        """
        Navigates the Playwright page to the given URL.

        Args:
            url (str): The target URL to open.
        """
        self.page.goto(url)
        
    def screenshot(self, name: str):
        """
        Takes a screenshot of the current page and attaches it to the Allure report.

        Args:
            name (str): Name to identify the screenshot in the report.

        Behavior:
            - Saves screenshot in `screenshots/` directory.
            - Attaches screenshot to Allure report automatically.
        """
        Path("screenshots").mkdir(exist_ok=True)
        path = f"screenshots/{name}_{random.randint(1000,9999)}.png"
        self.page.screenshot(path=path)
        allure.attach.file(path, name=name, attachment_type=allure.attachment_type.PNG)

    def attach_video(self, name: str = "Video Recording"):
        """
        Attaches a video of the current page to the Allure report if available.

        Args:
            name (str): Name to identify the video in the Allure report.

        Behavior:
            - Looks for Playwright's recorded video of the page.
            - Attaches the video to Allure report as WEBM file.
        """
        if hasattr(self.page, "video") and self.page.video:
            video_path = self.page.video.path()
            if Path(video_path).exists():
                allure.attach.file(video_path, name=name, attachment_type=allure.attachment_type.WEBM)

    def human_wait(self, min_ms: int = 100, max_ms: int = 300):
        """
        Waits for a random duration to simulate human-like behavior.

        Useful for reducing bot-like patterns and adding natural delays
        between actions.

        Args:
            min_ms (int, optional): Minimum wait time in milliseconds. Defaults to 100.
            max_ms (int, optional): Maximum wait time in milliseconds. Defaults to 300.
        """
        self.page.wait_for_timeout(random.randint(min_ms, max_ms))
