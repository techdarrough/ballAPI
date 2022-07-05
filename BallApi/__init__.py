
from flask import Flask
from flask_migrate import Migrate


# app Fact

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgressql://postgres:postgres@localhost:5432/ballAPI'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello():
        return {'response': 'Welcome to ballAPI',
                'category1': 'reptiles'}

    

    @app.route('/')
    def not_found(error):
        return {
            "error": error,
            "message": "Not Found"
        }

    from . import reptile
    app.register_blueprint(reptile.bp)

    return app
