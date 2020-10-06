# to avoid circular imports and errors with the deployments 
from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
