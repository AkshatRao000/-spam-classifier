from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import openai

# 🔐 Replace these with your tokens
TELEGRAM_TOKEN = "8014679695:AAHToGCmoCoCQHA6RKCEas2mwnTccIHgSdc"
OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

# 🔮 List of motivational quotes
quotes = [
    "🌟 Believe in yourself and all that you are.",
    "🚀 Push yourself, because no one else is going to do it for you.",
    "🔥 Don’t watch the clock; do what it does. Keep going.",
    "💪 The pain you feel today will be the strength you feel tomorrow.",
    "🌈 Start where you are. Use what you have. Do what you can."
]

def start(update, context):
    update.message.reply_text("🙏 Welcome, Parth! Type /motivate or /ask <your question>")

def motivate(update, context):
    update.message.reply_text(random.choice(quotes))

def ask(update, context):
    question = ' '.join(context.args)
    if not question:
        update.message.reply_text("❓ Please ask a question after /ask.")
        return

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=100,
        temperature=0.7
    )
    answer = response.choices[0].text.strip()
    update.message.reply_text(f"💡 {answer}")

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("motivate", motivate))
    dp.add_handler(CommandHandler("ask", ask))
    updater.start_polling()
    print("🤖 Bot is running...")
    updater.idle()

if __name__ == "__main__":
    main()
