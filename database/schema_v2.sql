CREATE TABLE question (
    question_id INT PRIMARY KEY AUTO_INCREMENT,
    quiz_id INT NOT NULL,
    question_text TEXT NOT NULL,
    choice_a VARCHAR(255) NOT NULL,
    choice_b VARCHAR(255) NOT NULL,
    choice_c VARCHAR(255) NOT NULL,
    choice_d VARCHAR(255) NOT NULL,
    correct_answer CHAR(1) NOT NULL,
    CONSTRAINT fk_question_quiz
        FOREIGN KEY (quiz_id)
        REFERENCES quiz(quiz_id)
        ON DELETE CASCADE
);

CREATE TABLE choice (
    choice_id INT PRIMARY KEY AUTO_INCREMENT,
    question_id INT NOT NULL,
    choice_text VARCHAR(255) NOT NULL,
    is_correct BOOLEAN,
    CONSTRAINT fk_choice_question
        FOREIGN KEY (question_id)
        REFERENCES question(question_id)
        ON DELETE CASCADE
);

CREATE TABLE quiz_result (
    quizresult_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    quiz_id INT NOT NULL,
    score INT NOT NULL,
    taken_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_result_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_result_quiz
        FOREIGN KEY (quiz_id)
        REFERENCES quiz(quiz_id)
        ON DELETE CASCADE
);
