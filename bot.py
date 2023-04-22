import json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

# membuka file app.json untuk membaca token dan id owner
with open('app.json') as f:
    data = json.load(f)
    TOKEN = data['token']
    OWNER_ID = data['owner_id']

# inisialisasi updater
updater = Updater(TOKEN, use_context=True)

# fungsi untuk menampilkan menu utama
def main_menu(update, context):
    user = update.message.from_user
    message = f'Hai {user.first_name}, selamat datang di Bot Feedback dan Rating!\nSilakan pilih opsi di bawah ini:'
    keyboard = [[InlineKeyboardButton("⭐️ Beri Rating", callback_data='rating')],
                [InlineKeyboardButton("💬 Beri Feedback", callback_data='feedback')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=user.id, text=message, reply_markup=reply_markup)

# fungsi untuk menampilkan form rating
def show_rating_form(update, context):
    user = update.callback_query.from_user
    message = 'Silakan beri rating untuk bot kami:'
    keyboard = [[InlineKeyboardButton("⭐️", callback_data='1'),
                 InlineKeyboardButton("⭐️⭐️", callback_data='2'),
                 InlineKeyboardButton("⭐️⭐️⭐️", callback_data='3')],
                [InlineKeyboardButton("⭐️⭐️⭐️⭐️", callback_data='4'),
                 InlineKeyboardButton("⭐️⭐️⭐️⭐️⭐️", callback_data='5')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=user.id, text=message, reply_markup=reply_markup)

# fungsi untuk menampilkan form feedback
def show_feedback_form(update, context):
    user = update.callback_query.from_user
    message = 'Silakan berikan feedback untuk bot kami:'
    keyboard = [[KeyboardButton("🔙 Kembali ke Menu Utama")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    context.bot.send_message(chat_id=user.id, text=message, reply_markup=reply_markup)
    # mengubah status user menjadi "menunggu feedback"
    context.user_data['status'] = 'menunggu_feedback'

# fungsi untuk memproses feedback yang diberikan user
def process_feedback(update, context):
    user = update.message.from_user
    feedback = update.message.text
    message = 'Terima kasih atas feedback yang Anda berikan!'
    keyboard = [[KeyboardButton("🔙 Kembali ke Menu Utama")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    context.bot.send_message(chat_id=user.id, text=message, reply_markup=reply_markup)
    # mengubah status user menjadi "selesai"
    context.user_data['status'] = 'selesai'
    # kirim feedback ke owner bot
    owner_id = 'your_owner_id_here'
    owner_message = f'Feedback dari user {user.first_name} (id:{user.id}): {feedback}'
    context.bot.send_message(chat_id=owner_id, text=owner_message)

# fungsi untuk memproses rating yang diberikan user
def process_rating(update, context):
    user = update.callback_query.from_user
    rating = update.callback_query.data
    message = f'Terima kasih atas rating {rating} yang Anda berikan!'
    keyboard = [[KeyboardButton("🔙 Kembali ke Menu Utama")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    context.bot.send_message(chat_id=user.id, text=message, reply_markup=reply_markup)
    # mengubah status user menjadi "selesai"
    context.user_data['status'] = 'selesai'
    # kirim rating ke owner bot
    owner_id = 'your_owner_id_here'
    owner_message = f'Rating dari user {user.first_name} (id:{user.id}): {rating}'
    context.bot.send_message(chat_id=owner_id, text=owner_message)

# fungsi untuk menampilkan pesan error
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# main program
if __name__ == '__main__':
    # baca token bot dan id owner dari app.json
    with open('app.json', 'r') as f:
        data = json.load(f)
    TOKEN = data['token']
    owner_id = data['owner_id']

    # inisialisasi updater
    updater = Updater(TOKEN, use_context=True)

    # register handler
    updater.dispatcher.add_handler(CommandHandler('start', main_menu))
    updater.dispatcher.add_handler(CallbackQueryHandler(show_rating_form, pattern='rating'))
    updater.dispatcher.add_handler(CallbackQueryHandler(show_feedback_form, pattern='feedback'))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), process_feedback))
    updater.dispatcher.add_handler(CallbackQueryHandler(process_rating))
    updater.dispatcher.add_error_handler(error)

    # start bot
    updater.start_polling()
    updater.idle()
