from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy import UniqueConstraint

engine = create_engine('postgres://john:123@localhost:5432/qwerty')

Base = declarative_base()


class Tests(Base):
    __tablename__ = 'tests'
    id = Column(Integer, primary_key=True)
    name_test = Column(String(length=100), unique=True)


class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    test_id = Column(ForeignKey(Tests.id))
    question = Column(String(length=100))
    __table_args__ = (UniqueConstraint(test_id, question),)


class Answers(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    question_id = Column(ForeignKey(Questions.id))
    answer = Column(String(length=100))
    true_answer = Column(Boolean)
    __table_args__ = (UniqueConstraint(question_id, answer),)


class Persons(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name_person = Column(String(length=100))
    test_id = Column(ForeignKey(Tests.id))
    __table_args__ = (UniqueConstraint(name_person, test_id),)


class AnswersPersons(Base):
    __tablename__ = 'answers_person'
    id = Column(Integer, primary_key=True)
    person_id = Column(ForeignKey(Persons.id))
    test_id = Column(ForeignKey(Tests.id))
    questions_id = Column(ForeignKey(Questions.id))
    answers_id = Column(ForeignKey(Answers.id))
    answer_person = Column(String(length=100))
    __table_args__ = (UniqueConstraint(person_id, test_id, questions_id, answers_id),)


Base.metadata.create_all(engine)
