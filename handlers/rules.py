from aiogram.types import Update
from telegram.ext import CallbackContext #я тут чуть у chatGPТ подсмотрел :)



FORBIDDEN_WORDS = ['bad_word1', 'bad_word2', 'bad_word3']

ADMIN_ID = 123456789 #просто для примера, я свой айди не знаю :)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот-админ. Я могу банить пользователей за использование запрещенных слов.')

def check_forbidden_words(update: Update, context: CallbackContext) -> None:
    message_text = update.message.text.lower()

    if any(word in message_text for word in FORBIDDEN_WORDS):
        user_id = update.message.from_user.id
        user_name = update.message.from_user.username

        # Проверяем, не является ли автор сообщения админом
        if user_id == ADMIN_ID:
            update.message.reply_text(f"Админ {user_name}, пожалуйста, избегайте использование запрещенных слов.")
        else:
            # Бан пользователя
            context.bot.kick_chat_member(update.message.chat_id, user_id)
            update.message.reply_text(f"Пользователь {user_name} забанен за использование запрещенных слов.")
