INSERT INTO users (username, email, password_hash, role)
VALUES
('student01', 'student01@gmail.com', 'hashed_password', 'student'),
('student02', 'student02@gmail.com', 'hashed_password', 'student'),
('student03', 'student03@gmail.com', 'hashed_password', 'student'),
('admin01',   'admin01@gmail.com',   'hashed_password', 'admin');
('admin02',   'admin02@gmail.com',   'hashed_password', 'admin');

INSERT INTO material (title, description, category, file_path) VALUES
('Introduction to Python',
 'Basic concepts of Python programming language',
 'Programming',
 '/uploads/python_intro.pdf'),

('HTML Basics',
 'Introduction to HTML tags and structure',
 'Web Development',
 '/uploads/html_basics.pdf'),

('CSS Fundamentals',
 'Styling and layout using CSS',
 'Web Development',
 '/uploads/css_fundamentals.pdf'),

('JavaScript Essentials',
 'Core JavaScript concepts for beginners',
 'Programming',
 '/uploads/javascript_essentials.pdf'),

('Database Fundamentals',
 'Overview of relational databases and tables',
 'Database',
 '/uploads/database_fundamentals.pdf'),

('SQL Basic Commands',
 'Common SQL queries such as SELECT and INSERT',
 'Database',
 '/uploads/sql_basic_commands.pdf'),

('Object-Oriented Programming',
 'Concepts of OOP including classes and inheritance',
 'Programming',
 '/uploads/oop_concepts.pdf'),

('Flask Framework Basics',
 'Introduction to Flask web framework',
 'Web Development',
 '/uploads/flask_basics.pdf'),

('Web Security Basics',
 'Understanding authentication and data security',
 'Cybersecurity',
 '/uploads/web_security_basics.pdf'),

('Software Engineering Principles',
 'Fundamentals of software development life cycle',
 'Software Engineering',
 '/uploads/software_engineering_principles.pdf');

INSERT INTO quiz_result (user_id, quiz_id, score, taken_at) VALUES
(1, 1, 8, '2025-12-18 09:00:00'),
(2, 2, 7, '2025-12-18 09:10:00'),
(3, 3, 9, '2025-12-18 09:20:00'),
(4, 4, 6, '2025-12-18 09:30:00'),
(5, 5, 8, '2025-12-18 09:40:00'),
(6, 6, 7, '2025-12-18 09:50:00'),
(7, 7, 9, '2025-12-18 10:00:00'),
(8, 8, 10, '2025-12-18 10:10:00'),
(9, 9, 6, '2025-12-18 10:20:00'),
(10, 10, 8, '2025-12-18 10:30:00');

INSERT INTO choice (question_id, choice_text, is_correct) VALUES
(1, 'func', FALSE),
(1, 'define', FALSE),
(1, 'def', TRUE),
(1, 'function', FALSE),
(2, 'Hyper Text Markup Language', TRUE),
(3, 'color', TRUE),
(4, '//', TRUE),
(5, 'Tables', TRUE),
(6, 'SELECT', TRUE),
(7, 'Inheritance', TRUE);

INSERT INTO question
(quiz_id, question_text, choice_a, choice_b, choice_c, choice_d, correct_answer)
VALUES
(1, 'Which keyword defines a function in Python?', 'func', 'define', 'def', 'function', 'C'),
(2, 'What does HTML stand for?', 'Hyper Tool ML', 'Hyper Text Markup Language', 'High Text Machine Language', 'Hyperlinks Text ML', 'B'),
(3, 'Which CSS property changes text color?', 'font-style', 'color', 'background', 'align', 'B'),
(4, 'Which symbol is used for comments in JavaScript?', '//', '/* */', '#', '<!-- -->', 'A'),
(5, 'What stores data in a database?', 'Tables', 'Forms', 'Reports', 'Queries', 'A'),
(6, 'Which SQL command retrieves data?', 'INSERT', 'DELETE', 'SELECT', 'UPDATE', 'C'),
(7, 'Which OOP principle allows reuse?', 'Encapsulation', 'Inheritance', 'Abstraction', 'Polymorphism', 'B'),
(8, 'Which function starts a Flask app?', 'app.run()', 'flask.start()', 'run.app()', 'start()', 'A'),
(9, 'What protects data over the internet?', 'HTTP', 'FTP', 'SSL/TLS', 'IP', 'C'),
(10, 'Which model is used in software development?', 'Waterfall', 'Spiral', 'Agile', 'All of the above', 'D');

INSERT INTO quiz (title, description) VALUES
('Python Basics', 'Introductory Python quiz'),
('HTML Fundamentals', 'Basic HTML concepts'),
('CSS Basics', 'Styling web pages'),
('JavaScript Intro', 'JS fundamentals'),
('Database Basics', 'Intro to databases'),
('SQL Commands', 'Basic SQL queries'),
('OOP Concepts', 'Object-oriented programming'),
('Flask Basics', 'Flask framework quiz'),
('Web Security', 'Basic security concepts'),
('Software Engineering', 'SE principles');
