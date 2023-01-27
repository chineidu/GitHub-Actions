import pandas as pd


def load_data(filename: str) -> float:
    """This retuns a Pandas DataFrame."""
    df = pd.read_csv(filename)
    print(f"Shape of df: {df.shape}\n")
    return df
