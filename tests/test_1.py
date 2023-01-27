import pandas as pd

from src.calculator import add_nums
from src.main import select_num_variables


def test_select_num_vars(data: pd.DataFrame) -> None:
    """This tests that the output DF contains only numerical variables"""
    # Given
    expected_result = set(['RAM', "Rating", "Price"])

    # When
    result = select_num_variables(data=data)

    # Then
    assert set(result.columns) == expected_result


def test_calculator() -> None:
    """This tests that the output DF contains only numerical variables"""
    # Given
    expected_result = 5

    # When
    result = add_nums(num_1=2, num_2=3)

    # Then
    assert result == expected_result
