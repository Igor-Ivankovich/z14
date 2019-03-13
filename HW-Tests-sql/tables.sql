CREATE TABLE tests (
  id SERIAL PRIMARY KEY ,
  name_test VARCHAR(100) UNIQUE
);

CREATE TABLE questions (
  id SERIAL PRIMARY KEY ,
  tests_id INTEGER REFERENCES tests(id),
  question VARCHAR(100),
  UNIQUE (tests_id, question)
);

CREATE TABLE answers (
  id SERIAL PRIMARY KEY,
  questions_id INTEGER REFERENCES questions(id),
  answer VARCHAR(100),
  true_answer bool,
  UNIQUE (questions_id, answer)
);

CREATE TABLE persons (
  id SERIAL PRIMARY KEY,
  name_person VARCHAR(100),
  tests_id INTEGER REFERENCES tests(id),
  UNIQUE (name_person, tests_id)
);

CREATE TABLE answers_persons (
  id SERIAL PRIMARY KEY,
  persons_id INTEGER REFERENCES persons(id),
  tests_id INTEGER REFERENCES tests(id),
  questions_id INTEGER REFERENCES questions(id),
  answers_id INTEGER REFERENCES answers(id),
  answer_person VARCHAR (100),
  UNIQUE (persons_id, tests_id,questions_id,answers_id,answer_person)
);

