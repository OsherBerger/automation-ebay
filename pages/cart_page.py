from pages.base_page import BasePage
from locators.cart_locators import CartLocators
import re

class CartPage(BasePage):

    def get_total(self) -> float:
        """
        Retrieves and parses the cart subtotal value.

        Extracts the numeric value from the cart subtotal element,
        removing currency symbols and formatting characters.

        Returns:
            float: The numeric subtotal value of the cart.

        Raises:
            ValueError: If no numeric value can be parsed from the subtotal text.
        """
        text = self.page.locator(CartLocators.SUBTOTAL_VALUE).inner_text()
        match = re.search(r"[\d,.]+", text)
        if not match:
            raise ValueError(f"Could not parse a numeric total from: {text}")
        return float(match.group().replace(",", ""))

    def assert_total_not_exceeds(self, budget_per_item: float, items_count: int):
        """
        Asserts that the cart total does not exceed the allowed budget.

        The allowed maximum is calculated as:
            budget_per_item * items_count

        Args:
            budget_per_item (float): Maximum allowed price per item.
            items_count (int): Number of items expected in the cart.

        Raises:
            AssertionError: If the cart total exceeds the allowed budget.
        """
        total = self.get_total()
        print("Total is:",total)
        assert total <= budget_per_item * items_count
