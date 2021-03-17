from app import app, db
from app.models import SModel


@app.shell_context_processor
def make_shell_context():
   return {'db': db, 'SModel': SModel}
