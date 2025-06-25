from flask import Flask 



def create_app():
    app = Flask(__name__)

    from app.routes import plan
    app.register_blueprint(plan)
    return app