from datetime import datetime
import logging
import database_py
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def update(update, context):
    new = str(update.message.text).replace("/updateS ", "")
    print(new)
    database_py.insert(datetime.now(), new)
    update.message.reply_text(database_py.select())
    logger.warning(database_py.select())


def analyze(update, context):
    update.message.reply_text(database_py.select())
    logger.warning(database_py.select())


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)
    logger.warning(database_py.all())


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(
        "5028788079:AAHQj5uFxgDX12H80jSWrB6kG-dCHBBwuEE", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("updateS", update))
    dp.add_handler(CommandHandler("analyze", analyze))

    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
