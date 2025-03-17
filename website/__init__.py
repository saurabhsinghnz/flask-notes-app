from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

db = SQLAlchemy()
DB_NAME = "database.db"
DB_PATH = Path(__file__).parent / DB_NAME

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    return app

def create_database(app):
    if not DB_PATH.exists():
        with app.app_context():
            db.create_all()
            print('Created Database!')
    else:
        print('Found Database!')
