import telebot
import config
from bs4 import BeautifulSoup
import requests
from pprint import pprint

request = requests.get('https://ua.sinoptik.ua/погода-рівне')
html = BeautifulSoup(request.content, 'html.parser')
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def buttons(message):
    today = html.find_all('div', 'main loaded')
    today_day = today[0].select_one('.day-link').text
    today_date = today[0].select_one('.date').text
    today_month = today[0].select_one('.month').text

    day2 = html.find_all('div', 'main')[1]
    dday2 = day2.select_one('.day-link').text
    date2 = day2.select_one('.date').text
    month2 = day2.select_one('.month').text

    day3 = html.find_all('div', 'main')[2]
    dday3 = day3.select_one('.day-link').text
    date3 = day3.select_one('.date').text
    month3 = day3.select_one('.month').text

    day4 = html.find_all('div', 'main')[3]
    dday4 = day4.select_one('.day-link').text
    date4 = day4.select_one('.date').text
    month4 = day4.select_one('.month').text

    day5 = html.find_all('div', 'main')[4]
    dday5 = day5.select_one('.day-link').text
    date5 = day5.select_one('.date').text
    month5 = day5.select_one('.month').text

    day6 = html.find_all('div', 'main')[5]
    dday6 = day6.select_one('.day-link').text
    date6 = day6.select_one('.date').text
    month6 = day6.select_one('.month').text

    day7 = html.find_all('div', 'main')[6]
    dday7 = day7.select_one('.day-link').text
    date7 = day7.select_one('.date').text
    month7 = day7.select_one('.month').text

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(
        text=f'{today_day}, {today_date} {today_month} (сьогодні)', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(
        text=f'{dday2}, {date2} {month2} (завтра)', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(
        text=f'{dday3}, {date3} {month3} (післязавтра)', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(
        text=f'{dday4}, {date4} {month4}', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(
        text=f'{dday5}, {date5} {month5}', callback_data=5))
    markup.add(telebot.types.InlineKeyboardButton(
        text=f'{dday6}, {date6} {month6}', callback_data=6))
    markup.add(telebot.types.InlineKeyboardButton(
        text=f'{dday7}, {date7} {month7}', callback_data=7))
    bot.send_message(
        message.chat.id, text='Виберіть день на який хочете подивитись погоду', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == '1':

        min_temp = html.select_one('.temperature .min').text.strip()
        max_temp = html.select_one('.temperature .max').text.strip()
        now_temp = html.select_one('.imgBlock .today-temp').text.strip()
        descr = html.select_one('.wDescription .description').text.strip()
        humidity = html.find_all('td', 'cur')[5].text
        wind = html.find_all('td', 'cur')[6]
        wind_dir = wind.select('div.wind')
        wind_direction = wind_dir[0].get('data-tooltip').split()[0][:-1]
        prob_of_prec = html.find_all('td', 'cur')[7].text
        bot.answer_callback_query(
            callback_query_id=call.id, text="You check some button!")

        answer = (
            f'Cьогодні протягом дня очікується температура: {min_temp}; {max_temp}\n{descr}\nТемпература на даний момент: {now_temp}\nВологість: {humidity}%\nВітер: {wind_direction}, {wind.text}м/с\nЙмовірність опадів: {prob_of_prec}%')
    elif call.data == '2':
        day = html.find_all('div', 'main')[1]
        w_status = day.select_one('.weatherIco')
        weather = w_status.get('title').lower()
        temperature = day.select_one('.temperature').find_all('span')
        min_t = temperature[0].text
        max_t = temperature[1].text
        answer = (
            f'Завтра протягом дня очікується {weather} з  мінімальною {min_t} та максимальною {max_t} температурою')
    elif call.data == '3':
        day = html.find_all('div', 'main')[2]
        w_status = day.select_one('.weatherIco')
        weather = w_status.get('title').lower()
        temperature = day.select_one('.temperature').find_all('span')
        min_t = temperature[0].text
        max_t = temperature[1].text
        answer = (
            f'Післязавтра протягом дня очікується {weather} з  мінімальною {min_t} та максимальною {max_t} температурою')
    elif call.data == '4':
        day = html.find_all('div', 'main')[3]
        date = (day.select_one('.date').text +
                ' ' + day.select_one('.month').text)
        w_status = day.select_one('.weatherIco')
        weather = w_status.get('title').lower()
        temperature = day.select_one('.temperature').find_all('span')
        min_t = temperature[0].text
        max_t = temperature[1].text
        answer = (
            f'{date} протягом дня очікується {weather} з  мінімальною {min_t} та максимальною {max_t} температурою')
    elif call.data == '5':
        day = html.find_all('div', 'main')[4]
        date = (day.select_one('.date').text +
                ' ' + day.select_one('.month').text)
        w_status = day.select_one('.weatherIco')
        weather = w_status.get('title').lower()
        temperature = day.select_one('.temperature').find_all('span')
        min_t = temperature[0].text
        max_t = temperature[1].text
        answer = (
            f'{date} протягом дня очікується {weather} з  мінімальною {min_t} та максимальною {max_t} температурою')
    elif call.data == '6':
        day = html.find_all('div', 'main')[5]
        date = (day.select_one('.date').text +
                ' ' + day.select_one('.month').text)
        w_status = day.select_one('.weatherIco')
        weather = w_status.get('title').lower()
        temperature = day.select_one('.temperature').find_all('span')
        min_t = temperature[0].text
        max_t = temperature[1].text
        answer = (
            f'{date} протягом дня очікується {weather} з  мінімальною {min_t} та максимальною {max_t} температурою')
    elif call.data == '7':
        day = html.find_all('div', 'main')[6]
        date = (day.select_one('.date').text +
                ' ' + day.select_one('.month').text)
        w_status = day.select_one('.weatherIco')
        weather = w_status.get('title').lower()
        temperature = day.select_one('.temperature').find_all('span')
        min_t = temperature[0].text
        max_t = temperature[1].text
        answer = (
            f'{date} протягом дня очікується {weather} з  мінімальною {min_t} та максимальною {max_t} температурою')
    bot.send_message(call.message.chat.id, answer)


bot.polling()
