from aiogram import Bot, Router, F, types
from aiogram.filters import CommandStart, Command, or_f
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery, ReplyKeyboardRemove, FSInputFile

from keyboards.user_kb import share_number_phone_kb, select_service_kb, select_serv_kb, select_time_serv_kb, confirm_or_cancel_kb, main_kb, after_kb, my_sel_serv_kb
from db.db import insert_data_db, insert_user_phone, sel_serv, select_time, select_date_serv, show_info, confirm_service, cancel_service, check_time
from lexicon.lexicon_ru import services

from datetime import datetime
from aiogram_calendar import SimpleCalendar, SimpleCalendarCallback, DialogCalendar, DialogCalendarCallback, get_user_locale


user_router = Router()

@user_router.message(CommandStart())
async def start_command(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    date = datetime.now()
    phone = None
    await insert_data_db(user_id, first_name, last_name, username, phone, date)
    await message.answer(text='''<b>Привет, красотка🌸</b>

Меня зовут Ирина, я сертифицированный мастер бровист , страстно увлеченный искусством ухода за бровями)
Моя цель- помочь Вам достичь идеальной формы и выразительности ваших бровей)

В моей работе я использую только качественные продукты, чтобы обеспечить оптимальный результат и долговременный эффект. 
Моя цель- не только создать красивые брови, но и предоставить Вам приятное и комфортное обслуживание.

<u>Жду Вас за красивыми бровями</u> 😻
📲89025385699 <i>Viber/ What’s App/ Telegram</i>
<a href="https://vk.com/fomina_brow">Загляни в мою группу ВК</a>''', reply_markup=share_number_phone_kb)
    await message.answer('Для продолжения жми кнопку внизу...')
    
# simple calendar usage - filtering callbacks of calendar format
@user_router.callback_query(SimpleCalendarCallback.filter())
async def process_simple_calendar(callback_query: CallbackQuery, callback_data: CallbackData):
    calendar = SimpleCalendar(
        locale=await get_user_locale(callback_query.from_user), show_alerts=True
    )
    calendar.set_dates_range(datetime(2024, 2, 1), datetime(2024, 12, 31))
    selected, date = await calendar.process_selection(callback_query, callback_data)
    # print(date)
    # print(datetime.now())
    if selected:
        if date >= datetime.now():
            await select_date_serv(user_id=callback_query.from_user.id, select_date=date.strftime("%d/%m/%Y"))
            await callback_query.message.answer(
                f'Вы выбрали: {date.strftime("%d/%m/%Y")}',
                reply_markup=select_time_serv_kb
            )
        else:
            await callback_query.message.answer(text='К сожалению машину времени еще не изобрели =)\nВыберите актуальную дату:', reply_markup=select_serv_kb)
        
@user_router.callback_query()
async def follow_on_uslugi(callback_query: CallbackQuery, bot: Bot):
    if callback_query.data == 'follow':
        await bot.send_message(chat_id=callback_query.from_user.id, text='Its a 1st callback')
        await callback_query.answer("It's a callback", show_alert=True)

    if callback_query.data == 'correction':
        await sel_serv(user_id=callback_query.from_user.id, sel_serv='Коррекция бровей')
        await bot.send_message(chat_id=callback_query.from_user.id, text='Коррекция\n400 ₽', reply_markup=select_serv_kb)
        await callback_query.answer(f"Коррекция\n400 ₽\n{services.get('correction')}", show_alert=True)
    if callback_query.data == 'corr_paint':
        await sel_serv(user_id=callback_query.from_user.id, sel_serv='Коррекция и окрашивание')
        await bot.send_message(chat_id=callback_query.from_user.id, text='Коррекция и окрашивание\nReady in 1 hour\n750 ₽', reply_markup=select_serv_kb)
        await callback_query.answer(f"Коррекция и окрашивание\nReady in 1 hour\n750 ₽\n{services.get('correction')}", show_alert=True)
    if callback_query.data == 'corr_styling':
        await sel_serv(user_id=callback_query.from_user.id, sel_serv='Коррекция и Долговременная укладка')
        await bot.send_message(chat_id=callback_query.from_user.id, text='Коррекция и Долговременная укладка\nReady in 1 hour\n1,000 ₽', reply_markup=select_serv_kb)
        await callback_query.answer(f"Коррекция и Долговременная укладка\nReady in 1 hour\n1,000 ₽\n{services.get('correction')}", show_alert=True)
    if callback_query.data == 'corr_pain_styl':
        await sel_serv(user_id=callback_query.from_user.id, sel_serv='Коррекция окрашивания с ДУ')
        await bot.send_message(chat_id=callback_query.from_user.id, text='Коррекция окрашивания с ДУ\nReady in 2 hours\n1,400 ₽', reply_markup=select_serv_kb)
        await callback_query.answer(f"Коррекция окрашивания с ДУ\nReady in 2 hours\n1,400 ₽\n{services.get('correction')}", show_alert=True)
    if callback_query.data == 'del_hair':
        await sel_serv(user_id=callback_query.from_user.id, sel_serv='Удаление пушка')
        await bot.send_message(chat_id=callback_query.from_user.id, text='Удаление пушка\nReady in 30 minutes\n200 ₽', reply_markup=select_serv_kb)
        await callback_query.answer(f"Удаление пушка\nReady in 30 minutes\n200 ₽\n{services.get('correction')}", show_alert=True)
    if callback_query.data == 'lash':
        await sel_serv(user_id=callback_query.from_user.id, sel_serv='Ламинирование ресниц')
        await bot.send_message(chat_id=callback_query.from_user.id, text='Ламинирование ресниц\nReady in 30 minutes\n1100 ₽', reply_markup=select_serv_kb)
        await callback_query.answer(f"Ламинирование ресниц\nReady in 30 minutes\n1100 ₽\n{services.get('correction')}", show_alert=True)

    if callback_query.data == 'sel_date':
        await bot.send_message(chat_id=callback_query.from_user.id, text='Выберите дату записи:', reply_markup=await SimpleCalendar(locale=await get_user_locale(callback_query.from_user)).start_calendar())

    if callback_query.data == '9:00':
        await select_time(user_id=callback_query.from_user.id, time_serv='9:00')
        if await check_time(user_id=callback_query.from_user.id):
            await callback_query.message.answer('Извините, это время уже занято\nВыберите другое время!', reply_markup=select_time_serv_kb)
        else:
            usluga = await show_info(user_id=callback_query.from_user.id)
            await bot.send_message(chat_id=callback_query.from_user.id, 
                               text=f'Ваша запись: {usluga}', reply_markup=confirm_or_cancel_kb)
    if callback_query.data == '11:30':
        await select_time(user_id=callback_query.from_user.id, time_serv='11:30')
        if await check_time(user_id=callback_query.from_user.id):
            await callback_query.message.answer('Извините, это время уже занято\nВыберите другое время!', reply_markup=select_time_serv_kb)
        else:
            usluga = await show_info(user_id=callback_query.from_user.id)
            await bot.send_message(chat_id=callback_query.from_user.id, 
                               text=f'Ваша запись: {usluga}', reply_markup=confirm_or_cancel_kb)
    if callback_query.data == '13:30':
        await select_time(user_id=callback_query.from_user.id, time_serv='13:30')
        if await check_time(user_id=callback_query.from_user.id):
            await callback_query.message.answer('Извините, это время уже занято\nВыберите другое время!', reply_markup=select_time_serv_kb)
        else:
            usluga = await show_info(user_id=callback_query.from_user.id)
            await bot.send_message(chat_id=callback_query.from_user.id, 
                               text=f'Ваша запись: {usluga}', reply_markup=confirm_or_cancel_kb)
    if callback_query.data == '15:30':
        await select_time(user_id=callback_query.from_user.id, time_serv='15:30')
        if await check_time(user_id=callback_query.from_user.id):
            await callback_query.message.answer('Извините, это время уже занято\nВыберите другое время!', reply_markup=select_time_serv_kb)
        else:
            usluga = await show_info(user_id=callback_query.from_user.id)
            await bot.send_message(chat_id=callback_query.from_user.id, 
                               text=f'Ваша запись: {usluga}', reply_markup=confirm_or_cancel_kb)

    if callback_query.data == 'confirm_service':
        usluga = await show_info(user_id=callback_query.from_user.id)
        await callback_query.answer(text=f'Буду рада видеть Вас в салоне, по адресу: Балтахинова 17, 206 офис.\n{usluga[0][1]+usluga[0][2]}', show_alert=True)
        await bot.send_message(chat_id=callback_query.from_user.id, text=f'Буду рада видеть Вас в салоне, по адресу: Балтахинова 17, 206 офис.\n{usluga[0][1]+usluga[0][2]}', reply_markup=after_kb)
        await confirm_service(user_id=callback_query.from_user.id)

    if callback_query.data == 'cancel_service':
        await bot.send_message(chat_id=callback_query.from_user.id, text='Запись успешно отменена.\nМожете выбрать другую услугу и дату, для этого нажмите соответствующую кнопку внизу)', reply_markup=main_kb)
        await cancel_service(user_id=callback_query.from_user.id)

@user_router.message(F.contact)
async def update_phone(message: types.Message):
    photo = FSInputFile(path='service.jpg')
    await insert_user_phone(phone=message.contact.phone_number, id=message.from_user.id)
    await message.answer('Номер телефона успешно добавлен в Базу Данных', reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo=photo)
    await message.answer(text='Ознакомьтесь со списком услуг:', reply_markup=select_service_kb)
    
@user_router.message(F.text.lower() == 'запись на услугу')
async def sell_servic(message: types.Message):
    await message.answer(text='Ознакомьтесь со списком услуг:', reply_markup=select_service_kb)

@user_router.message(F.text.lower() == 'просмотр моей записи' or Command(commands='my_service'))
async def my_select_service(message: types.Message):
    usluga = await show_info(message.from_user.id, )
    await message.answer(text=f'Мои записи:\nУслуга: {usluga[0]}\nДата: {usluga[1]}\nВремя: {usluga[2]}', reply_markup=my_sel_serv_kb)
