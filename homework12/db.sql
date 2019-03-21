CREATE DATABASE testing;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username  VARCHAR (100) UNIQUE,
  password VARCHAR (100)
);

CREATE TABLE tests (
  id SERIAL PRIMARY KEY,
  name VARCHAR (100)
);

CREATE TABLE questions (
  id SERIAL PRIMARY KEY,
  text VARCHAR (100)
);

CREATE TABLE tests_questions (
  test_id INTEGER REFERENCES tests(id),
  question_id INTEGER REFERENCES questions(id)
);

CREATE TABLE answers (
  id SERIAL PRIMARY KEY,
  text VARCHAR (100),
  question_id INTEGER REFERENCES questions(id),
  correct BOOLEAN
);

CREATE TABLE users_answers (
  user_id INTEGER REFERENCES users(id),
  test_id INTEGER REFERENCES tests(id),
  question_id INTEGER REFERENCES questions(id),
  answer_id INTEGER REFERENCES answers(id),
  UNIQUE (user_id, test_id, question_id)
);


SELECT tests.name, questions.text, answers.text FROM tests_questions
  JOIN tests ON tests.id=tests_questions.test_id
  JOIN questions ON questions.id=tests_questions.question_id
  JOIN answers ON questions.id = answers.question_id
;