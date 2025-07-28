from flask import Flask, render_template
from flask_migrate import Migrate
import config
from app.extensions import bcrypt, restx_api, jwt
from flask_sqlalchemy import SQLAlchemy
from config import config
import os


migrate = Migrate()

db = SQLAlchemy()

def create_app(config_class="config.DevelopmentConfig"):

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..'))
    app = Flask(
        __name__, 
        template_folder=os.path.join(PROJECT_ROOT, 'templates'),
        static_folder=os.path.join(PROJECT_ROOT, 'static')
        )
    app.config.from_object(config_class)
    print("App created")

    bcrypt.init_app(app)
    restx_api.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    migrate.init_app(app, db)

    from app.api.v1.users import api as users_ns
    from app.api.v1.admin import admin_api
    from app.api.v1.places import api as places_ns
    from app.api.v1.amenities import api as amenities_ns
    from app.api.v1.reviews import api as reviews_ns
    from app.api.v1.auth import api as auth_ns
    

    restx_api.add_namespace(users_ns, path='/api/v1/users')
    restx_api.add_namespace(places_ns, path='/api/v1/places')
    restx_api.add_namespace(amenities_ns, path='/api/v1/amenities')
    restx_api.add_namespace(reviews_ns, path='/api/v1/reviews')
    restx_api.add_namespace(auth_ns, path='/api/v1/auth')
    restx_api.add_namespace(admin_api, path='/api/v1/admin')

    @app.route('/index')
    def index():
        """Render the index page."""
        return render_template('index.html')
    
    @app.route('/login')
    def login():
        """Render the login page."""
        return render_template('login.html')
    
    @app.route('/place/<place_id>')
    def place(place_id):    
        """Render the place page."""
        return render_template('place.html', place_id=place_id)

    return app
