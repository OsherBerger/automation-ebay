from playwright.sync_api import Page
import random


class BasePage:
    """
    Base class for all Page Objects.

    Provides common browser actions and utilities that are shared
    across all pages in the application (navigation, screenshots,
    human-like waits, etc.).
    """

    def __init__(self, page: Page):
        """
        Initializes the BasePage with a Playwright Page instance.

        Args:
            page (Page): Playwright page object representing the browser tab.
        """
        self.page = page

    def open(self, url: str):
        """
        Navigates the browser to the specified URL.

        This method performs a direct navigation without explicitly
        waiting for full page load, allowing faster test execution.
        Any required waits should be handled by the calling page.

        Args:
            url (str): The URL to navigate to.
        """
        self.page.goto(url)

    def screenshot(self, name: str):
        """
        Captures a screenshot of the current page.

        The screenshot is saved under the 'screenshots/' directory
        with the provided name.

        Args:
            name (str): File name for the screenshot (without extension).
        """
        self.page.screenshot(path=f"screenshots/{name}.png")

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
