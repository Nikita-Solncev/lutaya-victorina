import requests
import json

def get_questions_from_api() -> None:
    """
    Функция обращаеться к сайту lifeis.porn по апи и записывает полученные вопросы в questions.json
    """

    #Выбираем сложность вопроса
    print('Выберите сложность от 1 до 4:\n"1" для получения лёгкого/шуточного вопроса.\n"2" для получения вопроса средней сложности.\n"3" для получения сложного вопроса.\n"4" для получения детского вопроса.')
    while True:
        mode = input()
        try:
            if int(mode) > 4 or int(mode) < 1:
                print("Значение сложности неверно")
            else:
                break
        except ValueError:
            print("Значение сложности неверно")

    #Записываем в виде словаря в response ответ от сайта
    response = requests.get(f'https://engine.lifeis.porn/api/millionaire.php?qType={mode}&count=5').json()

    #Записываем вопросы в questions.json
    with open('questions.json', "w", encoding='utf-8') as json_file:
        answ_list = []
        for answ in response['data']:
            answ = {
                'answers': answ['answers'],
                'question': answ['question'].replace("\u2063", "")
            }
            answ_list.append(answ)
        json.dump(answ_list, json_file, ensure_ascii=False, indent=4)