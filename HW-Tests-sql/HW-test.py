import psycopg2
import sys


class TestException(Exception):
    pass


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(dsn='postgres://john:123'
                                               '@localhost:5432/wsx')
        self.cursor = self.connection.cursor()

    def query_name_test(self):
        self.cursor.execute("SELECT name_test, id FROM tests ;")
        return self.cursor.fetchall()

    def query_name_person(self):
        self.cursor.execute("SELECT name_person, name_test FROM persons"
                            " JOIN tests ON persons.tests_id = tests.id;")
        return self.cursor.fetchall()

    def query_question(self, test_id):
        self.cursor.execute(f"SELECT question, id FROM questions WHERE"
                            f" tests_id = '{test_id}';")
        return self.cursor.fetchall()

    def query_answer(self, i):
        self.cursor.execute(f"SELECT answer FROM answers WHERE"
                            f" questions_id = '{i}';")
        return self.cursor.fetchall()

    def query_output_date(self, answers, test, input_name_person):
        print()
        self.cursor.execute(
            f"SELECT persons.id,tests.id,questions.id,answers.id FROM"
            f" tests JOIN persons ON persons.tests_id = tests.id JOIN "
            f"questions ON questions.tests_id = tests.id JOIN answers"
            f" ON answers.questions_id = questions.id WHERE tests.id = {test}"
            f" AND answers.answer  IN {answers}"
            f" AND persons.name_person = '{input_name_person}';")
        return self.cursor.fetchall()

    def query_enter_name_test(self, test, name_person):
        self.cursor.execute(f"""
                               INSERT INTO persons (name_person,tests_id)
                               VALUES ('{name_person}','{test}');
                                """)

    def query_enter_answer_in_database(self, answers):
        self.cursor.execute(f"""
                    INSERT INTO answers_persons (persons_id, tests_id,questions_id,answers_id,answer_person)
                    VALUES {','.join(answers)};
                      """)

    def commit(self):
        return self.connection.commit()

    def close(self):
        return self.connection.close()


class Test(Database):
    @staticmethod
    def _validate(test, person):
        if not test:
            raise TestException('Test not found')
        if person:
            raise TestException(f'{person[0][0]} has already completed'
                                f' this test: {test[0][0]}')

    def checking_data_in_database(self, name_test, name_person):
        test = [i for i in self.query_name_test() if i[0] == name_test]
        person = [i for i in self.query_name_person()
                  if i[0] == name_person and i[1] == name_test]
        self._validate(test, person)
        return test[0][1]

    def start_test(self, test_id, name_person):
        answers = []
        for i in self.query_question(test_id):
            print('Question:= ', i[0])
            for j in self.query_answer(i[1]):
                print('Answer:= ', j[0])
            answer = input('Answer:= ')
            answers.append(answer)
        n = len(answers)
        if n != 1:
            answer = tuple(answers)
        else:
            answer = f"('{answers[0]}')"
        output = [str(self.query_output_date(answer, test_id, name_person)[i]
                  + (answers[i], )) for i in range(n)]
        return output


def main(argv):
    test = Test()
    argv = argv[1:3]
    print(len(argv))
    if not argv:
        raise Exception("Bad arguments")
    input_name_person, input_name_test = (argv[0], argv[1])
    test_id = test.checking_data_in_database(input_name_test, input_name_person)
    test.query_enter_name_test(test_id, input_name_person)
    answer = test.start_test(test_id, input_name_person)
    test.query_enter_answer_in_database(answer)
    test.commit()
    test.close()


if __name__ == '__main__':
    main(sys.argv)
