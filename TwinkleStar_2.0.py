import csv
import logging

from telegram.ext import Updater, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
database = {}

# Reading from *.csv file to the dataBase
with open('database.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        database[row[0]] = row[1]


# Find a keyword in the dataBase
def find_keyword(update, context):
    if update.message.chat.id == -1001679650861:
        if update.message.text in database:
            context.bot.send_message(chat_id=update.effective_chat.id, text=database.get(update.message.text))


# Error block
def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


# Main function, start bot
def main():
    updater = Updater("5092374817:AAG-YUsEhPp0SRj3acSwTQuOlw5kGO-4OSg")  # Bot's token
    dp = updater.dispatcher

    find_keyword_handler = MessageHandler(Filters.text & (~Filters.command), find_keyword)  # Catching the keyword
    dp.add_handler(find_keyword_handler)
    dp.add_error_handler(error)

    updater.start_polling()  # Start bot
    print("Started successfully")  # Just message
    updater.idle()  # Stop the bot with ctrl+c or process killing


if __name__ == '__main__':
    main()
