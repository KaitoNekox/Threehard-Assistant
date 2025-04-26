from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Reemplaza 'YOUR_TOKEN' con el token de tu bot
TOKEN = '7640760603:AAHZ0tZuhwXYOdFSGqrfNYzt5VikJ1UvflE'

# Función que maneja el comando /start
def start(update: Update, context: CallbackContext):
    user = update.effective_user.first_name
    keyboard = [
        [
            InlineKeyboardButton("Website", url="https://example.com"),  # Cambia 'https://example.com' a tu URL
            InlineKeyboardButton("Menu", callback_data='help')
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(
        f"Hello {user}, I am *Threehard Assistant Forum* and I can help you with the Threehard website. ✌🏻",
        reply_markup=reply_markup,
        parse_mode='MarkdownV2'
    )

# Función que maneja el callback del botón "Menu"
def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    if query.data == 'help':
        query.edit_message_text(text="Aquí tienes el menú de ayuda: ...")  # Agrega tu menú de ayuda aquí

def main():
    updater = Updater(TOKEN)

    # Obtén el dispatcher para registrar manejadores
    dp = updater.dispatcher

    # Comando /start
    dp.add_handler(CommandHandler("start", start))
    # Manejador para los botones
    dp.add_handler(CallbackQueryHandler(button_handler))

    # Inicia el bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
