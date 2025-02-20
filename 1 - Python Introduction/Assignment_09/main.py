from random import randint
import qrcode as q
import gtts
from persiantools.jdatetime import JalaliDate
import telebot
import datetime

bot = telebot.TeleBot("token", parse_mode=None)

random_numbers = {}

game_markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
restart_key = telebot.types.KeyboardButton("/restart")
game_markup.add(restart_key)

markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
key_1 = telebot.types.KeyboardButton("/game")
key_2 = telebot.types.KeyboardButton("/age")
key_3 = telebot.types.KeyboardButton("/max")
key_4 = telebot.types.KeyboardButton("/voice")
key_5 = telebot.types.KeyboardButton("/argmax")
key_6 = telebot.types.KeyboardButton("/qrcode")
key_7 = telebot.types.KeyboardButton("/help")
markup.add(key_1, key_2, key_3, key_4, key_5, key_6, key_7)


@bot.message_handler(commands=['start'])
def start_chat(message):
    first_name = message.from_user.first_name
    bot.send_message(message.chat.id, f'Hello {first_name} ...')
    print(message.from_user.username)


@bot.message_handler(commands=['game'])
def start_game(message):
    username = message.from_user.username
    random_numbers[username] = randint(0, 100)
    msg = bot.send_message(message.chat.id, f'Enter Your Number (1, 100)...', reply_markup=game_markup)
    bot.register_next_step_handler(msg, game)
    print(message.from_user.username)


@bot.message_handler(commands=['restart'])
def restart_game(message):
    username = message.from_user.username
    random_numbers[username] = randint(0, 100)
    msg = bot.send_message(message.chat.id, f'Restarted...')
    bot.register_next_step_handler(msg, game)
    print(message.from_user.username)


def game(message):
    print(message.from_user.username)
    username = message.from_user.username
    try:
        user_input = int(message.text)
        if user_input > random_numbers[username]:
            msg = bot.send_message(message.chat.id, 'Your Number Is Bigger...', reply_markup=game_markup)
            bot.register_next_step_handler(msg, game)
        elif user_input < random_numbers[username]:
            msg = bot.send_message(message.chat.id, 'Your Number Is Smaller...', reply_markup=game_markup)
            bot.register_next_step_handler(msg, game)
        else:
            msg = bot.send_message(message.chat.id, 'You Win...', reply_markup=game_markup)
            bot.register_next_step_handler(msg, game)
    except:
        pass
        # msg = bot.send_message(message.chat.id, 'Invalid Input...', reply_markup=game_markup)
        # bot.register_next_step_handler(msg, game)


@bot.message_handler(commands=['age'])
def age(message):
    print(message.from_user.username)
    msg = bot.send_message(message.chat.id, f'Enter Your Age 1385/12/02 ...')
    bot.register_next_step_handler(msg, age_calculation)


def age_calculation(message):
    print(message.from_user.username)
    try:
        year, month, day = str(message.text).split('/')
        year, month, day = int(year), int(month), int(day)
        miladi_date = JalaliDate(year, month, day).to_gregorian()
        miladi_date = datetime.date.today() - miladi_date
        user_age = miladi_date.days // 365
        bot.send_message(message.chat.id, f'Your Age {user_age}')

    except:
        msg = bot.send_message(message.chat.id, 'Invalid Input...')
        bot.register_next_step_handler(msg, age_calculation)


@bot.message_handler(commands=['voice'])
def age(message):
    print(message.from_user.username)
    msg = bot.send_message(message.chat.id, f'Enter Your Text ...')
    bot.register_next_step_handler(msg, get_voice)


def get_voice(message):
    print(message.from_user.username)
    user_text = message.text
    voice = gtts.gTTS(user_text, lang="en", slow=False)
    voice.save("/home/voice.mp3")
    with open("/home/voice.mp3", "rb") as file:
        bot.send_voice(message.chat.id, file)


@bot.message_handler(commands=['max'])
def max_item(message):
    print(message.from_user.username)
    msg = bot.send_message(message.chat.id, f'Enter Your Numbers 10,20,30,40 ...')
    bot.register_next_step_handler(msg, find_max)


def find_max(message):
    print(message.from_user.username)
    user_list = str(message.text).split(',')
    user_list = map(lambda text: text.strip(), user_list)
    bot.send_message(message.chat.id, f'Max Arg is {max(user_list)}')


@bot.message_handler(commands=['argmax'])
def max_index_item(message):
    print(message.from_user.username)
    msg = bot.send_message(message.chat.id, f'Enter Your Numbers 10,20,30,40 ...')
    bot.register_next_step_handler(msg, find_index_max)


def find_index_max(message):
    print(message.from_user.username)
    user_list = str(message.text).split(',')
    user_list = list(map(lambda text: text.strip(), user_list))
    bot.send_message(message.chat.id, f'Max Arg Index Is {user_list.index(max(user_list))}')


@bot.message_handler(commands=["qrcode"])
def qrcode(message):
    print(message.from_user.username)
    msg = bot.send_message(message.chat.id, "Enter Your Text ...")
    bot.register_next_step_handler(msg, get_qrcode)


def get_qrcode(message):
    print(message.from_user.username)
    qr_img = q.make(message.text)
    qr_img.save("/home/qrcode.png")
    with open("/home/qrcode.png", "rb") as file:
        bot.send_photo(message.chat.id, file)


@bot.message_handler(commands=["help"])
def help(message):
    print(message.from_user.username)
    text = '''
        1- /game -> Number Game
        2- /restart -> Restart Game
        3- /age -> Calculate Age With Year Of Birth
        4- /voice -> Convert Text To Voice
        5- /max -> Find The Largest Value
        6- /argmax -> Find The Largest Index Value
        7- /qrcode -> Get QRcode With Text
        8- /help -> Show Help
    '''
    bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda m: True)
def menu(message):
    print(message.from_user.username)
    help(message)


bot.infinity_polling()
