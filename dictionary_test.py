"""Testing Dictionaries Function Practice."""
from exercises.ex07.dictionary import invert, favorite_color, count

__author__: "730530011"


def test_no_dict() -> None:
    """Testing with no dictionaries."""
    assert invert([]) == {}


def test_three_dicts() -> None:
    """Testing with three dicts."""
    test_dict: dict[str, str] = {'tree': 'apple', 'dog': 'hot', 'jeep': 'red'}
    assert invert(test_dict) == {'apple': 'tree', 'hot': 'dog', 'red': 'jeep'}


def test_with_num_string() -> None:
    """Testing with number strings."""
    test_dict: dict[str, str] = {'5': '1', '2': '0'}
    assert invert(test_dict) == {'1': '5', '0': '2'}


def test_none_favorite_color() -> None:
    """Testing favorite_color with no dict."""
    assert favorite_color([]) == ""


def test_same_color() -> None:
    """Testng favorite_color with same number of color occurances."""
    test_dict: dict[str, str] = {'Jack': 'blue', 'Liam': 'blue', 'Ethan': 'blue'}
    assert favorite_color(test_dict) == 'blue'


def test_differente_amount() -> None:
    """Testng favorite_color with same number of color occurances."""
    test_dict: dict[str, str] = {'Jack': 'blue', 'Liam': 'red', 'Ethan': 'green', 'Zach': 'red'}
    assert favorite_color(test_dict) == 'red'


def test_none_count() -> None:
    """Testing count with no dict."""
    assert count([]) == {}


def test_one_of_each() -> None:
    """Testing count when each value of the list appears once."""
    test_list = ['ham', 'turkey', 'pork', 'steak']
    assert count(test_list) == {'ham': 1, 'turkey': 1, 'pork': 1, 'steak': 1}


def test_two_of_one() -> None:
    """Testing count when one value appears twice in the list."""
    test_list = ['padres', 'dodgers', 'd_backs', 'padres', 'giants']
    assert count(test_list) == {'padres': 2, 'dodgers': 1, 'd_backs': 1, 'giants': 1}
