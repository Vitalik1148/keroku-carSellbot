import telebot
from telebot import types
import ch

bot = telebot.TeleBot('5302347371:AAH4LbBjVwKNJBlK47sXUFXpqg-LL8eP3qs')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Добро пожаловать, <b>{message.from_user.first_name}</b>\nВас приветствует виртуальный бот по продаже авто автосалона ВАЗ\nЧем я могу вам помочь?'
    photo = open('photos/photo.png', 'rb')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Машины в наличии', 'Задать вопрос❓')
    bot.send_photo(message.chat.id, photo, caption=mess, parse_mode='html', reply_markup=markup)
    sti = open('stickers/AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)


@bot.message_handler(content_types=['text'])
def two(message):
    if message.text == "Машины в наличии":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Nissan', 'Mazda', 'Kia', 'Hyundai', 'Ford')
        markup.row('Домой')
        bot.send_message(message.chat.id, 'Какая марка машины вас интересует?', reply_markup=markup)
    elif message.text == "Задать вопрос❓":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Где вы находитесь?', 'Как с вами связаться?', 'О нас', 'Видео салона')
        markup.row('Время работы?', 'Как добраться?', 'Фото автосалона')
        markup.row('Домой')
        bot.send_message(message.chat.id, 'Что вас интересует?', reply_markup=markup)
    if message.text == "Где вы находитесь?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Домой', 'Назад')
        bot.send_location(message.chat.id, 55.899573, 37.542303, reply_markup=markup)
        bot.send_message(message.chat.id, '<b>Наш автосалон находится по адресу:</b> г. Москва, Дмитровское шоссе, д.157, стр.4\n\nВыше вы можете быстро перейти на карты, что бы построить маршрут👆🏼', parse_mode='html')
    elif message.text == "Как с вами связаться?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Домой', 'Назад')
        bot.send_message(message.chat.id, '<b>Телефоны:</b>\n\n8 (800) 1000-157 <ins>(Бесплатно по России)</ins>\n8 (495) 488-71-57\n\n<b>Электронная почта:</b>\n\ninfo@saloncentr.ru', reply_markup=markup, parse_mode='html')
    elif message.text == "Время работы?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Домой', 'Назад')
        bot.send_message(message.chat.id, '<b>Режим работы:</b>\n\nБудние дни:\nС 9:00 - 21:00\n\nСуббота и Воскресенье:\nС 8.00 - 21.00', reply_markup=markup, parse_mode='html')
    elif message.text == "Как добраться?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Домой', 'Назад')
        photo = open('photos/contacts-car.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=markup)
        bot.send_message(message.chat.id, '<b>Бесплатное маршрутное такси от метро "Алтуфьево</b>\n\n1. Серая ветка, станция метро "Алтуфьево" - первый вагон из центра, выходите на станции Алтуфьево, поднимаетесь по ступенькам, после стеклянных дверей налево поворачиваете и к выходу\nна улицу опять налево.\n2. При выходе из метро, справа увидите зеленое здание. Прямо за ним Вас ждет бесплатный транспорт к автосалону "Центральный" (перед магазином "Перекрёсток").\n\n<b>Общественным транспортом</b>\n\n<b>от метро "Алтуфьево"</b>\n\n· Серая ветка, станция метро "Алтуфьево".\n· Когда будете ехать к станции "Алтуфьево" - садитесь в первый вагон поезда (ближе к машинисту), выходите на станции Алтуфьево,\n'
                                          'поднимаетесь по ступенькам, после стеклянных дверей налево поворачиваете и к выходу на улицу опять налево.\n· При выходе из метро справа будет зеленое здание с надписью "ЛИГА СТАВОК".\n· За этим зданием находится бесплатный транспорт к автосалону "Центральный" (перед магазином "Перекрёсток").\n· Вы также можете доехать на маршрутных такси 994, 571, 352 или автобусы 774, 92, 928, 284.\n· Проехать 6 остановок, на 7-ой выйти - называется остановка "Дмитровское шоссе,155".\n· От остановки "Дмитровское шоссе,155" вернуться назад в сторону области 60 метров.\n\n<b>от метро "Селигерская"</b>\n\n· Салатовая ветка, станция метро "Селигерская".\n· Выйти из метро - '
                                          'последний вагон из центра, налево в направлении эскалатора, после турникетов налево, и направо в сторону выхода в город до автобусной остановки (находится за выходом из метро).\n· На автобусах № 763, 63, 994, т78, 763к следовать 7 остановок до остановки "Дмитровское шоссе, 155".\n· Далее по подземному пешеходному переходу пересечь Дмитровское шоссе и следовать вдоль него в сторону МКАДа 100 метров.', parse_mode='html')
    elif message.text == "Фото автосалона":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Домой', 'Назад')
        media = [types.InputMediaPhoto('https://www.saloncentr.ru/assets/images/centr/contacts/pn-001-629b410513accb8af3de32c616fe7d719ac72f7a8504e9cc9244f3efa647ec5f.jpg'),
                 types.InputMediaPhoto('https://www.saloncentr.ru/assets/images/centr/contacts/pn-002-7f65e8ea6fc835c8aa0cd717a552f30cbba649f12a03e51dfe22090d234c487a.jpg'),
                 types.InputMediaPhoto('https://www.saloncentr.ru/assets/images/centr/contacts/pn-003-4a65d3655fb88d7f43560f215cde15d7cbfff8062a6b9eac78a04925f501ac63.jpg'),
                 types.InputMediaPhoto('https://www.saloncentr.ru/assets/images/centr/contacts/pn-004-be1ce477864268cb4d2c82b17fb04d31b4539f8c6a3312f124f7aa6069fbedeb.jpg'),
                 types.InputMediaPhoto('https://www.saloncentr.ru/assets/images/centr/contacts/1-f3441b5a87709c5a9dbb20dd9339d35932d26ba28b176d3993c140a8b44ccc05.jpg'),
                 types.InputMediaPhoto('https://www.saloncentr.ru/assets/images/centr/contacts/2-b9eaacb2cc0e32bf3f49bc422bcfc9000af4574ed5b542b0a443aff8249b4b23.jpg'),
                 types.InputMediaPhoto('https://www.saloncentr.ru/assets/images/centr/contacts/3-5ff248f7095ae6a029003d637155573b5fee887fdea0e8ed093753d49d22e83e.jpg'),
                 types.InputMediaPhoto('https://www.saloncentr.ru/assets/images/centr/contacts/pn-007-492a5a3688ecb28e7fd906b45d1cab1e3338bfb0daa85dbb14a943ac0837cc51.jpg'),
                 types.InputMediaPhoto('https://www.saloncentr.ru/assets/images/centr/contacts/pn-008-db3f722dc19a1e1dfadf491732d0097ea4ac55ca0b58acc5bfe6d91135aa324c.jpg'),
                 types.InputMediaPhoto('https://www.saloncentr.ru/assets/images/centr/contacts/pn-010-df8775ff38d82f0dbf2578e9e4a5086927f15deb20689efc38469506bdcc8ceb.jpg')]
        bot.send_media_group(message.chat.id, media)
    # Nissan
    if message.text == "Nissan":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Nissan Terrano', 'Nissan Qashqai', 'Nissan X-Trail', 'Nissan Murano')
        markup.row('Назад к выбору марки', 'Домой')
        bot.send_message(message.chat.id, 'Какая модель машины вас интересует?', reply_markup=markup)
    if message.text == "Nissan Terrano":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Домой', 'Назад к выбору модели Nissan')
        markup.row('Купить')
        photo = open('photos/largecard_1-lednikovyy-belyy_1642334951.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=ch.Nissan_Terrano, parse_mode='html', reply_markup=markup)
    elif message.text == "Nissan Qashqai":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Домой', 'Назад к выбору модели Nissan')
        markup.row('Купить')
        photo = open('photos/largecard_2-belyy-perlamutr_1642334565.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=ch.Nissan_Qashqai, parse_mode='html', reply_markup=markup)
    elif message.text == "Nissan X-Trail":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Домой', 'Назад к выбору модели Nissan')
        markup.row('Купить')
        photo = open('photos/largecard_6-belyy-perlamutr_1642334801.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=ch.Nissan_XTrail, parse_mode='html', reply_markup=markup)
    elif message.text == "Nissan Murano":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Домой', 'Назад к выбору модели Nissan')
        markup.row('Купить')
        photo = open('photos/largecard_1-belyy-perlamutr_1642335041.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=ch.Nissan_Murano, parse_mode='html', reply_markup=markup)
    if message.text == "Назад к выбору модели Nissan":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Nissan Terrano', 'Nissan Qashqai', 'Nissan X-Trail', 'Nissan Murano')
        markup.row('Назад к выбору марки', 'Домой')
        bot.send_message(message.chat.id, 'Какая модель машины вас интересует?', reply_markup=markup)
    # Мазда
    elif message.text == "Mazda":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Mazda CX-9', 'Mazda CX-5', 'Mazda 6 Седан')
        markup.row('Назад к выбору марки', 'Домой')
        bot.send_message(message.chat.id, 'Какая модель машины вас интересует?', reply_markup=markup)
    if message.text == "Mazda 6 Седан":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Домой', 'Назад к выбору модели Mazda')
        markup.row('Купить')
        photo = open('photos/largecard_1-arctic-white-cle_1642335179.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=ch.Mazda6_Sedan, parse_mode='html', reply_markup=markup)
    elif message.text == "Mazda CX-9":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Домой', 'Назад к выбору модели Mazda')
        markup.row('Купить')
        photo = open('photos/largecard_1-snowflake-white-pearl_1642335803.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=ch.Mazda9_CX, parse_mode='html', reply_markup=markup)
    elif message.text == "Mazda CX-5":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Домой', 'Назад к выбору модели Mazda')
        markup.row('Купить')
        photo = open('photos/largecard_1-arctic-white-cle_1642335552.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=ch.Mazda5_CX, parse_mode='html', reply_markup=markup)
    if message.text == "Назад к выбору модели Mazda":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Mazda CX-9', 'Mazda CX-5', 'Mazda 6 Седан')
        markup.row('Назад к выбору марки', 'Домой')
        bot.send_message(message.chat.id, 'Какая модель машины вас интересует?', reply_markup=markup)
    # Audi
    elif message.text == "Kia":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('KIA Picanto', 'KIA Rio', 'KIA Cerato 2021', 'Kia Rio Х 2021')
        markup.row('Назад к выбору марки', 'Домой')
        bot.send_message(message.chat.id, 'Какая модель машины вас интересует?', reply_markup=markup)
    if message.text == "KIA Picanto":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Домой', 'Назад к выбору модели Kia')
        markup.row('Купить')
        photo = open('photos/largecard_1-clear-white_1644590700.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=ch.KIA_Picanto, parse_mode='html', reply_markup=markup)
    elif message.text == "KIA Rio":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Домой', 'Назад к выбору модели Kia')
        markup.row('Купить')
        photo = open('photos/largecard_1-crystal-white_1644587685.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption=ch.KIA_Rio, parse_mode='html', reply_markup=markup)
    elif message.text == "KIA Cerato 2021":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Домой', 'Назад к выбору модели Kia')
        markup.row('Купить')
        photo = open('photos/largecard_1-clear-white_1644591227.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=ch.KIA_Cerato21, parse_mode='html', reply_markup=markup)
    elif message.text == "Kia Rio Х 2021":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Домой', 'Назад к выбору модели Kia')
        markup.row('Купить')
        photo = open('photos/largecard_1-crystal-white_1644590032.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption=ch.Kia_Rio_X21, parse_mode='html', reply_markup=markup)
    if message.text == "Назад к выбору модели Kia":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('KIA Picanto', 'KIA Rio', 'KIA Cerato 2021', 'Kia Rio Х 2021')
        markup.row('Назад к выбору марки', 'Домой')
        bot.send_message(message.chat.id, 'Какая модель машины вас интересует?', reply_markup=markup)
    # не изменяемые кнопки
    elif message.text == "Назад к выбору марки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Nissan', 'Mazda', 'Kia', 'Hyundai', 'Ford')
        markup.row('Домой')
        bot.send_message(message.chat.id, 'Какая марка машины вас интересует?', reply_markup=markup)
    elif message.text == "Домой":
        mess = f'Добро пожаловать, <b>{message.from_user.first_name}</b>\nВас приветствует виртуальный бот по продаже авто автосалона ВАЗ\nЧем я могу вам помочь?'
        photo = open('photos/photo.png', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Машины в наличии', 'Задать вопрос❓')
        bot.send_photo(message.chat.id, photo, caption=mess, parse_mode='html', reply_markup=markup)
    if message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Где вы находитесь?', 'Как с вами связаться?', 'О нас', 'Видео салона')
        markup.row('Время работы?', 'Как добраться?', 'Фото автосалона')
        markup.row('Домой')
        bot.send_message(message.chat.id, 'Что вас интересует?', reply_markup=markup)


bot.polling(none_stop=True)
