from pages.base_page import BasePage
from utils.price_parser import parse_price
from locators.search_selectors import SearchSelectors
class SearchPage(BasePage):

    def search_items_under_price(self, query: str, min_price: float, max_price: float, limit: int = 5):
        self.page.fill(SearchSelectors.SEARCH_INPUT, query)
        self.page.click(SearchSelectors.SEARCH_BUTTON)
        
        # wait for the page and filter inputs to appear
        self.page.wait_for_selector(SearchSelectors.PRICE_MIN_INPUT)
        self.page.wait_for_selector(SearchSelectors.PRICE_MAX_INPUT)
        
        # -----------------------------
        # Type min price
        # -----------------------------
        min_input = self.page.locator(SearchSelectors.PRICE_MIN_INPUT)
        min_input.click()
        min_input.fill("")  # clear existing value
        min_input.type(min_price)  # type slowly, triggers events

        # -----------------------------
        # Type max price
        # -----------------------------
        max_input = self.page.locator(SearchSelectors.PRICE_MAX_INPUT)
        max_input.click()
        max_input.fill("")
        max_input.type(max_price)

        # Apply filter
        self.page.locator(SearchSelectors.PRICE_FILTER_APPLY).click()

        # small wait for results to update
        self.page.wait_for_timeout(1000)

        results = []

        while len(results) < limit:
            self.page.wait_for_selector(SearchSelectors.ITEM_PRICE)
            prices = self.page.locator(SearchSelectors.ITEM_PRICE)
            links = self.page.locator(SearchSelectors.ITEM_LINK)

            count = prices.count()

            # Skip first two items (e.g. ads)
            for i in range(2, count):
                price_elem = prices.nth(i)
                link_elem = links.nth(i)

                if not price_elem.is_visible() or not link_elem.is_visible():
                    continue

                price_text = price_elem.inner_text()
                try:
                    price = parse_price(price_text)
                except ValueError:
                    continue

                if price <= float(max_price) and price >= float(min_price):
                    url = link_elem.get_attribute("href")
                    results.append(url)

                if len(results) == limit:
                    break

            if self.page.locator(SearchSelectors.NEXT_BUTTON).count() == 0:
                break

            self.page.click(SearchSelectors.NEXT_BUTTON)
            self.page.wait_for_timeout(500)

        return results

    