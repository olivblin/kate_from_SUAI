#coding=utf-8
import telebot
from telebot import types
import openai
import os
from openai import OpenAI

TOKEN = "7120359989:AAGTdb8z8HVz6Wzk0OKV0DWOTVLKfDeM89o"

bot = telebot.TeleBot(TOKEN)


OpenAI.api_key='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'
client=OpenAI(api_key=OpenAI.api_key)
def search(x):
    response=client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=[{'role':'user','content':x}],
        temperature=0.7,
        max_tokens=256,
        top_p=1
    )
    return (response.choices[0].message.content)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id,"Привет! Задай свой вопрос")
@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text:
        answer=search(message.text)
        bot.send_message(message.from_user.id, answer)


bot.polling(none_stop=True, interval=0)