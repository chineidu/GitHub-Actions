import pandas as pd

from src.main import select_num_variables


def test_select_num_vars(data: pd.DataFrame) -> None:
    """This tests that the output DF contains only numerical variables"""
    # Given
    expected_result = set(['RAM', "Rating", "Price"])

    # When
    result = select_num_variables(data=data)
    print(result.shape)

    # Then
    assert set(result.columns) == expected_result
