"""Dictionary Function Practice."""


def invert(orig_dict: dict[str, str]) -> dict[str, str]: 
    """Given a dictionary with strings for both keys and values return the keys as values and keys as values."""
    dicts_inv: dict[str, str] = {}
    
    for key in orig_dict:
        if orig_dict[key] in dicts_inv:
            raise KeyError("Values cannot be the same!")
        dicts_inv[orig_dict[key]] = key
    return dicts_inv


def favorite_color(dict_color: dict[str, str]) -> str:
    """Given a dictionary with strings for keys and values, return the value to occurs the most."""
    new_list: list[str] = {}

    for key in dict_color:
        color = dict_color[key]
        if color in new_list:
            new_list[color] = new_list[color] + 1
        else:
            new_list[color] = 1
    most_common_value: str = ""
    most_freq: int = 0
    for color in new_list:
        if new_list[color] > most_freq:
            most_freq = new_list[color]
            most_common_value = color
    return most_common_value
    

def count(count_list: list[str]) -> dict[str, int]:
    """Creating a dictionary where each key creates a unique value."""
    new_dict: dict[str, int] = {}

    for key in count_list:
        if key in new_dict:
            new_dict[key] = new_dict[key] + 1
        else:
            new_dict[key] = 1
    return new_dict

        
