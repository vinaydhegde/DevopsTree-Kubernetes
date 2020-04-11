from project import create_app, db
from project.api.models import DevopsTree
from flask.cli import FlaskGroup
import json
import os
app = create_app()
cli = FlaskGroup(create_app=create_app)
data_json_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),"data.json")
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('bootstrap_db')
def bootstrap_db():
    """Seeds the database."""
    print("Seeding the database") 
    with open(data_json_file) as f:
        data = json.load(f) 
    db.session.add(DevopsTree(data))   
    db.session.commit()


if __name__ == '__main__':
    cli()
