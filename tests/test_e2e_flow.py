import json
import random
from playwright.sync_api import sync_playwright, TimeoutError
from pages.search_page import SearchPage
from pages.item_page import ItemPage
from pages.cart_page import CartPage
from utils.captcha import wait_for_captcha

def test_full_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page(record_video_dir="videos/")

        data = json.load(open("data/test_data.json"))

        search = SearchPage(page)
        item = ItemPage(page)
        cart = CartPage(page)

        print("Opening eBay...")
        search.open("https://www.ebay.com")

        print(f"Searching items: {data['query']} above {data['min_price']} and under {data['max_price']}")
        urls = search.search_items_under_price(
            data["query"], data["min_price"], data["max_price"], data["limit"]
        )

        print(f"Found {len(urls)} valid items.")
        for index, url in enumerate(urls):
            print(f"Navigating to item {index+1}: {url}")
            page.goto(url, wait_until="domcontentloaded")
            wait_for_captcha(page)
            try:
                item.add_to_cart()
            except TimeoutError:
                print(f"⚠️ Failed to add item {index+1}, skipping...")
            item.human_wait(500, 1000)

        print("Going to cart to assert totals...")
        page.goto("https://cart.ebay.com",wait_until="domcontentloaded")
        wait_for_captcha(page)
        cart.assert_total_not_exceeds(float(data["max_price"]), len(urls))
        cart.screenshot(f"cart_subtotal{random.randint(1000,9999)}.png")


        print("✅ Test completed successfully!")
        browser.close()
