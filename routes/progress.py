from flask import Blueprint, redirect, render_template, session, url_for, flash
from models.quiz import Quiz
from models.result import QuizResult
from extensions import db

progress_bp = Blueprint('progress', __name__, url_prefix='/prefix')

@progress_bp.route('/')
def progress_dashboard():
    user_id = session.get('user_id')
    if not user_id:
        return render_template('progress/dashboard.html', results=[])
    
    results = (
        db.session.query(QuizResult, Quiz)
        .join(Quiz, Quiz.id == QuizResult.quiz_id)
        .filter(QuizResult.user_id == user_id)
        .all()
    )

    return render_template('progress/dashboard.html', results=results)

@progress_bp.route('/clear', methods=['POST'])
def clear_progress():
    user_id = session.get('user_id')
    if not user_id:
        flash("No user logged in.")
        return redirect(url_for('auth.login'))
    
    QuizResult.query.filter_by(user_id=user_id).delete()
    db.session.commit()
    flash("Progress cleared.")
    return redirect(url_for('progress.progress_dashboard'))