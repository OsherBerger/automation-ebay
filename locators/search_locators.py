class SearchLocators:
    SEARCH_INPUT = "#gh-ac"
    SEARCH_BUTTON = "#gh-search-btn"

    PRICE_MIN_INPUT = "//input[contains(@id,'beginParamValue')]"
    PRICE_MAX_INPUT = "//input[contains(@id,'endParamValue')]"
    PRICE_FILTER_APPLY = "//div[contains(@class,'x-textrange__button')]"

    ITEM_PRICE = ".su-card-container__attributes > div:nth-child(1)"
    ITEM_LINK = ".su-card-container__media .su-media a"
    NEXT_BUTTON = ".s-pagination__container > nav > a"
