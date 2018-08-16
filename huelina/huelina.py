# -*- coding: utf-8 -*- 
# TODO: Unite encodings for windows and linux
__version__ = 0.3
try:
    from question import Question
except:
    from huelina.question import Question
from colorama import Fore, init
from random import shuffle
from os import getcwd
from pathlib import Path

class quize():
    def __init__(self):
        self.questions = []
        self.mistakes = set() 
        
        print(Fore.CYAN) # Color background text in blue
        print(f"Добро пожаловать в Хуелина v{__version__}\n \
        \nВаш каталог: {getcwd()}\n \
        \nВведите имя файла с тестами (по умолчанию anat.txt) \
        \nИспользуйте файлы anatN-ansi.txt на windows и anatN-utf8 на других OS")

        file = Path(input())
        print(file)
        if file == '':
            file = "data/anat.txt"
        self.quize_file = file

        self.load_questions()
        self.start_and_end()
        self.ask_questions()

    def ask_questions(self):
        chosen = self.questions[self.start:self.ends]
        shuffle(chosen)
        for q in chosen:
            print(f"[{chosen.index(q) + 1}/{len(chosen)}]", end=" ")
            q.printq()
            no_mistakes = q.check(input())
            if not no_mistakes:
                self.mistakes.add(q)
            print("")

        while len(self.mistakes) != 0:

            print(f"Количество Ваших ошибок: {len(self.mistakes)}\n"
                "Сделать работу над ошибками? Введите 1 и нажмите Enter, чтобы выполнить "
                "\n(Другие цифры или буквы, или просто нажатие Enter выключат программу)")
            if input() == "1":
                pending_rem = set()
                i = 1
                for q in self.mistakes:
                    print(f"[{i}/{len(self.mistakes)}]", end=" ")
                    q.printq()
                    no_mistakes = q.check(input())
                    if no_mistakes:
                        pending_rem.add(q)
                    i += 1
                    print("")
                self.mistakes = self.mistakes - pending_rem
            else:
                self.mistakes.clear()

        
    def load_questions(self):
        """
        Parses file defined by filepath
        """
        try:
            with open(self.quize_file) as f:
                for line in f.readlines():
                    if line[0].isnumeric():
                        self.questions.append(Question(line))
                    elif line[0] == "*":
                        self.questions[-1].add_correct(line[2:len(line) - 1])
                    elif line[0] == "#":
                        pass
                    else:
                        self.questions[-1].add_incorrect(line[:len(line) - 1])
        except FileNotFoundError:
            print(f"{Fore.RED}Файл не существует! Файл по умолчанию - anat.txt{Fore.CYAN}")
            file="data/anat.txt"

    def start_and_end(self):
        #User specifies start and stop points
        print("\nВведите номер вопроса, с которого хотите начать (по умолчанию 1)")
        self.start = input()

        try:
            if self.start == '':
                self.start = 0
            else:
                self.start = int(self.start) - 1
        except ValueError:
            print(f"{Fore.RED}Неверный ввод, вы начнете с первого вопроса{Fore.CYAN}")
            self.start = 0

        print(f"Введите номер вопроса, которым хотите закончить (по умолчанию {len(self.questions)})")
        self.ends = input()

        try:
            if self.ends == '':
                self.ends = len(self.questions)
            elif int(self.ends) > len(self.questions) or int(self.ends) < self.start:
                print(f"{Fore.RED}Неверный ввод, вы закончите вопросом номер {len(self.questions)} {Fore.CYAN}")
                self.ends = len(self.questions)
            else:
                self.ends = int(self.ends)
        except ValueError:
            print(f"{Fore.RED}Неверный ввод, вы закончите вопросом номер {len(self.questions)} {Fore.CYAN}")
            self.ends = len(self.questions)

        print(f"Вопросы в выбранном Вами диапазоне перемешаны автоматически \
                    \n{Fore.RED}Вводите ответ как на ЕГЭ \
                    \n(цифры в любой последовательности, без дополнительных знаков){Fore.CYAN}\n")


if __name__ == "__main__":
    init()
    new_quize = quize()