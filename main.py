import requests
import os

API_URL = 'https://ru.wikipedia.org/w/api.php'

def search_query_id(query,):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36'
    }
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srsearch': query,
        'srlimit': 1
    }
    response = requests.get(API_URL, params=params, headers=headers, timeout=(5, 10))
    query_result = response.json()
    query_id = query_result['query']['search'][0]['pageid']
    return query_id



def search_info(query_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36'
    }
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'extracts',
        'pageids': query_id,
        'explaintext': True
    }  
    
    info = requests.get(API_URL, params=params, headers=headers).json()
    text = info['query']['pages'][str(query_id)]['extract']
    return text
    

def main():
    print('WikiApp')
    try:
        while True:
            try:
                action = input('1. Начать поиск\n2. Выйти\n> ')
                if action == '1':
                    query = input('Что хотите найти?: ').split()
                    os.system('cls')
                    id = search_query_id(query)
                    text = search_info(id)
                    print(f'\n{text}\n')
                elif action == '2':
                    os.system('cls')
                    break
            except requests.exceptions.ConnectionError:
                print('Ошибка соединения')
            except requests.exceptions.Timeout:
                print('Время ожидания вышло')
            except requests.exceptions.RequestException as e:
                print(e)
            except Exception:
                print('Ответ не найден')
    except KeyboardInterrupt:
        print('Работа программы была завершена досрочно')
    
    
main()