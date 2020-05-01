import datetime
import telebot
import requests
import re

from config import token

from logging import getLogger

from telebot import types
from telegram import Bot
from telegram import Update
from telegram import Chat
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram import ReplyKeyboardMarkup
from telegram import ChatPermissions

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler

from telegram.ext.dispatcher import run_async

from buttons import BUTTON1_MONOBANK
from buttons import BUTTON2_PRIVAT24
from buttons import BUTTON3_CHEAT
from buttons import BUTTON4_BACK1
from buttons import BUTTON5_NEW
from buttons import BUTTON6_RATE
from buttons import BUTTON6_RATE_USD
from buttons import BUTTON6_RATE_EUR 
from buttons import BUTTON6_RATE_GBP 
from buttons import BUTTON6_BACK_TO_MENU 
from buttons import BUTTON7_BALANCE
from buttons import BUTTON9_SETTINGS
from buttons import BUTTON10_NEW_MONOBANK
from buttons import BUTTON11_NEW_PRIVAT24
from buttons import BUTTON12_NEW_BOTH_BANKS
from buttons import BUTTON13_BALANCE_MONOBANK
from buttons import BUTTON14_BALANCE_PRIVAT24
from buttons import BUTTON15_BALANCE_BOTH_BANKS
from buttons import BUTTON16_SETTINGS_MONOBANK
from buttons import BUTTON17_SETTINGS_PRIVAT24


from buttons import get_base_reply_keyboard
from buttons import get_base_reply_keyboard_back
from buttons import get_base_reply_keyboard_main
from buttons import get_base_reply_keyboard_main_new
from buttons import get_base_reply_keyboard_main_rate
from buttons import get_base_reply_keyboard_main_balance
from buttons import get_base_reply_keyboard_main_settings


bot = telebot.TeleBot(token)

logger = getLogger(__name__)


def debug_requests(f):
    # decorator for requests
    def inner(*args, **kwargs):
        try:
            logger.error(args)
            logger.error(kwargs)
            logger.info("Обращение в функцию {}".format(f.__name__))
            return f(*args, **kwargs)
        except Exception:
            logger.exception("Ошибка в обработчике {}".format(f.__name__))
            raise 
    return inner





# # buttons
CALLBACK_BUTTON0_BACK = "callback_button0_back"
CALLBACK_BUTTON1_AUTHORIZATION = "callback_button1_authorization"
CALLBACK_BUTTON2_NEW_REQUEST = "callback_button2_new_request"
CALLBACK_BUTTON3_RATE = "callback_button3_rate"
CALLBACK_BUTTON4_BALANCE = "callback_button4_balance"
CALLBACK_BUTTON5_SETTINGS = "callback_button5_settings"

TITLES = {
    CALLBACK_BUTTON0_BACK: "Back ⬅️",
    CALLBACK_BUTTON1_AUTHORIZATION: "Banks authorization 🔄",
    CALLBACK_BUTTON2_NEW_REQUEST: "New request ✅",
    CALLBACK_BUTTON3_RATE: "Exchange rates 📉",
    CALLBACK_BUTTON4_BALANCE: "Balance 💰",
    CALLBACK_BUTTON5_SETTINGS: "Settings ⚙",
}





# keyboards
# first keyboard under messages
def get_base_inline_keyboard():
    # получить клавиатуру, она будет видна под каждым сообщением
    keyboard = [
        #каждый элемент внутри этого списка - один вертикальный столбец. сколько кнопок - столько столбцов
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_AUTHORIZATION], callback_data=CALLBACK_BUTTON1_AUTHORIZATION),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_NEW_REQUEST], callback_data=CALLBACK_BUTTON2_NEW_REQUEST),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_RATE], callback_data=CALLBACK_BUTTON3_RATE),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON4_BALANCE], callback_data=CALLBACK_BUTTON4_BALANCE),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_SETTINGS], callback_data=CALLBACK_BUTTON5_SETTINGS),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

# second keyboard under messages
def get_base_inline_keyboard_back():
    # получить клавиатуру, она будет видна под каждым сообщением
    keyboard = [
        #каждый элемент внутри этого списка - один вертикальный столбец. сколько кнопок - столько столбцов
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON0_BACK], callback_data=CALLBACK_BUTTON0_BACK),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

# functions for click on each button from keyboard
# @debug_requests
def keyboard_callback_handler(bot:Bot, update:Update, chat_data=None, **kwargs):
    query = update.callback_query
    data = query.data
    # now = datetime.datetime.now()

    # current_text = update.effective_message.text

    if data == CALLBACK_BUTTON0_BACK:
        reply_text = "Welcome to help page!\n\nIn case you have problems, you always can use /help to find an answer to your problem. To continue, from the list below please select the topic of your problem: "
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = reply_text,
            reply_markup=get_base_inline_keyboard(),
        )
    
    elif data == CALLBACK_BUTTON1_AUTHORIZATION:
        reply_text = "Authorization in banks 🔄:\n\nTo get start using banks services, you should add to bot your token.\n\nFirst of all, you should go to Monobank (https://api.monobank.ua/) or Privat24 (https://api.privatbank.ua/), depends on your needs. After that, from the begining  menu (you can stop and restart bot), you go to Monobank or Privat24. There you will also see the instructions of using. Your should send the next message for Monobank or Privat24:\n\nMonobank token: (token)\nPrivat24 token: (token)\n\n(token) - instead of this you put your own token. "
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = reply_text,
            reply_markup=get_base_inline_keyboard_back(),
        )

    elif data == CALLBACK_BUTTON2_NEW_REQUEST:
        reply_text = "Creating a new request ✅:\n\nTo create a new request you should go to 'main menu' > 'new request'.\nCreating a new request you can for each bank separately, or for both together. You will receive the information about your incomes, expencss and balance."
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = reply_text,
            reply_markup=get_base_inline_keyboard_back(),
        )

    elif data == CALLBACK_BUTTON3_RATE:
        reply_text = "Exchange rates 📉:\n\nTo get the latest information about exchange rates, you should go to 'main menu' > 'exchange rates'."
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = reply_text,
            reply_markup=get_base_inline_keyboard_back(),
        )

    elif data == CALLBACK_BUTTON4_BALANCE:
        reply_text = "Getting the balance 💰:\n\nTo get the latest information about your balances, you should go to 'main menu' > 'balance'."
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = reply_text,
            reply_markup=get_base_inline_keyboard_back(),
        )

    elif data == CALLBACK_BUTTON5_SETTINGS:
        reply_text = "Settings for bot ⚙:\n\nTo change the information about your bank account, you should go to 'main menu' > 'settings'."
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = reply_text,
            reply_markup=get_base_inline_keyboard_back(),
        )





# functions
# start
@debug_requests
def do_start(bot:Bot, update:Update):
    user = update.effective_user
    if user: 
        name = user.first_name
    else:
        name = 'Anonim'

    reply_text = f'Hello, {name}!\n\nTo get started, you need to log in to banks such as Monobank and Privat24. For authorization you need to enter your X-Token for each bank.\nIf you want to continue working without authorization, click on the button "Log in without authorization 💎".\n\nIn case you have problems, to get help you can use /help'

    bot.send_message(
        chat_id=update.message.chat_id,
        text=reply_text,
        reply_markup=get_base_reply_keyboard(),
    )

# help 
@debug_requests 
def do_help(bot:Bot, update:Update):
    reply_text = "Welcome to help page!\n\nIn case you have problems, you always can use /help to find an answer to your problem. To continue, from the list below please select the topic of your problem: "
    bot.send_message(
        chat_id=update.effective_message.chat_id,
        text = reply_text,
        reply_markup=get_base_inline_keyboard(),
    )
    print('nu typa rabotaet')


# message repeating
@debug_requests
@run_async
def do_echo(bot: Bot, update: Update):
    # chat_id = update.message.chat_id
    text = update.effective_message.text
    
    # first page
    if text == BUTTON1_MONOBANK:
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "To make authorization in your Monobank account, please send me here your token.\n\nTo get your token, you should use this link https://api.monobank.ua/. Copy your token and send it here only in such way:",
            reply_markup=get_base_reply_keyboard_back(),
        )
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "Monobank token: (token)",
            reply_markup=get_base_reply_keyboard_back(),
        )

    elif re.search(r'Monobank token: ', text):
        text = update.effective_message.text
        reply_text = f'Success! Your {text}\nGo back to menu to continue.'
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            message_id = update.effective_message.message_id,
            text = reply_text,
            reply_markup=get_base_reply_keyboard_back(),
        )

    elif text == BUTTON2_PRIVAT24:
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "To make authorization in your Privat24 account, please send me here your token.\n\nTo get your token, you should use this link https://api.privatbank.ua/. Copy your token and send it here only in such way:",
            reply_markup=get_base_reply_keyboard_back(),
        )
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "Privat24 token: (token)",
            reply_markup=get_base_reply_keyboard_back(),
        )

    elif re.search(r'Privat24 token: ', text):
        text = update.effective_message.text
        reply_text = f'Success! Your {text}\nGo back to menu to continue.'
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            message_id = update.effective_message.message_id,
            text = reply_text,
            reply_markup=get_base_reply_keyboard_back(),
        )

    elif text == BUTTON3_CHEAT:
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "Great! You finished your authorization, so now you can you all functions of bot.\nLet's find out what the bot can do:\n\n1) New request - allows you to get expenses and income for today, as well as the balance on the account\n2) Exchange rate - allows you to see the exchange rate USD, EUR, GBP\n3) Balance - receiving information about the balance in your account;\n4) Settings allow you to configure the bot, change your tokens.",
            reply_markup=get_base_reply_keyboard_main(),
        )

    elif text == BUTTON4_BACK1:
        user = update.effective_user
        if user: 
            name = user.first_name
        else:
            name = 'Anonim'
        reply_text = f'{name}, select the bank from the list in which you want to log in.'

        bot.send_message(
            chat_id=update.message.chat_id,
            text=reply_text,
            reply_markup=get_base_reply_keyboard(),
        )
    


    # Main menu
    # new START
    elif text == BUTTON5_NEW:
        user = update.effective_user
        if user: 
            name = user.first_name
        else:
            name = 'Anonim'
        reply_text = f'{name}, please select the bank you want to make a request:'

        bot.send_message(
            chat_id=update.message.chat_id,
            text=reply_text,
            reply_markup=get_base_reply_keyboard_main_new(),
        )

    elif text == BUTTON10_NEW_MONOBANK:
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "Your Monobank 🏦 info:\nTime: 24hours\n*****\nIncomes: 10000\nRate: UAH\n*****\nOutcomes: 2500\nRate: UAH\n*****\nBalance: 2500\nRate: UAH",
            reply_markup=get_base_reply_keyboard_main_new(),
        )

    elif text == BUTTON11_NEW_PRIVAT24:
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "Your Privat24 🏪 info:\nTime: 24hours\n*****\nIncomes: 10000\nRate: UAH\n*****\nOutcomes: 2500\nRate: UAH\n*****\nBalance: 2500\nRate: UAH",
            reply_markup=get_base_reply_keyboard_main_new(),
        )

    elif text == BUTTON12_NEW_BOTH_BANKS:
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "Your Monobank 🏦 info:\nTime: 24hours\n*****\nIncomes: 10000\nRate: UAH\n*****\nOutcomes: 2500\nRate: UAH\n*****\nBalance: 2500\nRate: UAH",
            reply_markup=get_base_reply_keyboard_main_new(),
        )
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "Your Privat24 🏪 info:\nTime: 24hours\n*****\nIncomes: 10000\nRate: UAH\n*****\nOutcomes: 2500\nRate: UAH\n*****\nBalance: 2500\nRate: UAH",
            reply_markup=get_base_reply_keyboard_main_new(),
        )
    # new FINISH


    elif text == BUTTON6_BACK_TO_MENU: 
        bot.send_message(
            chat_id=update.message.chat_id,
            text  = "Back to main menu: ",
            reply_markup=get_base_reply_keyboard_main(),
        )


    # rate START
    elif text == BUTTON6_RATE:
        user = update.effective_user
        if user: 
            name = user.first_name
        else:
            name = 'Anonim'
        reply_text = f'{name}, in the future here it will be exchange rates.'

        bot.send_message(
            chat_id=update.message.chat_id,
            text=reply_text,
            reply_markup=get_base_reply_keyboard_main_rate(),
        )
    # rate FINISH
        

    # balance START
    elif text == BUTTON7_BALANCE:
        user = update.effective_user
        if user: 
            name = user.first_name
        else:
            name = 'Anonim'
        reply_text = f'{name}, please select the bank you want to check the balance:'

        bot.send_message(
            chat_id=update.message.chat_id,
            text=reply_text,
            reply_markup=get_base_reply_keyboard_main_balance(),
        )

    elif text == BUTTON13_BALANCE_MONOBANK:
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "Your Monobank 🏦 balance:\nBalance: 2500\nRate: UAH",
            reply_markup=get_base_reply_keyboard_main_balance(),
        )

    elif text == BUTTON14_BALANCE_PRIVAT24:
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "Your Privat24 🏪 balance:\nBalance: 2500\nRate: UAH",
            reply_markup=get_base_reply_keyboard_main_balance(),
        )

    elif text == BUTTON15_BALANCE_BOTH_BANKS:
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "Your Monobank 🏦 balance:\nBalance: 2500\nRate: UAH",
            reply_markup=get_base_reply_keyboard_main_balance(),
        )
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "Your Privat24 🏪 balance:\nBalance: 2500\nRate: UAH",
            reply_markup=get_base_reply_keyboard_main_balance(),
        )
    # balance FINISH


    # settings START
    elif text == BUTTON9_SETTINGS:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Here it will be settings for BOT.",
            reply_markup=get_base_reply_keyboard_main_settings()
        )

    elif text == BUTTON16_SETTINGS_MONOBANK:
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "To change your Monobank token, please send me here your new token.\n\nTo get your token, you should use this link https://api.monobank.ua/. Copy your token and send it here only in such way:",
            reply_markup=get_base_reply_keyboard_main_settings(),
        )
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "New Monobank token: (token)",
            reply_markup=get_base_reply_keyboard_main_settings(),
        )

    elif re.search(r'New Monobank token: ', text):
        text = update.effective_message.text
        reply_text = f'Success! Your {text}'
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            message_id = update.effective_message.message_id,
            text = reply_text,
            reply_markup=get_base_reply_keyboard_main_settings(),
        )

    elif text == BUTTON2_PRIVAT24:
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "To change your Privat24 token, please send me here your token.\n\nTo get your token, you should use this link https://api.privatbank.ua/. Copy your token and send it here only in such way:",
            reply_markup=get_base_reply_keyboard_main_settings(),
        )
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text = "New Privat24 token: (token)",
            reply_markup=get_base_reply_keyboard_main_settings(),
        )
        
    elif re.search(r'New Privat24 token: ', text):
        text = update.effective_message.text
        reply_text = f'Success! Your {text}'
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            message_id = update.effective_message.message_id,
            text = reply_text,
            reply_markup=get_base_reply_keyboard_main_settings(),
        )
    # more FINISH


    else:
        user = update.effective_user
        if user:  
            name = user.first_name
        else:
            name = 'Аnonim'
        text = update.effective_message.text
        reply_text = f'{name}, your message: \t{text}\nTry again'
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            message_id = update.effective_message.message_id,
            text = reply_text,
        )
    





# bot body
@debug_requests
def main():
    print('Start')
    bot = Bot (
        token=token,
    )
    updater = Updater(
        bot = bot, 
    )


    start_handler = CommandHandler("start", do_start)
    help_handler = CommandHandler("help", do_help)
    # mes_handler = CommandHandler("mes", do_mes)
    message_handler = MessageHandler(Filters.text, do_echo)
    buttons_handler = CallbackQueryHandler(callback=keyboard_callback_handler, pass_chat_data=True)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    # updater.dispatcher.add_handler(mes_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.dispatcher.add_handler(buttons_handler)
 
    updater.start_polling()
    updater.idle()
    print('Finish')

if __name__ == "__main__":
    main()