import click

import pandas as pd


@click.command()
@click.option("-f", "--filename", help="The filename")
def load_data(filename: str) -> float:
    """This retuns a Pandas DataFrame."""
    df = pd.read_csv(filename)
    return df
