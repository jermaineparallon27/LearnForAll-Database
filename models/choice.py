from extensions import db

class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    choice_text = db.Column(db.String(255), nullable=False)
    is_correct = db.Column(db.Boolean, default=False)