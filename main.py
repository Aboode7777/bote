import requests , re
import telebot
from telebot.types import InlineKeyboardButton as Btn , InlineKeyboardMarkup as Mak

dev = Mak().add(Btn('Dev',url="tg://user?id=1315011160"))
token = "6014757385:AAHv1Th4n1oxzYbPyN84-RMRICj7PK3aNHw"
bot = telebot.TeleBot(token)
#@BRoK8 & @Crrazy_8
@bot.message_handler(commands=["start"])
def welcome(message):
	name = message.from_user.first_name
	bot.reply_to(message,'مهلاً انتظر {} انا بوت اقوم بجلب اوقات الصلاة بأسم مدينك او بأسم دولتك .'.format(name),reply_markup=dev)

@bot.message_handler(content_types=['text'])
def timings(message):
	brok = bot.reply_to(message,'حسناا انتظر ')
	try:
		msg = message.text
		response = requests.get(f'https://timesprayer.com/prayer-times-in-{msg}.html').text
		ggg = re.search("<title>(.*?)</title>",response).group(1)
		fajr = re.search("<td><strong>صلاة الفجْر</strong></td><td>(.*?)</td></tr>", response).group(1);alshuruq = re.search("<td><strong> الشروق</strong></td><td>(.*?)</td></tr>", response).group(1);alzuhr = re.search("<td><strong>صلاة الظُّهْر</strong></td><td>(.*?)</td></tr>", response).group(1);aleasr = re.search("<td><strong>صلاة العَصر</strong></td><td>(.*?)</td></tr>", response).group(1);almaghrib = re.search("<td><strong>صلاة المَغرب</strong></td><td>(.*?)</td></tr>", response).group(1);aleisha = re.search("<td><strong>صلاة العِشاء</strong></td><td>(.*?)</td></tr>", response).group(1)
		
		almakan = re.search("<div><b>المكان :</b> (.*?)</div>",response).group(1)
		
		alsala = re.search("<div><b>الصلاة القادمة :</b> (.*?)</div>",response).group(1)
		
		saea = re.search("<div><b>ساعات الصيام :</b> (.*?)</div>",response).group(1)
		
		miladi = re.search("<div><b>التاريخ :</b> (.*?)</div>",response).group(1)
		
		hijri = re.search("<div><b>هجري :</b> (.*?)</div>",response).group(1)
		
		day = re.search("<b>اليوم :</b> (.*?)</div>",response).group(1)
		
		tim = re.search('<b id="timenowinthecity">(.*?)</b>',response).group(1)
		
		alzamania = re.search('(?<=title=")(\w+/\w+)', response).group(1)
		
		name = ggg.split("في")[1].strip()
		text = f"{ggg}\n\nصلاة الفجر: {fajr}\nالشروق: {alshuruq}\nصلاة الظهر: {alzuhr}\nصلاة العصر: {aleasr}\nصلاة المغرب: {almaghrib}\nصلاة العشاء: {aleisha}\n — — — — — —\nالمكان: {almakan}\nالصلاة القادمة: {alsala}\nساعات الصيام: {saea}\nالتاريخ: {miladi}\nهجري: {hijri}\nالوقت الان: {tim} حسب التوقيت المحلي في {name}\nاليوم: {day}\nالمنطقة الزمنية: {alzamania}"
		bot.delete_message(message.chat.id,message_id=brok.message_id)
		bot.reply_to(message,text)
		
	except:
		bot.edit_message_text(chat_id=message.chat.id, message_id=brok.message_id, text='لم اتعرف على اسم المدينة')

#المصدر تذكرو حبي 
#@BRoK8 & @Crrazy_8
bot.infinity_polling()
