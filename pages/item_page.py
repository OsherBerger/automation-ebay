from pages.base_page import BasePage
from playwright.sync_api import TimeoutError
from locators.item_locators import ItemLocators
import random
import time

class ItemPage(BasePage):
    """
    Page Object representing an individual eBay product/item page.

    Responsibilities:
        - Select product variants (size, color, style, width, quantity).
        - Skip out-of-stock or disabled options.
        - Add item to the cart.
        - Attach screenshots and video recordings for Allure reports.
    """

    def choose_all_variants(self, pick_second: bool = True):
        """
        Selects valid options for all relevant product variants on the item page.

        Args:
            pick_second (bool, optional): If True, selects the first valid option
                after the placeholder. If False, selects a random valid option.
                Defaults to True.

        Behavior:
            - Iterates through all variant dropdowns.
            - Skips hidden or non-relevant dropdowns.
            - Ignores out-of-stock/disabled options.
            - Continues gracefully if no valid option is available.
        """
        buttons = self.page.locator(ItemLocators.VARIANT_BUTTONS)

        for i in range(buttons.count()):
            button = buttons.nth(i)
            if not button.is_visible():
                continue

            text = button.inner_text().lower()
            if not any(k in text for k in ["size", "color","colour", "style", "width","qty"]):
                continue

            button.click()
            self.page.wait_for_timeout(150)

            dropdown_id = button.get_attribute("aria-controls")
            if dropdown_id:
                options = self.page.locator(f"#{dropdown_id} .listbox__option")
            else:
                options = self.page.locator(".listbox__option:visible")

            valid_options = []
            for j in range(1, options.count()):
                option = options.nth(j)
                if not option.is_visible():
                    continue
                if ItemLocators.OUT_OF_STOCK_CLASS in (option.get_attribute("class") or ""):
                    continue
                valid_options.append(option)

            if not valid_options:
                print(f"⚠️ No valid options for '{text}', skipping this dropdown")
                continue

            selected_option = valid_options[0] if pick_second else random.choice(valid_options)
            selected_option.click()
            self.page.wait_for_timeout(150)

    def add_to_cart(self, pick_second: bool = True):
        """
        Adds the current item to the shopping cart.

        Args:
            pick_second (bool, optional): Passed to variant selection logic
                to control which options are chosen. Defaults to True.

        Behavior:
            - Attempts variant selection.
            - Waits for the 'Add to Cart' button.
            - Clicks the button to add the item to cart.
            - Captures screenshot and video recording for Allure report.
        """
        try:
            self.choose_all_variants(pick_second=pick_second)
        except TimeoutError:
            pass

        self.page.wait_for_selector(ItemLocators.ADD_TO_CART)
        self.page.click(ItemLocators.ADD_TO_CART)

        # 📸 Screenshot after adding to cart
        time.sleep(3)
        self.screenshot("item_added")

