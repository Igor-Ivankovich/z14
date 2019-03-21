from sqlalchemy import create_engine
from sqlalchemy.orm import mapper

engine = create_engine('postgresql://postgres:postgres@localhost:5432/db_z14')

from sqlalchemy import Column, Table, MetaData, Integer, String, ForeignKey

metadata = MetaData()

users_table = Table('users', metadata,
     Column('id', Integer, primary_key=True),
     Column('name', String),
     Column('fullname', String(length=100)),
     Column('password', String)
)

metadata.create_all(engine)


class User:
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (
        self.name, self.fullname, self.password)


mapper(User, users_table)

user = User("Bob", "Bobster", "qweasdzxc")

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()

session.add(user)

session.commit()


from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    text = Column(String(length=100))
    number = Column(Integer, unique=True)

    def __repr__(self):
        return f'<{self.id}, {self.text}, {self.number}>'


class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    text = Column(String(length=100))
    question = Column(ForeignKey(Question.id))

    def __repr__(self):
        return f'<{self.id}, {self.text}, {self.question}>'

Base.metadata.create_all(engine)

# question1 = Question(text='Text 1', number=1)
# question2 = Question(text='Text 2', number=2)

# session.add_all([question1, question2])
# session.commit()

# answer = Answer(text='A 1', question=1)
# session.add(answer)
# session.commit()

result = session.query(Question).with_entities(Question.text).all()
print(result)

session.query(Question).filter(Question.number == 1).update({'text': 'Text 1'})
session.commit()
result = session.query(Question).filter(Question.text.like('Text%')).all()
print(result)

result = session.query(Answer, Question).filter(Answer.id == 2).join(Question).first()
answer, question = result
print("ANSWER", answer)
print("QUESTION", question)
