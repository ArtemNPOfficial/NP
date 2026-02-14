import telebot
bot=telebot.TeleBot("8590892256:AAEtT89d9xy6NIMADjbBj9WvyDUN0jQubmI")

@bot.message_handler(func=lambda msg: True)
def response(msg):
    bot.send_message(msg.chat.id, "Над ботом ведутся технические работы. Попробуйте позже.")

bot.polling(none_stop=True)
