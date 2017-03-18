


if __name__ == '__main__':

    class_scores = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '4b', 'scores': [4,3,3,5,2]},
                    {'school_class': '4b', 'scores': [4,4,3,3,3]}]

    print("""\n1.
Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.
    """)

    scores_list = [x for x in class_scores for x in x['scores']]

    print('Cредний балл по всей школе: %s' % (sum(scores_list) / len(scores_list)))
    print('\nСредний балл по каждому классу:')
    print('класс : средний балл')

    for cl in class_scores:
        print("%s : %s" % (cl['school_class'], (sum(cl['scores']) / len(cl['scores']))))