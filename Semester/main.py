import logging
import random
import requests
from bs4 import BeautifulSoup
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# Импортируем словарь urls из файла img_character.py
from img_character import urls
from config import TOKEN

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

reply_keyboard = [['/character', '/scrape', '/log', '/help']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def log_user_interaction(user_id, message):
    filename = f"{user_id}.log"
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(message + '\n')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    log_user_interaction(user.id, f"User {user.id} started the bot.")
    await update.message.reply_text(
        "Привет! Я бот, который показывает информацию из Star Wars и выполняет различные команды.",
        reply_markup=markup
    )



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    log_user_interaction(user.id, f"User {user.id} requested help.")
    await update.message.reply_text(
        "Вот доступные команды:\n/character - Показать случайного персонажа\n/scrape - Показать последние цитаты\n/log - Показать лог\n/help - Помощь")


async def character_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    character_id = random.randint(1, 20)
    response = requests.get(f'https://swapi.dev/api/people/{character_id}/')

    if response.status_code != 200:
        log_user_interaction(user.id,
                             f"User {user.id} requested character info but API request failed with status {response.status_code}.")
        await update.message.reply_text(
            f"Произошла ошибка при получении данных от API. Код ошибки: {response.status_code}")
        return

    character_data = response.json()

    required_keys = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year']
    if not all(key in character_data for key in required_keys):
        log_user_interaction(user.id,
                             f"User {user.id} requested character info but response data is incomplete: {character_data}")
        await update.message.reply_text(
            "Произошла ошибка при обработке данных от API. Ответ не содержит необходимой информации.")
        return

    character_info = (
        f"Имя: {character_data['name']}\n"
        f"Рост: {character_data['height']}\n"
        f"Вес: {character_data['mass']}\n"
        f"Цвет волос: {character_data['hair_color']}\n"
        f"Цвет кожи: {character_data['skin_color']}\n"
        f"Цвет глаз: {character_data['eye_color']}\n"
        f"Год рождения: {character_data['birth_year']}\n"
    )

    image_url = urls.get(str(character_id), "URL изображения не найден")

    log_user_interaction(user.id, f"User {user.id} requested character info: {character_info.strip()}")

    await update.message.reply_photo(photo=image_url, caption=character_info)

async def scrape_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    url = 'http://quotes.toscrape.com/'
    response = requests.get(url)

    if response.status_code != 200:
        log_user_interaction(user.id,
                             f"User {user.id} attempted to scrape data but request failed with status {response.status_code}.")
        await update.message.reply_text(f"Произошла ошибка при скрапинге данных. Код ошибки: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.select('.quote')

    if not quotes:
        log_user_interaction(user.id, f"User {user.id} attempted to scrape data but no quotes were found.")
        await update.message.reply_text("Не удалось найти цитаты на странице.")
        return

    next_quote_index = context.user_data.get('next_quote_index', 0)
    if next_quote_index >= len(quotes):
        await update.message.reply_text("There are no more quotes.")
        return

    quote = quotes[next_quote_index].select_one('.text').get_text().strip()
    next_quote_index += 1
    context.user_data['next_quote_index'] = next_quote_index

    log_user_interaction(user.id, f"User {user.id} scraped quote: {quote}")
    await update.message.reply_text(quote)



async def log_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    log_file_path = f"{user.id}.log"

    try:
        with open(log_file_path, "r") as file:
            # Получаем текущую позицию из контекста пользователя или устанавливаем 0, если позиция не определена
            current_position = context.user_data.get('log_position', 0)

            # Считываем строки из лога, начиная с текущей позиции и выводим следующие 10 строк
            lines = file.readlines()[current_position:]
            next_lines = lines[:10]

            # Обновляем текущую позицию в контексте пользователя
            context.user_data['log_position'] = current_position + len(next_lines)

            log_contents = "".join(next_lines)

            await update.message.reply_text(f"Лог для пользователя {user.id}:\n\n{log_contents}")

    except FileNotFoundError:
        await update.message.reply_text("Лог для этого пользователя не найден.")



def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('character', character_command))
    application.add_handler(CommandHandler('scrape', scrape_command))
    application.add_handler(CommandHandler('log', log_command))

    application.run_polling()


if __name__ == '__main__':
    main()
