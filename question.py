from collections import defaultdict
from random import shuffle
import bgcolors as bgc


class Question:

    def __init__(self, question):
        self.__answers = defaultdict()
        self._question = question
        self.__rnd_answers = []

    @property
    def question(self):
        return self._question

    def add_correct(self, correct_line):
        self.__answers[correct_line] = True

    def add_incorrect(self, incorrect_line):
        self.__answers[incorrect_line] = False

    def printq(self):
        print(self._question)
        self.__rnd_answers = [k for k in self.__answers.keys()]
        shuffle(self.__rnd_answers)
        for a in self.__rnd_answers:
            print("{}{}. {}{}".format(
                bgc.WHITE,
                self.__rnd_answers.index(a) + 1,
                a,
                bgc.OKBLUE))

    def check(self, user_answer):
        no_mistakes = True
        try:
            answers_indexes = [int(answ) - 1 for answ in user_answer]
            answers = [self.__rnd_answers[i] for i in answers_indexes]

            for a in self.__rnd_answers:
                if not self.__answers[a] and a not in answers:
                    print("{}{}. {}{}".format(
                        bgc.WHITE,
                        self.__rnd_answers.index(a) + 1,
                        a,
                        bgc.OKBLUE))
                elif not self.__answers[a] and a in answers:
                    print("{}{}. {} {}{}".format(
                        bgc.FAIL,
                        self.__rnd_answers.index(a) + 1,
                        a,
                        "(Вы отметили неправильный ответ)",
                        bgc.OKBLUE))
                    no_mistakes = False
                elif self.__answers[a] and a in answers:
                    print("{}{}. {}{}".format(
                        bgc.OKGREEN,
                        self.__rnd_answers.index(a) + 1,
                        a,
                        bgc.OKBLUE))
                else:
                    print("{}{}. {}{} {}{}".format(
                        bgc.OKGREEN,
                        self.__rnd_answers.index(a) + 1,
                        a,
                        bgc.FAIL,
                        "(Вы не отметили правильный ответ)",
                        bgc.OKBLUE))
                    no_mistakes = False

        except IndexError:
            print(bgc.FAIL + "Этого ответа нет в списке" + bgc.OKBLUE)
            return False

        except ValueError:
            print(bgc.FAIL + "Пожалуйста вводите только цифры" + bgc.OKBLUE)
            return False
        return no_mistakes
