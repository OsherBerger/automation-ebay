from pages.base_page import BasePage
from playwright.sync_api import TimeoutError
from locators.item_locators import ItemLocators
import random


class ItemPage(BasePage):
    """
    Page Object representing an individual item/product page.

    This page handles variant selection (such as size, color, style, width)
    and the process of adding an item to the shopping cart.
    """

    def choose_all_variants(self, pick_second: bool = True):
        """
        Selects valid options for all relevant product variants.

        This method iterates through all variant dropdowns (e.g. size, color,
        style, width), opens each dropdown, and selects a valid option while
        skipping placeholders and out-of-stock/disabled entries.

        The selection strategy can be controlled via the `pick_second` flag.

        Args:
            pick_second (bool, optional):
                If True, selects the first valid option after the placeholder.
                If False, selects a random valid option.
                Defaults to True.

        Behavior:
            - Skips hidden variant dropdowns.
            - Ignores dropdowns that are not related to known variant types.
            - Avoids selecting disabled or out-of-stock options.
            - Safely continues if no valid option is found for a dropdown.
        """
        buttons = self.page.locator(ItemLocators.VARIANT_BUTTONS)

        for i in range(buttons.count()):
            button = buttons.nth(i)

            if not button.is_visible():
                continue

            text = button.inner_text().lower()
            if not any(k in text for k in ["size", "color", "style", "width"]):
                continue

            # Open the dropdown
            button.click()
            self.page.wait_for_timeout(150)

            # Resolve options related specifically to this dropdown
            dropdown_id = button.get_attribute("aria-controls")
            if dropdown_id:
                options = self.page.locator(f"#{dropdown_id} .listbox__option")
            else:
                # Fallback: only visible options
                options = self.page.locator(".listbox__option:visible")

            # Collect valid (enabled & visible) options
            valid_options = []
            for j in range(1, options.count()):  # skip placeholder
                option = options.nth(j)

                if not option.is_visible():
                    continue
                if ItemLocators.OUT_OF_STOCK_CLASS in (option.get_attribute("class") or ""):
                    continue

                valid_options.append(option)

            if not valid_options:
                print(f"⚠️ No valid options for '{text}', skipping this dropdown")
                continue

            # Select option
            selected_option = (
                valid_options[0]
                if pick_second
                else random.choice(valid_options)
            )
            selected_option.click()
            self.page.wait_for_timeout(150)

    def add_to_cart(self, pick_second: bool = True):
        """
        Adds the current item to the shopping cart.

        This method attempts to select all required product variants before
        clicking the 'Add to Cart' button. Variant selection failures are
        handled gracefully to prevent test interruption.

        Args:
            pick_second (bool, optional):
                Passed through to variant selection logic to control
                how options are chosen. Defaults to True.

        Behavior:
            - Attempts variant selection with fault tolerance.
            - Waits for the 'Add to Cart' button to be available.
            - Takes a screenshot after the item is added to the cart.
        """
        try:
            self.choose_all_variants(pick_second=pick_second)
        except TimeoutError:
            # Variant selection may fail on some items; continue gracefully
            pass

        self.page.wait_for_selector(ItemLocators.ADD_TO_CART)
        self.page.click(ItemLocators.ADD_TO_CART)
        self.screenshot(f"cart_item_added_{random.randint(1000, 9999)}.png")
