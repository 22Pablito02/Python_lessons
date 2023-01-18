#  env\Scripts\activate.ps1

import model
import logging
from tkn import token 
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
TOKEN = token


def start(update, context):
    update.message.reply_text(
        "/start"
        "Привет. Пройдите небольшой опрос, пожалуйста!\n"
        "Вы можете прервать диалог, послав команду /stop.\n"
        "/show - показать всех сотрудников;\n"
        "/add - добавить сотрудника;\n"
        "/delete - удалить сотрудника;\n"
        "/update - обновить данные сотрудника;\n"
        "/find - поиск контакта.")


def add (update, context):
    update.message.reply_text("Введите Имя, Фамилию, Номер и Должность через пробел")
    return 1


def delete (update, context):
    update.message.reply_text("Введите номер строки контакта, кого хотите удалить")
    return 1


def update (update, context):
    update.message.reply_text(
    "Введите номер строки контакта, а также:\n"
    "Имя, Фамилию, Номер и Должность через пробел")
    return 1


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def find(update, context):
    update.message.reply_text("Введите имя искомого контакта")
    return 1

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    
    entry_points = CommandHandler('start', start)
    
    show_handler = ConversationHandler(
        entry_points=[CommandHandler('show', model.get_contact)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, model.get_contact)]
        },
        fallbacks=[CommandHandler('stop', stop)]    
    )

    add_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, model.create_employee)]
        }, 
        fallbacks=[CommandHandler('stop', stop)]
    )

    delete_handler = ConversationHandler(
        entry_points=[CommandHandler('delete', delete)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, model.delete_employee)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    update_handler = ConversationHandler(
        entry_points=[CommandHandler('update', update)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, model.update_employee)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    find_handler = ConversationHandler(
        entry_points=[CommandHandler('find', find)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, model.find_contact)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    
    entry_points = CommandHandler('start', start)
    dp.add_handler(entry_points)
    dp.add_handler(show_handler)
    dp.add_handler(add_handler)
    dp.add_handler(delete_handler)
    dp.add_handler(update_handler)
    dp.add_handler(find_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
