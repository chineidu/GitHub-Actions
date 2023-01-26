import click


@click.command()
@click.option("-n1", "--num-1", help="The first number", type=float)
@click.option("-n2", "--num-2", help="The second number", type=float)
def add_nums(num_1: float, num_2: float) -> float:
    """This retuns the addition of two numbers."""
    click.echo("Running ...")
    click.echo(num_1 + num_2)
    return num_1 + num_2


if __name__ == "__main__":
    # result = add_nums()
    print(add_nums())
