from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from extensions import db
from models.material import Material
from models.quiz import Quiz
from models.question import Question
from models.choice import Choice
import os
from werkzeug.utils import secure_filename

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# ----------- Material CRUD ----------- 
@admin_bp.route('/materials')
def admin_materials():
    materials = Material.query.all()
    return render_template('admin/materials_list.html', materials=materials)

@admin_bp.route('/materials/create', methods=['GET', 'POST'])
def create_material():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        category = request.form.get('category')
        file = request.files.get('file')

        file_path = None
        if file:
            filename = secure_filename(file.filename)
            storage_dir = os.path.join(current_app.root_path, 'static', 'materials')
            os.makedirs(storage_dir, exist_ok=True)
            file.save(os.path.join(storage_dir, filename))
            file_path = filename

        material = Material(
            title=request.form.get('title'),
            description=request.form.get('description'),
            category=request.form.get('category'),
            file_path=file_path
        )
        db.session.add(material)
        db.session.commit()
        return redirect(url_for('admin.admin_materials'))
    return render_template('admin/materials_form.html')

@admin_bp.route('/materials/<int:material_id>/edit', methods=['GET', 'POST'], endpoint='edit_material')
def edit_material(material_id):
    material = Material.query.get_or_404(material_id)

    if request.method == 'POST':
        material.title = request.form.get('title')
        material.description = request.form.get('description')
        material.category = request.form.get('category')

        file = request.files.get('file')
        if file:
            # remove old file if exists
            if material.file_path and os.path.exists(material.file_path):
                os.remove(material.file_path)
            filename = secure_filename(file.filename)
            storage = os.path.join('static', 'materials')
            os.makedirs(storage, exist_ok=True)
            material.file_path = os.path.join(storage, filename)
            file.save(material.file_path)

        db.session.commit()
        return redirect(url_for('admin.admin_materials'))
    return render_template('admin/materials_form.html', material=material)

@admin_bp.route('/materials/<int:material_id>/delete', methods=["POST"], endpoint='delete_material')
def delete_material(material_id):
    material = Material.query.get_or_404(material_id)
    if material.file_path and os.path.exists(material.file_path):
        os.remove(material.file_path)
    db.session.delete(material)
    db.session.commit()
    return redirect(url_for('admin.admin_materials'))

#  ----------- Quiz CRUD  ----------- 
@admin_bp.route('/quizzes')
def admin_quizzes():
    quizzes = Quiz.query.all()
    return render_template('admin/quizzes_list.html', quizzes=quizzes)

@admin_bp.route('/quizzes/create', methods=['GET', 'POST'])
def create_quiz():
    if request.method == 'POST':
        title = request.form.get('title')
        quiz = Quiz(title=title)
        db.session.add(quiz)
        db.session.commit()
        return redirect(url_for('admin.admin_quizzes'))
    return render_template('admin/quizzes_form.html')

@admin_bp.route('/quizzes/<int:quiz_id>/edit', methods=['GET', 'POST'], endpoint='edit_quiz')
def edit_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    if request.method == 'POST':
        quiz.title = request.form.get('title')
        db.session.commit()
        return redirect(url_for('admin.admin_quizzes'))
    return render_template('admin/quizzes_form.html', quiz=quiz)

@admin_bp.route('/quizzes/<int:quiz_id>/delete', methods=['POST'], endpoint='delete_quiz')
def delete_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    db.session.delete(quiz)
    db.session.commit()
    return redirect(url_for('admin.admin_quizzes'))

#  ----------- Question CRUD  -----------
@admin_bp.route('/quizzes/<int:quiz_id>/questions')
def quiz_questions(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz.id).all()
    return render_template('admin/questions_list.html', quiz=quiz, questions=questions)

@admin_bp.route('/quizzes/<int:quiz_id>/questions/create', methods=['GET', 'POST'])
def create_question(quiz_id):
    if request.method == 'POST':
        q_text = request.form.get('question_text')
        a = request.form.get('choice_a')
        b = request.form.get('choice_b')
        c = request.form.get('choice_c')
        d = request.form.get('choice_d')
        correct = request.form.get('correct_choice')

        q = Question(
            quiz_id=quiz_id,
            question_text=q_text,
            choice_a=a,
            choice_b=b,
            choice_c=c,
            choice_d=d,
            correct_choice=correct
        )
        db.session.add(q)
        db.session.commit()

        return redirect(url_for('admin.quiz_questions', quiz_id=quiz_id))
    return render_template('admin/questions_form.html', quiz_id=quiz_id)

@admin_bp.route('/quizzes/<int:quiz_id>/questions/<int:question_id>/edit', methods=['GET', 'POST'], endpoint='edit_question')
def edit_question(quiz_id, question_id):
    q = Question.query.get_or_404(question_id)
    if request.method == 'POST':
        q.question_text = request.form.get('text')
        db.session.commit()
        return redirect(url_for('admin.quiz_questions', quiz_id=quiz_id))
    return render_template('admin/questions_form.html', quiz_id=quiz_id, question=q)

@admin_bp.route('/quizzes/<int:quiz_id>/questions/<int:question_id>/delete', methods=['POST'], endpoint='delete_question')
def delete_question(quiz_id, question_id):
    q = Question.query.get_or_404(question_id)
    db.session.delete(q)
    db.session.commit()
    return redirect(url_for('admin.quiz_questions', quiz_id=quiz_id))

@admin_bp.route('/questions/<int:question_id>/choices')
def question_choices(question_id):
    question = Question.query.get_or_404(question_id)
    choices = Choice.query.filter_by(question_id=question.id).all()
    return render_template('admin/choices_list.html', question=question, choices=choices)

@admin_bp.route('/questions/<int:question_id>/choices/create', methods=['GET', 'POST'])
def create_choice(question_id):
    if request.method == 'POST':
        text = request.form.get('text')
        is_correct = True if request.form.get('is_correct') else False
        choice = Choice(question_id=question_id, choice_text=text, is_correct=is_correct)
        db.session.add(choice)
        db.session.commit()
        return redirect(url_for('admin.question_choices', question_id=question_id))
    return render_template('admin/choices_form.html', question_id=question_id)