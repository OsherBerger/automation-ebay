import re

def parse_price(text: str) -> float:
    """
    Extracts the first price number from eBay price text.
    Handles "$", "US $", "ILS", and ranges like "100–200".
    """
    match = re.search(r"(\d+[.,]?\d*)", text)
    if match:
        price = match.group(1).replace(",", ".")
        return float(price)
    else:
        raise ValueError(f"Could not parse price from text: {text}")
