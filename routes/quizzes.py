from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from extensions import db
from models.quiz import Quiz
from models.question import Question
from models.result import QuizResult
from models.user import User


quizzes_bp = Blueprint('quizzes', __name__, url_prefix='/quizzes')

@quizzes_bp.route('/create', methods=['GET', 'POST'])
def create_quiz():
    if request.method == "POST":
        title = request.form.get('title')
        description = request.form.get('description')
        quiz = Quiz(title=title, description=description)
        db.session.add(quiz)
        db.session.commit()

        quiz_id = quiz.id

        questions = request.form.getlist('question[]')
        choices_a = request.form.getlist('choice_a[]')
        choices_b = request.form.getlist('choice_b[]')
        choices_c = request.form.getlist('choice_c[]')
        choices_d = request.form.getlist('choice_d[]')
        answers = request.form.getlist('answer[]')

        for i in range(len(questions)):
            q = Question(
                quiz_id=quiz_id,
                question=questions[i],
                choice_a=choices_a[i],
                choice_b=choices_b[i],
                choice_c=choices_c[i],
                choice_d=choices_d[i],
                correct_answer=answers[i]
            )
            db.session.add(q)
        db.session.commit()
        return redirect(url_for('quiz.manage_quiz'))
    return render_template('quiz/create_quiz.html')

@quizzes_bp.route('/')
def list_quizzes():
    quizzes = Quiz.query.all()
    return render_template('quizzes/list.html', quizzes=quizzes)

@quizzes_bp.route('/<int:quiz_id>/start', methods=['GET', 'POST'])
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz.id).all()

    if request.method == 'POST':
        score = 0
        for question in questions:
            selected = request.form.get(f'q{question.id}')
            print(f"Question {question.id}: selected={selected}, correct={question.correct_choice}")
            if selected == question.correct_choice:
                score += 1

        result = QuizResult(
            user_id = session.get('user_id'),
            quiz_id = quiz.id,
            score = score
        )
        db.session.add(result)
        db.session.commit()

        flash(f'You scored {score} points.')
        return redirect(url_for('quizzes.list_quizzes'))
    return render_template('quizzes/take_quiz.html', quiz=quiz, questions=questions)