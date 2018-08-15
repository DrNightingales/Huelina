# -*- coding: utf-8 -*- 
from collections import defaultdict
from random import shuffle
from colorama import Fore



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
            print(f"{Fore.WHITE}{self.__rnd_answers.index(a) + 1}. {a}{Fore.CYAN}")

    def check(self, user_answer):
        no_mistakes = True
        try:
            answers_indexes = [int(answ) - 1 for answ in user_answer]
            answers = [self.__rnd_answers[i] for i in answers_indexes]

            for a in self.__rnd_answers:
                if not self.__answers[a] and a not in answers:
                    print(f"{Fore.WHITE}{self.__rnd_answers.index(a) + 1}. {a}{Fore.CYAN}")
                elif not self.__answers[a] and a in answers:
                    print(f"{Fore.RED}{self.__rnd_answers.index(a) + 1}. {a} \
(Вы отметили неправильный ответ){Fore.CYAN}")
                    no_mistakes = False
                elif self.__answers[a] and a in answers:
                    print(f"{Fore.GREEN}{self.__rnd_answers.index(a) + 1}. {a}{Fore.CYAN}")
                else:
                    print(f"{Fore.GREEN}{self.__rnd_answers.index(a) + 1}. {a}{Fore.RED} \
(Вы не отметили правильный ответ){Fore.CYAN}")
                    no_mistakes = False

        except IndexError:
            print(Fore.RED + "Этого ответа нет в списке" + Fore.CYAN)
            return False

        except ValueError:
            print(Fore.RED + "Пожалуйста, вводите только цифры" + Fore.CYAN)
            return False
        return no_mistakes
