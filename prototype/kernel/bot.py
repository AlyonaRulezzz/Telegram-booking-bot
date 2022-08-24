# -*- coding: utf-8 -*-
import sqlite3
from telegram.utils.request import Request

from telegram import Bot
from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.utils.request import Request

# кнопки
button_role_adm = 'АДМ'
button_role_student = 'Студент'
button_role_applicant = 'Интенсивист'

button_action_booking = 'Бронирование'
button_action_status = 'Просмотр статуса'
button_action_cancel = 'Отмена бронирования'

button_campus_kzn = 'Казань'
button_campus_nsb = 'Новосибирск'
button_campus_msk = 'Москва'

button_room = 'Переговорка'
button_sport = 'Спортивный инвертарь'
button_game = 'Настольная игра'
button_kitchen = 'Кухня'

button_orion = 'Orion'
button_erehwon = 'Erehwon'
button_liberty = 'Liberty'
button_veranda = 'Veranda'
button_cassiopeia = 'Cassiopeia'
button_oasis = 'Oasis'
button_pulsar = 'Pulsar'
button_quazar = 'Quazar'

button_room_1_nsb = 'Зал Шафран'
button_room_2_nsb = 'Переговорка 2 НСБ'
button_room_3_nsb = 'Переговорка 3 НСБ'

button_room_1_msk = 'Атриум'
button_room_2_msk = 'Переговорка 2 МСК'
button_room_3_msk = 'Переговорка 3 МСК'

button_pingpong = 'Пинг-понг'
button_minifootball = 'Минифутбол'
button_playstation = 'Playstation'

button_munchkin = 'Манчкин'
button_imaginarium = 'Имаджинариум'

button_kitchen_2_floor = 'Кухня 2-ого этажа'
button_kitchen_3_floor = 'Кухня 3-его этажа'

button_9h = '9 ч'
button_12h = '12 ч'
button_14h = '14 ч'
button_15h = '15 ч'
button_17h = '17 ч'
button_18h = '18 ч'
button_19h = '19 ч'
button_21h = '21 ч'

button_positive = 'Одобрить'
button_negative = 'Отклонить'

flag_obj = 0
flag_positive = 0
flag_negative = 0

# функции
def log_error(f):

    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'Ошибка: {e}')
            raise e

    return inner

@log_error
def button_role_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Выберите следующее действие:',
        reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_action_booking), KeyboardButton(text=button_action_status), KeyboardButton(text=button_action_cancel),
            ],
        ],
        resize_keyboard=True,
        ),   
    )

@log_error
def button_action_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Выберите кампус:',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
            [
                KeyboardButton(text=button_campus_kzn), KeyboardButton(text=button_campus_nsb), KeyboardButton(text=button_campus_msk),
            ],
        ],
        resize_keyboard=True,
        ),
    )

@log_error
def button_campus_adm_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Выберите объект бронирования:',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
            [
                KeyboardButton(text=button_room), KeyboardButton(text=button_sport), KeyboardButton(text=button_game), KeyboardButton(text=button_kitchen),
            ],
        ],
        resize_keyboard=True,
        ),
    )

@log_error
def button_campus_student_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Выберите объект бронирования:',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
            [
                KeyboardButton(text=button_room), KeyboardButton(text=button_sport), KeyboardButton(text=button_game),
            ],
        ],
        resize_keyboard=True,
        ),
    )

@log_error
def button_campus_applicant_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Выберите объект бронирования:',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
            [
                KeyboardButton(text=button_room),
            ],
        ],
        resize_keyboard=True,
        ),
    )

@log_error
def button_obj_room_kzn_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Выберите переговорку в Казани<3:',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
            [
                KeyboardButton(text=button_orion), KeyboardButton(text=button_erehwon), KeyboardButton(text=button_liberty), KeyboardButton(text=button_veranda),
            ],
            [
                KeyboardButton(text=button_cassiopeia), KeyboardButton(text=button_oasis), KeyboardButton(text=button_pulsar), KeyboardButton(text=button_quazar),
            ],
        ],
        resize_keyboard=True,
        ),
    )

@log_error
def button_obj_room_nsb_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Выберите переговорку в Новосибирске=):',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
            [
                KeyboardButton(text=button_room_1_nsb), KeyboardButton(text=button_room_2_nsb), KeyboardButton(text=button_room_3_nsb),
            ],
        ],
        resize_keyboard=True,
        ),
    )

@log_error
def button_obj_room_msk_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Выберите переговорку в Москве=):',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
            [
                KeyboardButton(text=button_room_1_msk), KeyboardButton(text=button_room_2_msk), KeyboardButton(text=button_room_3_msk),
            ],
        ],
        resize_keyboard=True,
        ),
    )

@log_error
def button_obj_sport_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Выберите спортинвентарь:',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
            [
                KeyboardButton(text=button_pingpong), KeyboardButton(text=button_minifootball), KeyboardButton(text=button_playstation),
            ],
        ],
        resize_keyboard=True,
        ),
    )
    return update.message.text

@log_error
def button_obj_game_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Выберите настольную игру:',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
            [
                KeyboardButton(text=button_munchkin), KeyboardButton(text=button_imaginarium),
            ],
        ],
        resize_keyboard=True,
        ),
    )

@log_error
def button_obj_kitchen_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Выберите кухню:',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
            [
                KeyboardButton(text=button_kitchen_2_floor), KeyboardButton(text=button_kitchen_3_floor),
            ],
        ],
        resize_keyboard=True,
        ),
    )


@log_error
def button_time_begin_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Выберите время начала:',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
            [
                KeyboardButton(text=button_9h), KeyboardButton(text=button_12h), KeyboardButton(text=button_15h), KeyboardButton(text=button_18h),
            ],
        ],
        resize_keyboard=True,
        ),
    )

@log_error
def button_time_end_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Выберите время окончания:',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
            [
                KeyboardButton(text=button_14h), KeyboardButton(text=button_17h), KeyboardButton(text=button_19h), KeyboardButton(text=button_21h),
            ],
        ],
        resize_keyboard=True,
        ),
    )

@log_error
def button_end_student_and_applicant_book_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Спасибо за заявку! Ожидайте ответа!',
        reply_markup=ReplyKeyboardRemove(),
    )

@log_error
def button_end_student_and_applicant_cancel_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Заявка отменена!',
        reply_markup=ReplyKeyboardRemove(),
    )

@log_error
def button_end_adm_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Оформлено!',
        reply_markup=ReplyKeyboardRemove(),
    )


@log_error
def button_book_status_student_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=items,
        reply_markup=ReplyKeyboardRemove(),
    )

@log_error
def button_book_status_adm_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text= items + 'Выберите функцию:',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
            [
                KeyboardButton(text=button_positive), KeyboardButton(text=button_negative),
            ],
        ],
        resize_keyboard=True,
        ),
    )

@log_error
def button_book_status_positive_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Введите id заявки для одобрения:',
        reply_markup=ReplyKeyboardRemove(),
    )
@log_error
def button_book_status_positive_approve_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Заявка одобрена!',
    )

@log_error
def button_book_status_negative_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Введите id заявки для отклонения:',
        reply_markup=ReplyKeyboardRemove(),
    )
@log_error
def button_book_status_negative_rejection_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Заявка отклонена!',
    )



@log_error
def message_handler(update: Update, context: CallbackContext):
    db = sqlite3.connect('school.db')
    c = db.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS users (
        userid int64,
        name text,
        login text,
        role text,
        campus text
    )""")
    db.commit()
    db.close()
    
    global user
    global action
    global campus
    global obj
    global object_exact
    global object_id
    global time_begin
    global time_end
    global booking_id
    global items
    global result
    global flag_obj
    global flag_positive
    global flag_negative

    # выбор роли
    text = update.message.text
    if text == button_role_adm:
        user = button_role_adm
        print('user =', user)
    if text == button_role_student:
        user = button_role_student
        print('user =', user)
    if text == button_role_applicant:
        user = button_role_applicant
        print('user =', user)
    if text == button_role_adm or text == button_role_student or text == button_role_applicant:
        return button_role_handler(update=update, context=context)
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_role_adm), KeyboardButton(text=button_role_student), KeyboardButton(text=button_role_applicant),
            ],
        ],
        resize_keyboard=True,
    )
    # выбор действия
    if text == button_action_booking:
        action = button_action_booking
        print('action =', action)
    if text == button_action_status:
        action = button_action_status
        print('action =', action)
    if text == button_action_cancel:
        action = button_action_cancel
        print('action =', action)
    if text == button_action_booking or text == button_action_status or text == button_action_cancel:
        return button_action_handler(update=update, context=context)
    # выбор кампуса
    if text == button_campus_kzn:
        campus = button_campus_kzn
        print('campus =', campus)
    if text == button_campus_nsb:
        campus = button_campus_nsb
        print('campus =', campus)
    if text == button_campus_msk:
        campus = button_campus_msk
        print('campus =', campus)
    if text == button_campus_kzn or text == button_campus_nsb or text == button_campus_msk:
        # просмотр статуса
        if action == button_action_status:
            db = sqlite3.connect('school.db')
            c = db.cursor()
            if user == button_role_adm:
                c.execute("SELECT * FROM books WHERE obj_campus = '{}'".format(campus))
            if user == button_role_student or user == button_role_applicant:
                c.execute("SELECT * FROM books WHERE userid = %d" % update.message.from_user.id)
            items = c.fetchall()
            result = ''
            for item in items:
                result += str(item[0]) +' ' + str(item[1]) +' ' +str(item[2]) +' ' +item[3] +' ' +item[4] + ' ' +item[5] + ' ' + item[6] + ' ' + item[7] + ' ' + item[8] + '\n';
            items = result
            db.commit()
            db.close()
            if user == button_role_student or user == button_role_applicant:
                return button_book_status_student_handler(update=update, context=context)
            if user == button_role_adm:
                return button_book_status_adm_handler(update=update, context=context)
        # добавление юзера в бд
        this_user = (update.message.from_user.id, 'login', update.message.from_user.first_name, user, campus)
        db = sqlite3.connect('school.db')
        c = db.cursor()
        query = "SELECT * FROM users WHERE userid = %d" % update.message.from_user.id
        c.execute(query)
        data = c.fetchall()
        db.commit()
        if data is None or data == []:
            c.execute("""INSERT INTO users VALUES(?, ?, ?, ?, ?);""", this_user)
            db.commit()
        db.close()
        if user == button_role_adm:
            return button_campus_adm_handler(update=update, context=context)
        if user == button_role_student:
            return button_campus_student_handler(update=update, context=context)
        if user == button_role_applicant:
            return button_campus_applicant_handler(update=update, context=context)
    # выбор объекта
    if text == button_room:
        obj = button_room
        print('obj =', obj)
    if text == button_sport:
        obj = button_sport
        print('obj =', obj)
    if text == button_game:
        obj = button_game
        print('obj =', obj)
    if text == button_kitchen:
        obj = button_kitchen
        print('obj =', obj)
    # переговорки в Казани
    if text == button_room and campus == button_campus_kzn:
        flag_obj = 1
        return button_obj_room_kzn_handler(update=update, context=context)
    # переговорки в Новосибирске
    if text == button_room and campus == button_campus_nsb:
        flag_obj = 1
        return button_obj_room_nsb_handler(update=update, context=context)
    # переговорки в Москве
    if text == button_room and campus == button_campus_msk:
        flag_obj = 1
        return button_obj_room_msk_handler(update=update, context=context)
    # спортивный инвентарь
    if text == button_sport:
        flag_obj = 1
        return button_obj_sport_handler(update=update, context=context)
    # настольные игры
    if text == button_game:
        flag_obj = 1
        return button_obj_game_handler(update=update, context=context)
    # кухни
    if text == button_kitchen:
        flag_obj = 1
        return button_obj_kitchen_handler(update=update, context=context)
    # изменение АДМ статуса заявок
    # одобрение
    if text==button_positive and user == button_role_adm:
        flag_positive = 1
        return button_book_status_positive_handler(update=update, context=context)
    if flag_positive == 1:
        db = sqlite3.connect('school.db')
        c = db.cursor()
        c.execute("UPDATE books SET status = 'Одобрена' WHERE book_id = %d" %int(text))
        db.commit()
        db.close()
        flag_positive = 0
        return button_book_status_positive_approve_handler(update=update, context=context)
    # отклонение
    if text==button_negative and user == button_role_adm:
        flag_negative = 1
        return button_book_status_negative_handler(update=update, context=context)
    if flag_negative == 1:
        db = sqlite3.connect('school.db')
        c = db.cursor()
        c.execute("UPDATE books SET status = 'Отклонена' WHERE book_id = %d" %int(text))
        db.commit()
        db.close()
        flag_negative = 0
        return button_book_status_negative_rejection_handler(update=update, context=context)
    # сохранение object_id
    db = sqlite3.connect('school.db')
    c = db.cursor()
    object_exact = text
    if flag_obj == 1:
        print(object_exact)
        c.execute("SELECT obj_id FROM objects WHERE name ='{}'".format(object_exact))
        object_id = c.fetchone()[0]
        flag_obj = 0
        print('object_id', object_id)
    db.commit()
    db.close()
    # время начала бронирования
    if text == button_room_1_msk or text == button_room_2_msk or text == button_room_3_msk or text == button_room_1_nsb or text == button_room_2_nsb or text == button_room_3_nsb or text == button_orion  or text == button_erehwon or text == button_liberty or text == button_veranda or text == button_cassiopeia or text == button_oasis or text == button_pulsar or text == button_quazar or text == button_pingpong or text == button_minifootball or text == button_playstation or text == button_munchkin or text == button_imaginarium or text == button_kitchen_2_floor or text == button_kitchen_3_floor:
        return button_time_begin_handler(update=update, context=context)
    # время окончания бронирования
    if text == button_9h or text == button_12h or text == button_15h or text == button_18h:
        time_begin = text
        return button_time_end_handler(update=update, context=context)
    # заявка принята
    if text == button_14h or text == button_17h or text == button_19h or text == button_21h:
        time_end = text
        # сохранение object_name
        db = sqlite3.connect('school.db')
        c = db.cursor()
        c.execute("SELECT name FROM objects WHERE obj_id= %d;" % object_id)
        object_name = str(c.fetchone()[0])
        print('object_name ', object_name)
        db.commit()
        db.close()

        print(object_id)
        booking_id = update.message.from_user.id + object_id
        if user == button_role_adm:
            this_book = (booking_id, update.message.from_user.id, object_id, update.message.from_user.first_name, object_name, campus, time_begin, time_end, 'оформлена')
        if user == button_role_student or user == button_role_applicant:
            this_book = (booking_id, update.message.from_user.id, object_id, update.message.from_user.first_name, object_name, campus, time_begin, time_end, 'на рассмотрении')
        # добавить бронь в бд
        if action == button_action_booking:
            db = sqlite3.connect('school.db')
            c = db.cursor()
            c.execute("""INSERT INTO books VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);""", this_book)
            db.commit()
            db.close()
        # удалить бронь из бд
        if action == button_action_cancel:
            db = sqlite3.connect('school.db')
            c = db.cursor()
            c.execute("DELETE FROM books WHERE book_id= %d;" % booking_id)
            db.commit()
            db.close()
            
        if user == button_role_adm:
            return button_end_adm_handler(update=update, context=context)
        if user == button_role_student or user == button_role_applicant:
            if action == button_action_booking:
                return button_end_student_and_applicant_book_handler(update=update, context=context)
            if action == button_action_cancel:
                return button_end_student_and_applicant_cancel_handler(update=update, context=context)
    # default
    update.message.reply_text(
        text='Привет! Требуется авторизация! Выбери роль, ' + update.message.from_user.first_name,
        reply_markup=reply_markup,
    )

@log_error
def main():
    print('Start')

    req = Request(
        connect_timeout=2.5,
    )
    bot = Bot(
        request=req,
        # token = '5768136631:AAES0r9go3XWExZ77YrhHXT0ew1XuJJLjU8',
        token='5401171801:AAHyaij1XEPmiFTi1YCDw0dWVbyLS7re8Qw'# Ксюшин токен
    )

    updater =Updater(
        bot=bot,
        use_context=True,
    )
    print(updater.bot.get_me())

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()

    print('Finish')

if __name__ == '__main__':
    main()
