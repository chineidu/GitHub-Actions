import pandas as pd

from src.utils import load_data

filename = "data/Laptop.csv"
data = load_data(filename=filename)


def select_num_variables(*, data: pd.DataFrame) -> pd.DataFrame:
    """This returns a DF containing only numerical variables."""
    # Select only numerical variables
    data_num = data.select_dtypes(include=["int", "float"]).iloc[:, 1:]
    return data_num
