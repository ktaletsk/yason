# -*- coding: utf-8 -*-

"""Console script for notebook_scheduler."""
import sys
import click
import yason.yason as ys

@click.group()
def main():
    """Welcome to yason CLI."""
    pass

@main.command()
def list():
    ys.list_argo_jobs()

@main.command()
@click.argument('filename')
def add(filename):
    ys.schedule_notebook(filename)

@main.command()
@click.argument('filename')
def delete(filename):
    ys.delete_workflow(filename)

@main.command()
@click.argument('jobname', nargs=1)
@click.argument('destination', nargs=1)
def get(jobname, destination):
    ys.get_workflow(jobname, destination)

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
