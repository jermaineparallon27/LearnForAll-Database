from extensions import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    choice_a = db.Column(db.String(255), nullable=False)
    choice_b = db.Column(db.String(255), nullable=False)
    choice_c = db.Column(db.String(255), nullable=False)
    choice_d = db.Column(db.String(255), nullable=False)
    correct_choice = db.Column(db.String(1), nullable=False)