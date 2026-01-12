class SearchLocators:
    ##xpath requested solution:
    SEARCH_INPUT = "//input[@id='gh-ac']"
    SEARCH_BUTTON = "//button[@id='gh-search-btn']"

    PRICE_MIN_INPUT = "//input[contains(@id,'beginParamValue')]"
    PRICE_MAX_INPUT = "//input[contains(@id,'endParamValue')]"
    PRICE_FILTER_APPLY = "//div[contains(@class,'x-textrange__button')]"

    ITEM_PRICE = "//div[contains(@class,'su-card-container__attributes')]/div[1]"
    ITEM_LINK = "//div[contains(@class,'su-card-container__media')]//div[contains(@class,'su-media')]//a"

    ITEMS_UNDER_MAX_PRICE = (
        "(//div[contains(@class,'su-card-container')]"
        "[.//span[contains(text(),'$') "
        "and number(translate(., '$,₪ ', '')) <= {max_price}]])"
        "[position() <= {limit}]"
    )

    ITEM_LINK_RELATIVE = ".//a"
    NEXT_BUTTON = "//a[contains(@class,'pagination__next')]"

    ##more stable solution
    # SEARCH_INPUT = "#gh-ac"
    # SEARCH_BUTTON = "#gh-search-btn"

    # PRICE_MIN_INPUT = "//input[contains(@id,'beginParamValue')]"
    # PRICE_MAX_INPUT = "//input[contains(@id,'endParamValue')]"
    # PRICE_FILTER_APPLY = "//div[contains(@class,'x-textrange__button')]"

    # ITEM_PRICE = ".su-card-container__attributes > div:nth-child(1)"
    # ITEM_LINK = ".su-card-container__media .su-media a"
    # NEXT_BUTTON = ".s-pagination__container > nav > a"
