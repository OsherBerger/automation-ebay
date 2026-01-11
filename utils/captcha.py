import time
from playwright.sync_api import Page
from locators.common_locators import CommonLocators

def wait_for_captcha(page: Page, timeout=15):
    """Waits for CAPTCHA iframe to appear and be visible."""
    end_time = time.time() + timeout
    while time.time() < end_time:
        captcha_iframes = page.locator(CommonLocators.CAPTCHA_IFRAME)
        visible_count = sum(1 for i in range(captcha_iframes.count())
                            if captcha_iframes.nth(i).is_visible())
        if visible_count > 0:
            print("⚠️ CAPTCHA detected! Solve manually...")
            while sum(1 for i in range(captcha_iframes.count())
                      if captcha_iframes.nth(i).is_visible()) > 0:
                time.sleep(1)
            print("✅ CAPTCHA solved, continuing...")
            return
        time.sleep(0.2)
    print("No CAPTCHA detected, continuing...")
