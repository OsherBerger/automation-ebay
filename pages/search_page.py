from pages.base_page import BasePage
from utils.price_parser import parse_price
from locators.search_locators import SearchLocators

class SearchPage(BasePage):
    """
    Page Object representing the eBay search results page.

    This page handles searching for items by keyword, applying price filters,
    iterating through paginated results, and collecting item URLs that fall
    within a specified price range.
    """

    def search_items_under_price(self, query: str, min_price: float, max_price: float, limit: int = 5):
        """
        Searches for items on eBay within a given price range and returns item URLs.

        This method performs a keyword search, applies minimum and maximum
        price filters, parses item prices from the results, and collects
        item links that meet the price criteria. Pagination is handled
        automatically until the desired number of results is reached or
        no more pages are available.

        Args:
            query (str):
                Search keyword to look for (e.g., "shoes", "laptop").
            min_price (float):
                Minimum acceptable item price.
            max_price (float):
                Maximum acceptable item price.
            limit (int, optional):
                Maximum number of valid item URLs to return.
                Defaults to 5.

        Returns:
            list[str]:
                A list of item URLs that match the search query and
                fall within the specified price range.
        """
        # 1️⃣ Search by keyword
        self.page.fill(SearchLocators.SEARCH_INPUT, query)
        self.page.click(SearchLocators.SEARCH_BUTTON)
        
        # 2️⃣ Wait for price filters
        self.page.wait_for_selector(SearchLocators.PRICE_MIN_INPUT)
        self.page.wait_for_selector(SearchLocators.PRICE_MAX_INPUT)

        self.page.wait_for_timeout(500)  
        # 3️⃣ Type min price
        min_input = self.page.locator(SearchLocators.PRICE_MIN_INPUT)
        min_input.click()
        min_input.fill("")
        min_input.type(str(min_price))

        self.page.wait_for_timeout(500)  
        # 4️⃣ Type max price
        max_input = self.page.locator(SearchLocators.PRICE_MAX_INPUT)
        max_input.click()
        max_input.fill("")
        max_input.type(str(max_price))

        # 5️⃣ Apply filter
        self.page.locator(SearchLocators.PRICE_FILTER_APPLY).click()
        self.page.wait_for_timeout(500)  # small wait for page update

        # 6️⃣ Collect items within price limit
        results = []

        while len(results) < limit:
            self.page.wait_for_selector(SearchLocators.ITEM_PRICE)
            prices = self.page.locator(SearchLocators.ITEM_PRICE)
            links = self.page.locator(SearchLocators.ITEM_LINK)

            count = prices.count()

            # Skip first few results if needed (ads, non-relevant)
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

                if price >= float(min_price) and price <= float(max_price):
                    url = link_elem.get_attribute("href")
                    results.append(url)

                if len(results) == limit:
                    break

            # 7️⃣ Check for Next Page using XPath
            next_button = self.page.locator(SearchLocators.NEXT_BUTTON)
            if next_button.count() == 0:
                break

            next_button.click()
            self.page.wait_for_timeout(500)

        return results
