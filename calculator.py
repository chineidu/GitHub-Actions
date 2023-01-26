import click


@click.command()
@click.option("--num-1", help="The first number", type=float)
@click.option("--num-2", help="The second number", type=float)
def add_nums(num_1:float, num_2:float) -> float:
    """This retuns the addition of two numbers."""
    click.echo("Running ...")
    click.echo(num_1 + num_2)



if __name__ == "__main__":
    print(add_nums())
    # print(func_2())
