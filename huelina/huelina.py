# -*- coding: utf-8 -*- 
# TODO: Unite encodings for windows and linux
__version__ = 0.6

# Try-except block for the script to be used both as package as executable script
try:
    from question import Question
except:
    from huelina.question import Question
from colorama import Fore, init

from random import shuffle
import os 
from pathlib import Path
script_path = Path(os.path.realpath(__file__)).parent
data_path = script_path / "data"


class Quiz():
    def __init__(self):
        self.questions = []
        self.mistakes = set() 
        
        print(Fore.CYAN) # Color background text in blue
        print(f"Добро пожаловать в Хуелина v{__version__}\n")

        self.select_file()
        self.load_questions()
        self.start_and_end()
        print("Чтобы перемешать вопросы введите 1, другой ввод оставит вопросы в изначальном порядке")
        self.ask_questions(True if input() == "1" else False)
    
    def select_file(self):
        """
        Writes path of the file chosen by user to self.quiz
        """
        if not data_path.is_dir():
            print(f"{Fore.RED}Внимание! Папка data/ не обнаружена")
            raise FileNotFoundError

        anats = sorted([file for file in data_path.glob("*.txt")])
        print("Введите номер файла из списка\n"
              "Добавьте файл в папку data/ и перезапустите программу, если не можете найти нужный")

        for i, file in enumerate(anats):
            print(f"{i+1}. {file.name}")

        correct_input = False
        while not correct_input:
            try:
                anat_n = int(input())
                self.quiz_file = anats[anat_n-1]
                correct_input = True
            except ValueError:
                print(f"{Fore.RED}Неверный ввод, введите число из списка{Fore.CYAN}")
            except IndexError:
                print(f"{Fore.RED}Неверный ввод, введите число из списка{Fore.CYAN}")

    def ask_questions(self, shuffled=False):
        """
        Starts quiz, with mistakes correction
        shuffled - let's the user to decide either to shuffle quetsions or not
        """
        print(f"{Fore.RED}Вводите ответ как на ЕГЭ\n(Цифры, без доп. символов, в любом порядке){Fore.CYAN}")

        chosen = self.questions[self.start:self.ends]
        if shuffled:
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
        Parses and loads question to self.questions
        """
        try:
            with open(self.quiz_file,"r", encoding="utf-8", newline="") as f:
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
        """
        Asks user for the question to start from and the question to end with
        """
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


def run():
    init()
    Quiz()


if __name__ == "__main__":
    run()