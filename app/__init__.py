from flask import Flask
from .extensions import db, login_manager, mail, migrate, csrf
from .auth.routes import auth as auth_blueprint
from .main.routes import main as main_blueprint
from .analysis.routes import analysis as analysis_blueprint
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    
    # Register Blueprints
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(analysis_blueprint)
    
    return app
