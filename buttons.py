from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

BUTTON1_MONOBANK = "Log in Monobank 🏦"
BUTTON2_PRIVAT24 = "Log in Privat24 🏪"
BUTTON3_CHEAT = "Log in without authorization 💎"
BUTTON4_BACK1 = "Back ⬅️"
BUTTON5_NEW = "New request ✅"
BUTTON6_RATE = "Exchange rates 📉"
BUTTON6_RATE_USD = "USD 💵"
BUTTON6_RATE_EUR = "EUR 💶"
BUTTON6_RATE_GBP = "GBP 💷"
BUTTON6_BACK_TO_MENU = "Back to menu ⬅️"
BUTTON7_BALANCE = "Balance 💰"
BUTTON9_SETTINGS = "Settings ⚙"
BUTTON10_NEW_MONOBANK = "New request to Monobank 🏦"
BUTTON11_NEW_PRIVAT24 = "New request to Privat24 🏪"
BUTTON12_NEW_BOTH_BANKS = "New request to Monobank and Privat24"
BUTTON13_BALANCE_MONOBANK = "Monobank balance 🏦"
BUTTON14_BALANCE_PRIVAT24 = "Privat24 balance 🏪"
BUTTON15_BALANCE_BOTH_BANKS = "Monobank and Privat24 balances"
BUTTON16_SETTINGS_MONOBANK = "Change Monobank token 🏦"
BUTTON17_SETTINGS_PRIVAT24 = "Change Privat24 token 🏪"

def get_base_reply_keyboard():
    keyboard = [
        [
            KeyboardButton(BUTTON1_MONOBANK),
            KeyboardButton(BUTTON2_PRIVAT24),
        ],
        [
            KeyboardButton(BUTTON3_CHEAT),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard = keyboard,
        resize_keyboard = False,
    )
    return ReplyKeyboardRemove(
        remove_keyboard = True,
    )

def get_base_reply_keyboard_back():
    keyboard = [
        [
            KeyboardButton(BUTTON4_BACK1),
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard = keyboard,
        resize_keyboard = True,
    )
    return ReplyKeyboardRemove(
        remove_keyboard = True,
    )

def get_base_reply_keyboard_main():
    keyboard = [
        [
            KeyboardButton(BUTTON5_NEW),
            KeyboardButton(BUTTON6_RATE),
        ],
        [
            KeyboardButton(BUTTON7_BALANCE),
            KeyboardButton(BUTTON9_SETTINGS),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard = keyboard,
        resize_keyboard = False,
    )
    return ReplyKeyboardRemove(
        remove_keyboard = True,
    )

def get_base_reply_keyboard_main_new():
    keyboard = [
        [
            KeyboardButton(BUTTON10_NEW_MONOBANK),
            KeyboardButton(BUTTON11_NEW_PRIVAT24),
        ],
        [
            KeyboardButton(BUTTON12_NEW_BOTH_BANKS),
        ],
        [
            KeyboardButton(BUTTON6_BACK_TO_MENU),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard = keyboard,
        resize_keyboard = False,
    )

def get_base_reply_keyboard_main_rate():
    keyboard = [
        [
            KeyboardButton(BUTTON6_RATE_USD),
            KeyboardButton(BUTTON6_RATE_USD),
            KeyboardButton(BUTTON6_RATE_GBP),
        ],
        [
            KeyboardButton(BUTTON6_BACK_TO_MENU),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard = keyboard,
        resize_keyboard = False,
    )

def get_base_reply_keyboard_main_balance():
    keyboard = [
        [
            KeyboardButton(BUTTON13_BALANCE_MONOBANK),
            KeyboardButton(BUTTON14_BALANCE_PRIVAT24),
        ],
        [
            KeyboardButton(BUTTON15_BALANCE_BOTH_BANKS),
        ],
        [
            KeyboardButton(BUTTON6_BACK_TO_MENU),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard = keyboard,
        resize_keyboard = False,
    )

def get_base_reply_keyboard_main_settings():
    keyboard = [
        [
            KeyboardButton(BUTTON16_SETTINGS_MONOBANK),
        ],
        [
            KeyboardButton(BUTTON17_SETTINGS_PRIVAT24),
        ],
        [
            KeyboardButton(BUTTON6_BACK_TO_MENU),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard = keyboard,
        resize_keyboard = False,
    )
    return ReplyKeyboardRemove(
        remove_keyboard = True,
    )