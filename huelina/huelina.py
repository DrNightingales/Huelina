# -*- coding: utf-8 -*- 
# TODO: Unite encodings for windows and linux

from question import Question
from colorama import Fore, init
from random import shuffle
init()

#print(Style.BRIGHT) # Set style 
print(Fore.CYAN) # Color background text in blue

print("Добро пожаловать в Хуелина 0.2-альфа\n \
    \nВведите имя файла с тестами (по умолчанию anat.txt) \
    \nИспользуйте файлы anatN-ansi.txt на windows и anatN-utf8 на других OS")

file = input()

if file == '':
    file = "anat.txt"

questions = []
mistakes = set()


def load_questions(filepath):
    """
    Parses file defined by filepath
    """
    with open(filepath) as f:
        for line in f.readlines():
            if line[0].isnumeric():
                questions.append(Question(line))
            elif line[0] == "*":
                questions[-1].add_correct(line[2:len(line) - 1])
            elif line[0] == "#":
                pass
            else:
                questions[-1].add_incorrect(line[:len(line) - 1])

load_questions(file)


#User specifies start and stop points
print("\nВведите номер вопроса, с которого хотите начать (по умолчанию 1)")
start = input()

try:
    if start == '':
        start = 0
    else:
        start = int(start) - 1
except ValueError:
    print(f"{Fore.RED}Неверный ввод, вы начнете с первого вопроса{Fore.CYAN}")
    start = 0


print(f"Введите номер вопроса, которым хотите закончить (по умолчанию {len(questions)})")
ends = input()

try:
    if ends == '':
        ends = len(questions)
    elif int(ends) > len(questions) or int(ends) < start:
        print(f"{Fore.RED}Неверный ввод, вы закончите вопросом номер {len(questions)} {Fore.CYAN}")
        ends = len(questions)
    else:
        ends = int(ends)
except ValueError:
    print(f"{Fore.RED}Неверный ввод, вы закончите вопросом номер {len(questions)} {Fore.CYAN}")
    ends = len(questions)

print(f"Вопросы в выбранном Вами диапазоне перемешаны автоматически \
        \n{Fore.RED}Вводите ответ как на ЕГЭ \
        \n(цифры в любой последовательности, без дополнительных знаков){Fore.CYAN}\n")
chosen = questions[start:ends]
shuffle(chosen)
for q in chosen:
    print(f"[{chosen.index(q) + 1}/{len(chosen)}]", end=" ")
    q.printq()
    no_mistakes = q.check(input())
    if not no_mistakes:
        mistakes.add(q)
    print("")

while len(mistakes) != 0:

    print(f"Количество Ваших ошибок: {len(mistakes)}\n"
          "Сделать работу над ошибками? Введите 1 и нажмите Enter, чтобы выполнить "
          "\n(Другие цифры или буквы, или просто нажатие Enter выключат программу)")
    if input() == "1":
        pending_rem = set()
        i = 1
        for q in mistakes:
            print(f"[{i}/{len(mistakes)}]", end=" ")
            q.printq()
            no_mistakes = q.check(input())
            if no_mistakes:
                pending_rem.add(q)
            i += 1
            print("")
        mistakes = mistakes - pending_rem
    else:
        mistakes.clear()
