# -*- coding: utf-8 -*-

"""Console script for notebook_scheduler."""
import sys
import click
import yason.yason as ys

@click.group()
def main():
    """Console script for notebook_scheduler."""
    pass

@main.command()
def list():
    ys.list_argo_jobs()

@main.command()
@click.argument('filename')
def add(filename):
    ys.schedule_notebook(filename)

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
