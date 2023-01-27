import pandas as pd
import pytest

from src.utils import load_data


@pytest.fixture()
def data() -> pd.DataFrame:
    """This loads the data."""
    return load_data(filename="./data/Laptop.csv")
