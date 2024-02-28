from aiogram.types import BotCommand


main_menu = [
    BotCommand(command='/start', description='Пере/Запуск бота'),
    BotCommand(command='/help', description='Помощь'),
    BotCommand(command='/my_service', description='Просмотр моих записей'),
    BotCommand(command='/about', description='Обо мне'),
    BotCommand(command='/contacts', description='Мои контакты'),
]
