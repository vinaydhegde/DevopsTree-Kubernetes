from sqlalchemy.dialects.postgresql import JSON
from flask import current_app
from sqlalchemy.sql import func

from project import db


class DevopsTree(db.Model):
   
    __tablename__ = 'devopstree'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    devops_tree = db.Column(JSON)


    def __init__(self, devops_tree):
        self.devops_tree=devops_tree

    def get_json(self):
        
        return self.devops_tree
