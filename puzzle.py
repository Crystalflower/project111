import random

number = random.randint(1, 100)

print("Загадайте число от 1 до 100, а я его угадаю. Если я буду выдавать число меньше загаданного, прошу отправить в ответ <, и наоборот >, при верном ответе =.")

answer = None
answers_less = []
answers_more = []
while True:
    answer = input("Это {}?".format(number))
    if answer == ">" :
        answers_more.append(number)
        if len(answers_less) == 0:
            number = random.randint(number + 1, 100)
    elif answer == "<" :
        answers_less.append(number)
        if len(answers_more) == 0:
            number = random.randint(1, number - 1)
    else:
        print("Я угадал!")
        break

    if len(answers_less) != 0 and len(answers_more) != 0:
        number = random.randint(int(max(answers_more)) + 1, int(min(answers_less)) - 1)
