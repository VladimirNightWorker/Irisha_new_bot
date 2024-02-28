from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


main_btn = [
    [KeyboardButton(text='Запись на услугу')],
]
main_kb = ReplyKeyboardMarkup(keyboard=main_btn, resize_keyboard=True)


# follow_kbb = [
#     [InlineKeyboardButton(text='Записаться', callback_data='follow')]
# ]
# follow_kb = InlineKeyboardMarkup(inline_keyboard=follow_kbb)

share_number_phone = KeyboardButton(text='Дать свой номер телефона', request_contact=True)
share_number_phone_kb = ReplyKeyboardMarkup(keyboard=[[share_number_phone]], resize_keyboard=True, input_field_placeholder='Поделиться телефоном', one_time_keyboard=True)

select_service_btn = [
    [InlineKeyboardButton(text='Коррекция бровей', callback_data='correction')],
    [InlineKeyboardButton(text='Коррекция и окрашивание', callback_data='corr_paint')],
    [InlineKeyboardButton(text='Коррекция и Долговременная укладка', callback_data='corr_styling')],
    [InlineKeyboardButton(text='Коррекция окрашивания и долговременная укладка', callback_data='corr_pain_styl')],
    [InlineKeyboardButton(text='Удаление пушка(Одна зона)', callback_data='del_hair')],
    [InlineKeyboardButton(text='Ламинирование ресниц', callback_data='lash')],
]

select_service_kb = InlineKeyboardMarkup(inline_keyboard=select_service_btn)

# sel_or_back_btn = [
#     [KeyboardButton(text='Записаться на эту услугу')],
#     [KeyboardButton(text='Посмотреть другие услуги')]
# ]
# sell_or_back_kb = ReplyKeyboardMarkup(keyboard=sel_or_back_btn, resize_keyboard=True, input_field_placeholder='Сделайте выбор')

select_serv_btn = [
    [InlineKeyboardButton(text='Выбрать дату и время для записи на эту услугу к мастеру?', callback_data='sel_date')]
]

select_serv_kb = InlineKeyboardMarkup(inline_keyboard=select_serv_btn)


# date_serv_btn = [
#     [InlineKeyboardButton(text='date_serv_btn', callback_data='date_serv_btn')]
# ]
# date_serv_kb = InlineKeyboardMarkup(inline_keyboard=date_serv_btn)


select_time_serv_btn = [
    [InlineKeyboardButton(text='9:00', callback_data='9:00')],
    [InlineKeyboardButton(text='11:30', callback_data='11:30')],
    [InlineKeyboardButton(text='13:30', callback_data='13:30')],
    [InlineKeyboardButton(text='15:30', callback_data='15:30')]
]
select_time_serv_kb = InlineKeyboardMarkup(inline_keyboard=select_time_serv_btn)


confirm_or_cancel_btn = [
    [InlineKeyboardButton(text='Подтвердить запись', callback_data='confirm_service')],
    [InlineKeyboardButton(text='Отменить запись', callback_data='cancel_service')]
]
confirm_or_cancel_kb = InlineKeyboardMarkup(inline_keyboard=confirm_or_cancel_btn)

after_btn = [
    [KeyboardButton(text='Просмотр моей записи')],
    [KeyboardButton(text='Адрес студии')],
    [KeyboardButton(text='Инфо о мастере')],
    [KeyboardButton(text='Контакты')],
]

after_kb = ReplyKeyboardMarkup(keyboard=after_btn, resize_keyboard=True)


my_sel_serv_btn = [
    [InlineKeyboardButton(text='Отменить запись', callback_data='cancel_service')]
]
my_sel_serv_kb = InlineKeyboardMarkup(inline_keyboard=my_sel_serv_btn)
