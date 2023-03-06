import telebot
from telegram import *

bot = telebot.TeleBot('5517340699:AAF3pLYBW3wlELO1k8fC1WghoEa6BP1daPA')


@bot.messagehandler(commands=['start'])
def sendwelcome(message):
    bot.replyto(message, 'Welcome! How can I help you?')


@bot.messagehandler(func=lambda message: True)
def echoall(message):
    text = message.text
    if text == 'Hi':
        bot.replyto(message, 'Hello!')


bot.polling()
