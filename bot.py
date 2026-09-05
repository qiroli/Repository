from telegram import Update 
from telegram.ext import CommandHandler , ContextTypes , Application
import env

app = Application.builder().token(env.BOT_TOKEN).build()

def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    return update.message.reply_text(f"SALOM {update.effective_user.first_name} MEN BOTMAN 🤖 ")
def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    return update.message.reply_text("UZUR MEN SIZGA YORDAM BERA OLMAYMAN 😞")
def gls(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    return update.message.reply_text(f"salom {update.effective_user.last_name}")

app.add_handler(CommandHandler("start" ,  start))
app.add_handler(CommandHandler("help" ,  help))
app.add_handler(CommandHandler("gls" ,  gls))
app.run_polling()