from question import Question
import bgcolors as bg
import re
from random import shuffle

print(bg.OKBLUE)  # Color background text in blue
print("Добро пожаловать в Хуелина 0.2-альфа")
print("")
print("Введите имя файла с тестами (по умолчанию anat.txt)")
file = input()
print("")

if file == '':
    file = "anat.txt"

questions = []
mistakes = set()


def load_questions(filepath):
    q_pattern = r"\d"
    c_pattern = r"\*"
    h_pattern = r"\#"

    with open(filepath) as f:
        for line in f.readlines():
            if re.match(q_pattern, line) != None:
                questions.append(Question(line))
            elif re.match(c_pattern, line) != None:
                questions[-1].add_correct(line[2:len(line) - 1])
            elif re.match(h_pattern, line) != None:
                pass
            else:
                questions[-1].add_incorrect(line[:len(line) - 1])


load_questions(file)

print("Введите номер вопроса, с которого хотите начать (по умолчанию 1)")
start = input()
try:
    if start == '':
        start = 0
    else:
        start = int(start) - 1
except ValueError:
    print("{}Неверный ввод, вы начнете с первого вопроса{}".format(bg.FAIL, bg.OKBLUE))
    start = 0

print("Введите номер вопроса, которым хотите закончить (по умолчанию {})".format(len(questions)))
ends = input()
try:
    if ends == '':
        ends = len(questions)
    elif int(ends) > len(questions) or int(ends) < start:
        print("{}Неверный ввод, вы закончите вопросом номер {} {}"
              "".format(bg.FAIL, len(questions), bg.OKBLUE))
        ends = len(questions)
    else:
        ends = int(ends)
except ValueError:
    print("{}Неверный ввод, вы закончите вопросом номер {} {}"
          "".format(bg.FAIL, len(questions), bg.OKBLUE))
    ends = len(questions)

print("Вопросы в выбранном Вами диапазоне перемешаны автоматически")
print(bg.FAIL + "Вводите ответ как на ЕГЭ "
                "(цифры в любой последовательности, без дополнительных знаков)")
print(bg.OKBLUE)  # Color background text in blue
print()
chosen = questions[start:ends]
shuffle(chosen)
for q in chosen:
    print("[{}/{}]".format(chosen.index(q) + 1, len(chosen)), end=" ")
    q.printq()
    no_mistakes = q.check(input())
    if not no_mistakes:
        mistakes.add(q)
    print("")

while len(mistakes) != 0:

    print("Количество Ваших ошибок: {}\n"
          "Сделать работу над ошибками? Введите 1 и нажмите Enter, чтобы выполнить "
          "\n(Другие цифры или буквы, или просто нажатие Enter выключат программу)".format(len(mistakes)))
    if input() == "1":
        pending_rem = set()
        i = 1
        for q in mistakes:
            print("[{}/{}]".format(i, len(mistakes)), end=" ")
            q.printq()
            no_mistakes = q.check(input())
            if no_mistakes:
                pending_rem.add(q)
            i += 1
            print("")
        mistakes = mistakes - pending_rem
    else:
        mistakes.clear()
