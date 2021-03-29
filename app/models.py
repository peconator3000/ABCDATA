from app import db


class SModel(db.Model):
    __tablename__ = "object"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    path= db.Column(db.String(120), index=True, unique=False)
    def __init__(self,name,path):
        self.name=name
        self.path=path
    def ReturnPath(self):
        return str(self.path)
    def __repr__(self):
        return '<{}>'.format(self.path)
