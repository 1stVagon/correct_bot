import telebot
import language_tool_python

API_TOKEN = '<token>'
bot = telebot.TeleBot(API_TOKEN)

# function for text correction
def correct_text(text):
    tool = language_tool_python.LanguageTool('en')
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text

# processing start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hi there, I am CorrectorBot. I am there to correct your text')
    
# processing messages and correcting them
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    corrected_text = correct_text(text)
    bot.reply_to(message, f'Source: {text}\nСorrected text: {corrected_text}')

# start bot
bot.polling()

