"""Console script for enki_zero."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for enki_zero."""
    click.echo("Replace this message by putting your code into "
               "enki_zero.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
