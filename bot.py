import asyncio
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

# Լոգավորման կարգավորում
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = "8442849276:AAEYYKmjanCKSjjB16XUaEny5OOnpCfRamo"
MINI_APP_URL = " https://vigenamirkhanyan71-ai.github.io/AdEarn/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    
    keyboard = [
        [InlineKeyboardButton("🎬 Բացել AdEarn Mini App", web_app={"url": MINI_APP_URL})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = f"""
👋 Բարի գալուստ, {user.first_name}!

🎉 **AdEarn** - Դիտեք գովազդներ և ստացեք պարգեվներ

Սեղմեք կոճակը սկսելու համար 🎬
    """
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("ℹ️ Օգտագործեք /start Mini App-ին մուտք գործելու համար")

def main():
    # Ստեղծում ենք application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Ավելացնում ենք հրամաններ
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    print("🤖 Բոտը գործարկվում է...")
    print("✅ Բոտը աշխատում է! Սեղմեք Ctrl+C դադարեցնելու համար")
    
    # Գործարկում ենք բոտը
    application.run_polling()

if __name__ == '__main__':

    main()
