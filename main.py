import random
import json

from request_for_api_quiz import get_questions_from_api
from firebase_connect import connect_to_database

# читаем вопросы из json
def get_questions():
    questions = {}
    with open("questions.json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file)
        for answ in data:
            questions[answ['question']] = answ['answers']
    return questions

# цикл игры 
def start_game(): 
    questions = get_questions()
    while len(questions) != 0:
        global score
        current_question = random.choice(list(questions))
        correct_answer = questions[current_question][0]
        options_answer = questions[current_question]
        random.shuffle(options_answer)
        print(current_question)
        print("Возмжные варианты ответов:\n")
        print("\n".join(options_answer))
        answer = input("\n")
        if answer == correct_answer:
            score += 1
            print(f"ОТВЕТ ВЕРНЫЙ! ВАШ ТЕКУЩИЙ СЧЁТ: {score}")
        else:
            print(f"ОТВЕТ НЕВЕРНЫЙ! ВАШ ТЕКУЩИЙ СЧЁТ: {score}")
            print(f"Правильный ответ: {correct_answer}")
        del questions[current_question]

    print(f"ВИКТОРИНА ЗАВЕРШЕНА! ВАШ ТЕКУЩИЙ СЧЁТ: {score}")


def check_player_score():
    if user_name not in players:  #если пользователь новый, то записываем его имя и счёт в players
        players[user_name] = score
    elif score > int(players[user_name]): #если игрок побил свой рекорд, то перезаписываем его счёт
        players[user_name] = score


def get_leaders():
    new_list_items = [(score, name) for name, score in players.items()]

    print('Таблица лидеров:') #Выводим таблицу лидеров
    place_number = 1
    for score_item, name_item in sorted(new_list_items, reverse=True):
        if place_number < 8:
            print(f'{place_number}. {name_item} - {score_item}')
            place_number += 1
    db.set(players)


def main(): 
    get_questions_from_api()
    start_game()
    check_player_score()     
    get_leaders()

if __name__ == "__main__":


    db = connect_to_database()

    #Записывам наших игроков и их счёт в словарь 
    players = db.get()

    #Получаем имя текущего игрока
    user_name = input("Введите ваше имя: ")


    score = 0


    main()