import anime_images_api
import telebot
# @BRoK8 & @Crrazy_8

api = anime_images_api.Anime_Images()
token = "6014757385:AAHv1Th4n1oxzYbPyN84-RMRICj7PK3aNHw"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def Welcome(message:str):
    idu = message.from_user.id
    if message.chat.type == 'private' and not ex_id(str(idu)):
        with open("users.txt", 'a') as f:
            f.write("{}\n".format(idu))

    keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        telebot.types.InlineKeyboardButton('صور لطيفة', callback_data='sfw'),
        telebot.types.InlineKeyboardButton('صور للكبار فقط ⒙', callback_data='nsfw'),
        telebot.types.InlineKeyboardButton('More Bots',url="Crrazy_8.t.me")
    )
    name = message.from_user.first_name
    bot.reply_to(message,f"أهلاً بك [{name}](tg://settings) في بوت يقوم بتوفير صور للأنمي، اختر نوع الصور التي تفضله .",parse_mode="markdown",reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def All(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    if call.data == 'sfw':
        sfw = api.get_sfw('hug')
        send_photo(bot, chat_id, sfw, 'sfw', message_id)
    elif call.data == 'nsfw':
        nsfw = api.get_nsfw('hentai')
        send_photo(bot, chat_id, nsfw, 'nsfw', message_id)

def ex_id(id):
    with open("users.txt", 'r') as file:
        return any(line.strip() == id for line in file)

def send_photo(bot, chat_id, photo, category, message_id):
    keyboard = telebot.types.InlineKeyboardMarkup()
    next_button = telebot.types.InlineKeyboardButton(text='صورة أخرى', callback_data=category)
    keyboard.add(next_button)

    try:
        bot.edit_message_media(chat_id=chat_id, message_id=message_id, media=telebot.types.InputMediaPhoto(photo), reply_markup=keyboard)
    except telebot.apihelper.ApiException:
        bot.send_photo(chat_id, photo, reply_markup=keyboard)

#تذكر مصدري لا تكون فاشل وتغير الحقوق - 
#مبرمج الملف & @BRoK8
#قناتي & @Crrazy_8
bot.infinity_polling()