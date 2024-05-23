def get_formatted_name(first: str, last: str, middle: str = "") -> str:
    """generate full name"""
    if middle:
        full_name: str = f"{first} {middle} {last}"
    else:
        full_name: str = f"{first} {last}"
    return full_name.title()
