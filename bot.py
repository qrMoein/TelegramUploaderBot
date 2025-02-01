from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

TOKEN = "7924898020:AAEGOuPAlJ4sCqno8dtyHQS9XhHqeEjUX8M"
CHANNEL_USERNAME = "@ForceJoin123_bot"

def start(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    if is_user_in_channel(user_id):
        update.message.reply_text("سلام! لطفاً فایلت رو بفرست 🚀")
    else:
        keyboard = [[InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{ForceJoin123_bot[1:]}")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("🚫 برای استفاده از ربات، ابتدا در کانال عضو شو!", reply_markup=reply_markup)

def is_user_in_channel(user_id):
    url = f"https://api.telegram.org/bot{7924898020:AAEGOuPAlJ4sCqno8dtyHQS9XhHqeEjUX8M}/getChatMember?chat_id={CHAForceJoin123_botNNEL_USERNAME}&user_id={user_id}"
    response = requests.get(url).json()
    status = response.get("result", {}).get("status", "")
    return status in ["member", "administrator", "creator"]

def handle_docs(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    if is_user_in_channel(user_id):
        file = update.message.document
        update.message.reply_text(f"✅ فایل شما دریافت شد!\n\nنام فایل: {file.file_name}")
    else:
        update.message.reply_text("🚫 اول در کانال عضو شو!")

def main():
    updater = Updater(7924898020:AAEGOuPAlJ4sCqno8dtyHQS9XhHqeEjUX8M, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.document, handle_docs))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
