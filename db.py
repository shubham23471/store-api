from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# to testout changes in the git in this folder 


 from db import db
    db.init_app(app)