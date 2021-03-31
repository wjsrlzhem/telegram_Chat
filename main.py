from telegram.ext import Updater, MessageHandler, Filters,CallbackContext


updater = Updater(token='1445163243:AAH2-Ucch4veOAuEf02p7iurWFvgaAbhK3c')
dispatcher = updater.dispatcher
updater.start_polling()


def handler(update:Updater, context:CallbackContext):
    text = update.message.text
    chat_id = update.message.chat_id

    if '야' in text:
        context.bot.send_message(chat_id=chat_id, text='?')
    elif '뭐하는데' in text:
        context.bot.send_message(chat_id=chat_id, text='누워있는데')
    elif '피시' in text:
        context.bot.send_message(chat_id=chat_id, text='언제')
    elif '시' in text:
        context.bot.send_message(chat_id=chat_id, text='ㄱㄱ')
    elif 'ㅇㄷ' in text:
        context.bot.send_photo(chat_id=chat_id, photo=open('현재위치_bot_test.jpg', 'rb'))
    else:
        context.bot.send_message(chat_id=chat_id, text='뭐라카노')


echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)