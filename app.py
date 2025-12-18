import os
import secrets
from flask import Flask, render_template, redirect, url_for, session, request, flash
from extensions import db
from routes.auth import auth_bp
from routes.materials import materials_bp
from routes.quizzes import quizzes_bp
from routes.progress import progress_bp
from routes.admin import admin_bp

# copypaste venv\Scripts\activate

def create_app():
    app = Flask(__name__)
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config['SECRET_KEY'] = 'ea625cd41ff23b3c68d631c1a9e9da14e713dffa6eb1c12cd87348d5e092bfa7'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'learnforall.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(materials_bp)
    app.register_blueprint(quizzes_bp)
    app.register_blueprint(progress_bp)
    app.register_blueprint(admin_bp)

    return app

app = create_app()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test-session')
def test_session():
    return f"User ID in session: {session.get('user_id')}"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)