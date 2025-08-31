import os
import time

import requests
from dotenv import load_dotenv

import telegram


def get_status(url, dev_token, timestamp=None):
    headers = {"Authorization": f'Token {dev_token}'}
    params = {}
    if timestamp:
        params['timestamp'] = timestamp

    response = requests.get(
        url,
        headers=headers,
        params=params, 
        timeout=10
    )
    response.raise_for_status()
    return response.json()


def send_message(bot, telegram_chat_id, url, dev_token, timestamp):
    status = get_status(url, dev_token, timestamp)
    if status and status['status'] == 'found':
        for attempt in status['new_attempts']:
            message = f'Преподаватель проверил работу "{attempt["lesson_title"]}"\n\n'
            if attempt['is_negative']:
                bot.send_message(
                    telegram_chat_id,
                    message +
                    'В работе найдены ошибки\n\n'
                    f'Ссылка на урок: {attempt["lesson_url"]}'
                )
            else:
                bot.send_message(
                    telegram_chat_id,
                    message +
                    f'Преподаватель проверил работу "{attempt["lesson_title"]}"\n\n'
                    'Работа принята!'
                )
                timestamp = attempt.get('timestamp')

        return status.get('last_attempt_timestamp')


def main():
    load_dotenv() 

    dev_token = os.environ['DEV_TOKEN']
    tg_token = os.environ['BOT_TOKEN']
    telegram_chat_id = os.environ['CHAT_ID']
    url = 'https://dvmn.org/api/long_polling/'
    bot = telegram.Bot(token=tg_token)

    timestamp = None    
    while True:
        try: 
            msg_timestamp = send_message(
                bot,
                telegram_chat_id,
                url,
                dev_token,
                timestamp
            )
            timestamp = msg_timestamp

        except requests.exceptions.ReadTimeout:
            pass

        except requests.exceptions.ConnectionError:
            print("Ошибка соединения, пробуем через 5 секунд...")
            time.sleep(5)


if __name__ == '__main__':
    main()
