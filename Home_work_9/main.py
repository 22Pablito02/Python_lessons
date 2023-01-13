
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
        "/delete - удалить сотрудника.")



def get_contact(update, context):
    import sys, os, csv
    lst = []
    with open(os.path.join(os.path.dirname(sys.argv[0]),"file.csv"),"r", encoding='utf-8') as r_file:
        file_read = csv.reader(r_file, delimiter=",")
        for row in file_read:
            lst.append(row)
   
    for i in range(0, len(lst)):
        temp = str(lst[i])    
        lool = ""
        for j in range(0, len(temp)):
            if temp[j] == "'" or temp[j] == "[" or temp[j] == "]": 
                lool += ""
            else:
                lool += temp[j]
        update.message.reply_text(lool)
    


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    
    entry_points = CommandHandler('start', start)
    
    show_handler = ConversationHandler(
        entry_points=[CommandHandler('show', get_contact)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, get_contact)]
        },
        fallbacks=[CommandHandler('stop', stop)]    
    )

    add_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, add)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    # delete_handler = ConversationHandler(
    #     entry_points=[CommandHandler('delete', delete)],
    #     states={
    #         1: [MessageHandler(Filters.text & ~Filters.command, delete)]
    #     },
    #     fallbacks=[CommandHandler('stop', stop)]
    # )

    
    entry_points = CommandHandler('start', start)
    dp.add_handler(entry_points)
    dp.add_handler(show_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()