import sqlite3


class Db:
    async def __init__(self) -> None:
        self.conn = sqlite3.connect('user.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Users(
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         user_id TEXT NOT NULL,
                         first_name TEXT NOT NULL,
                         last_name TEXT,
                         username TEXT,
                         user_phone TEXT,
                         select_services TEXT,
                         date_to_serv TEXT,
                         time_serv TEXT,
                         confirm TEXT,
                         start_date VARCHAR)''')


async def create_user_db():
    services_list = [
        ('Удаление пушка', '200 ₽'), 
        ('Коррекция бровей', '400 ₽'), 
        ('Коррекция и Окрашивание', '750 ₽'),  
        ('Коррекция и Долговременная укладка', '1000 ₽'), 
        ('Коррекция, Окрашивание и Долговременная укладка', '1400 ₽'), 
        ('Ламинирование ресниц', '1100 ₽')
        ]
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                user_id TEXT NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT,
                username TEXT,
                user_phone TEXT,
                select_services TEXT,
                date_to_serv TEXT,
                time_serv TEXT,
                confirm TEXT,
                start_date VARCHAR)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Services
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   services TEXT,
                   services_price TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Recycle
                   (id INTEGER PRIMARY KEY,
                   user_id TEXT,
                   select_service1 TEXT,
                   select_service2 TEXT,
                   select_service3 TEXT,
                   select_service4 TEXT)''')

    cursor.executemany("INSERT INTO Services (services, services_price) VALUES (?, ?)", (services_list))
    
    connection.commit()
    connection.close()

async def insert_data_db(user_id, first_name, last_name, username, user_phone, date):
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()
    # user = cursor.execute('SELECT * FROM Users WHERE user_id == {key}'.format(key=user_id)).fetchone()
    user = cursor.execute(f'SELECT * FROM Users WHERE user_id == {user_id}').fetchone()
    if not user:
        try:
            cursor.execute("INSERT INTO Users (user_id, first_name, last_name, username, user_phone, start_date) VALUES (?, ?, ?, ?, ?, ?)", 
                           (user_id, first_name, last_name, username, user_phone, date))
            connection.commit()
        except sqlite3.Error as ex:
            print("Что-то пошло не так:'(\n", ex)
        finally:
            connection.close()

async def insert_user_phone(phone, id):
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()

    try:
        cursor.execute("UPDATE Users set user_phone = ? where user_id = ?",
                       (phone, id))

        connection.commit()
    except sqlite3.Error as er:
        print('Ошибка обновления данных, номер телефона\n', er)
    finally:
        connection.close()
        
async def select_service_user1(service, id):
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()

    try:
        cursor.execute("UPDATE Users set VALUES select_service = ? where user_id = ?",
                       (service, id))

        connection.commit()
    except sqlite3.Error as er:
        print('Ошибка обновления данных, номер телефона\n', er)
    finally:
        connection.close()


async def select_service_user2(time_service, id):
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()

    try:
        cursor.execute("UPDATE Users set time_service = ? where user_id = ?",
                       (time_service, id))

        connection.commit()
    except sqlite3.Error as er:
        print('Ошибка обновления данных, номер телефона\n', er)
    finally:
        connection.close()

async def sel_serv(user_id, sel_serv):
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()

    try:
        cur.execute("UPDATE Users set select_services = ? where user_id = ?", 
                    (sel_serv, user_id))
        conn.commit()
    except conn.Error as er:
        print(er)
    finally:
        conn.close()

async def select_date_serv(user_id, select_date):
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()

    try:
        cur.execute("UPDATE Users set date_to_serv = ? where user_id = ?",
                    (select_date, user_id))
        conn.commit()
    except conn.Error as er:
        print(er)
    finally:
        conn.close()

async def select_time(time_serv, user_id):
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()

    try:
        cur.execute("UPDATE Users set time_serv = ? where user_id = ?",
                    (time_serv, user_id))
        conn.commit()
    except conn.Error as er:
        print(er)
    finally:
        conn.close()

async def show_info(user_id):
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()

    try:
        info_db = cur.execute(f"SELECT * FROM Users where user_id = {user_id}").fetchall()
        name_serv = info_db[0][6]
        date_serv = info_db[0][7]
        hour_serv = info_db[0][8]
        return name_serv, date_serv, hour_serv
    except conn.Error as er:
        print(er)
    finally:
        conn.close()

async def confirm_service(user_id):
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()

    try:
        cur.execute(f"UPDATE Users set confirm = 'YES' where user_id = {user_id}")
        conn.commit()
    except conn.Error as er:
        print(er)
    finally:
        conn.close()

async def cancel_service(user_id):
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()

    try:
        cur.execute(f"UPDATE Users set (select_services, date_to_serv, time_serv, confirm) = (?, ?, ?, ?) where user_id = {user_id}",
                    ('NULL', 'NULL', 'NULL', 'NULL'))
        conn.commit()
    except conn.Error as er:
        print(er)
    finally:
        conn.close()

async def check_time(user_id):
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()
    flag = False
    date = cur.execute("SELECT date_to_serv, time_serv FROM Users WHERE confirm = 'YES'").fetchall()
    your_date = cur.execute(f"SELECT date_to_serv, time_serv FROM Users WHERE user_id = {user_id}").fetchall()

    print('date:', date)
    print('your_date:', your_date)

    for date1 in date:
        print(date1)
        if date1 in your_date:
            return True
    return flag
