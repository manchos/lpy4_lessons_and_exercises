


if __name__ == '__main__':
    print("""\n1.
Написать функцию, которая принимает на вход две строки.
Если строки одинаковые, возвращает 1.
Если строки разные и первая длиннее, возвращает 2.
Если строки разные и вторая строка 'learn', возвращает 3.
        """)

    def compare(str1, str2):
        if str1 == str2:
            return 1
        else:
            if len(str1) > len(str2) and str2 != "learn":
                return 2
            if str2 == "learn":
                return 3

    print("compare('вася','вася') return : %s" % compare('вася','вася'))
    print("compare('вася222','вася') return : %s" % compare('вася222', 'вася'))
    print("compare('вася222','learn') return : %s" % compare('вася222', 'learn'))

    print("""\n2.
Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.
    """)
    class_scores = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '4b', 'scores': [4,3,3,5,2]},
                    {'school_class': '4b', 'scores': [4,4,3,3,3]}]

    scores_list = [x for x in class_scores for x in x['scores']]

    print('Cредний балл по всей школе: %s' % (sum(scores_list) / len(scores_list)))
    print('\nСредний балл по каждому классу:')
    print('класс : средний балл')

    for cl in class_scores:
        print("%s : %s" % (cl['school_class'], (sum(cl['scores']) / len(cl['scores']))))

    print("""\n3.
Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] пока не встретите имя "Валера".
Когда найдете напишите "Валера нашелся". Подсказка: используйте метод list.pop()
Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.
    """)
    name_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]


    def find_person(name, list_name):
        while True:
            if name_list.pop() == "Валера":
                print("Валера нашелся")
                break
            if (len(name_list) == 0):
                print("Валера не нашелся")
                break

    find_person("Валера", name_list)

    print("""\n3.
Написать функцию ask_user() чтобы помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”
При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”
        """)

    from les_1_answer import get_answer, ask_user

    answers = {
        "привет": "Привет!",
        "как дела": "Отлично, а у тебя?",
        "Пока!": "Еще увидимся!",
        "Хорошо": "Молодца!"
    }

    ask_user(answers)