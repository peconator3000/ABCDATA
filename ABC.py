import click
from app import app, db
from app.models import SModel


@app.cli.command("fillthedata")
@click.argument("path")
def inittestdb(path):
    from app.fillthedata import fill_db
    fill_db(path)


@app.shell_context_processor
def make_shell_context():
   return {'db': db, 'SModel': SModel}
