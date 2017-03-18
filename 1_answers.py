answers = {
    "привет": "Привет!",
    "как дела": "Отлично, а у тебя?",
    "пока": "Еще увидимся!"
}


def get_answer(question, answers):
    return answers.get(question)


def ask_user(answers):
    # TODO Переписать функцию ask_user(), добавив обработку exception-ов. Добавить перехват ctrl+C и прощание
    while True:
        try:
            user_input = input("Скажи что-нибудь: ")
            answer = get_answer(user_input, answers)
            print(answer)

            if user_input == 'пока':
                break

        except (KeyboardInterrupt):
            print('Как жаль, что вы уже уходите...')
            break





ask_user(answers)