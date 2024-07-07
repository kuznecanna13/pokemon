import telebot 
from config import token

from logic import *

bot = telebot.TeleBot(token) 



@bot.message_handler(commands=['go'])
def start(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
            pokemon.hp += 10
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
            pokemon.power += 10
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.info())
    else:
        bot.reply_to(message, "У вас ещё нет покемона!")

@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            if pok.hp == 0:
                bot.reply_to(message, "У покемона слишком мало здоровья. Покормите, чтобы восстановить /feed")
            else:
                res = pok.attack(enemy)
                bot.reply_to(message, res)
        else:
            bot.reply_to(message, "Сражаться можно только с покемонами")
    else:
            bot.reply_to(message, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")
            
@bot.message_handler(commands=['feed'])
def feed(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "У вас ещё нет покемона!")
    else:
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.feed())   

@bot.message_handler(commands=['next'])
def next_lvl(message):
    pok = Pokemon.pokemons[message.from_user.username]
    if pok.next == 0:
        bot.reply_to(message, f"До следующего уровня: {pok.maxexp - pok.exp} очков опыта")
    else:
        bot.send_message(message.chat.id, pok.nextlvl())

@bot.message_handler(commands=['hp'])
def plus_stats(message):
    pok = Pokemon.pokemons[message.from_user.username]
    if pok.next > 0:
        bot.send_message(message.chat.id, pok.up_hp())
    else:
        bot.reply_to(message, "Нет улучшений")

@bot.message_handler(commands=['power'])
def plus_stats(message):
    pok = Pokemon.pokemons[message.from_user.username]
    if pok.next > 0:
        bot.send_message(message.chat.id, pok.up_power())
    else:
        bot.reply_to(message, "Нет улучшений")

bot.infinity_polling(none_stop=True)