# Skeleton of a CLI

import click

import ejotl


@click.command('ejotl')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(ejotl.has_legs)
