# Devman Bot - Уведомления о проверке работ

Бот для Telegram, который автоматически опрашивает API Devman на наличие новых результатов проверки и отправляет уведомлений в Telegram-чат:
- Работа принята.
- В работе найдены ошибки.

## Предварительные требования

- Python 3.7+
- Аккаунт на [dvmn.org](https://dvmn.org/)
- Telegram аккаунт и бот (создается через [@BotFather](https://t.me/BotFather))

## Установка и настройка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv env
env\Scripts\activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Настройка переменных окружения

Создайте файл `.env` в корневой директории проекта

Добавьте следующие переменные:
```env
DEV_TOKEN=5a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
BOT_TOKEN=123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ
CHAT_ID=987654321
```

### Получение токенов

- Токен `Devman API`
1. Зайдите в личный кабинет на [dvmn.org](https://dvmn.org/)
2. Перейдите к документации [API Devman](https://dvmn.org/api/docs)
3. Скопируйте ваш API-токен

- Токен `Telegram бота`
1. Напишите [@BotFather](https://t.me/BotFather) в Telegram
2. Используйте команду `/newbot` для создания нового бота
3. Следуйте инструкциям для создания нового бота
4. Скопируйте выданный токен

- Чтобы получить свой `chat_id`, напишите в Telegram специальному боту: [@userinfobot](https://telegram.me/userinfobot)

## Запуск

После выполнения всех шагов настройки запустите бота в командной строке:
```bash
python main.py
```
Если не указан `CHAT_ID` в `.env`, бот запросит его при запуске:
```bash
python main.py
Введите свой ID: <telegram_chat_id>
```