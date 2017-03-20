


def get_answer(question, answers):
    return answers.get(question)


def ask_user(answers):
    # TODO Переписать функцию ask_user(), добавив обработку exception-ов. Добавить перехват ctrl+C и прощание
    while True:
        try:
            user_input = input("Как дела? :")
            answer = get_answer(user_input, answers)
            print(answer)

            if user_input == 'Хорошо':
                break

            if user_input == 'Пока!':
                break


        except (KeyboardInterrupt):
            print('Как жаль, что вы уже уходите...')
            break



if __name__ == '__main__':
    answers = {
        "привет": "Привет!",
        "как дела": "Отлично, а у тебя?",
        "Пока!": "Еще увидимся!",
        "Хорошо": "Молодца!"
    }
    ask_user(answers)