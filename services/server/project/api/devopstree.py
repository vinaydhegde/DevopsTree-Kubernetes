import os
from sqlalchemy import text
from flask import Blueprint, jsonify, request
from project.api.models import DevopsTree
from project import db


devopstree_blueprint = Blueprint('devopstree', __name__)


@devopstree_blueprint.route('/devopstree', methods=['GET'])
def all_devopstree():
    devopstree = DevopsTree.query.all()[0]
    response = devopstree.get_json()
    return response


if __name__ == '__main__':
    app.run()
