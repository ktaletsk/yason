# -*- coding: utf-8 -*-

"""Console script for notebook_scheduler."""
import sys
import click
import notebook_scheduler.notebook_scheduler as ns

@click.group()
def main():
    """Console script for notebook_scheduler."""
    pass

@main.command()
def list():
    ns.list_argo_jobs()

@main.command()
def add():
    ns.schedule_notebook('test.ipynb')

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
