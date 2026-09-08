from telegram import Update 
from telegram.ext import CommandHandler , ContextTypes , Application
import env

app = Application.builder().token(env.BOT_TOKEN).build()

def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    first_name = update.effective_user.first_name
    last_name = update.effective_user.last_name
    user_id = update.effective_user.id
    is_bot = update.effective_user.is_bot
    language_code = update.effective_user.language_code
    username = update.effective_user.username

    if is_bot == True:
        is_bot = "bot ekan"
    else:
        is_bot = "bot emassiz"

    if username == None:
        username = "username yo'q"

    reply_text = f"""
    assalomu alaykum {first_name}

    siz haqida ma'lumotlar:
    1. telegram id {user_id}
    2. username: {username}
    3. telegramni {language_code} tilida ishlatasiz
    
    """
    return update.message.reply_text(reply_text)

async def cheksiz_salom(update: Update, context: ContextTypes.DEFAULT_TYPE):
    while True:
        reply_text = update.message.reply_text("salom")
        await reply_text
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("cheksiz_salom", cheksiz_salom))
print("bot ishga tushdi...")
app.run_polling() # run_webhook