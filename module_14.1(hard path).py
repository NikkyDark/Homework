import sqlite3

print('Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов."')
print('Цель: освоить основные команды языка SQL и использовать их в коде используя SQLite3.')
print('Задача "Первые пользователи":')
print('Студент Бобачeв Никита Дмитриевич.')
print('Дата: 20.03.2025г.')
thanks = 'Благодарю за внимание :-)'
print()

file_name = 'not_telegram.db'
full_table = ''
base_names = ''
connection = sqlite3.connect(file_name)
cursor = connection.cursor()
quantity = 11


def create_a_database(base_name, username, email, age, balance):
    global base_names
    global connection
    global cursor
    global full_table
    print(f'Создаем базу данных, и если она существует то открываем ее: {file_name}')
    base_names = base_name
    full_table = username, email, age, balance
    print(f'Создаем список таблиц - Пользователь: {base_name}, поля: {username}, {email}, {age}, {balance}')

    set_file_name = (f'''CREATE TABLE IF NOT EXISTS {base_name}(
                    id INTEGER PRIMARY KEY,
                    {username} TEXT NOT NULL,
                    {email} TEXT NOT NULL,
                    {age} INTEGER NOT NULL,
                    {balance} INTEGER NOT NULL);
    )
''')
    cursor.execute(set_file_name)


def fill_in_the_table(set_name, set_email, set_dog, set_age, set_balance):
    global full_table
    global base_names
    global connection
    global cursor
    for i in range(1, quantity):
        j = str(i)
        set1 = str(f'INSERT INTO {base_names} ({full_table[0]}, {full_table[1]}, {full_table[2]}, '
                   f'{full_table[3]}) VALUES (?, ?, ?, ?)')
        set2 = str(f"{set_name}{j}")
        set3 = str(f'{set_email}{j}{set_dog}')
        set4 = int(set_age)
        set5 = int(set_balance)
        cursor.execute(f'{set1}', (f'{set2}', f'{set3}', set4, set5))
        set_age += 10
    print(f'Заполнили список {quantity - 1}ю записями:')
    display()


def update_balance(quantity_b, plus_b):
    global base_names
    global connection
    global cursor
    for bal in range(1, quantity):
        if not (bal - 1) % quantity_b:
            set1 = str(f'UPDATE {base_names} SET {full_table[3]} = {plus_b} WHERE  id = ?')
            cursor.execute(set1, (bal,))
    print(f'Обноволили баланс у каждой {quantity_b}й записи начиная с первой на {plus_b} руб')
    display()


def delete_table(quantity_t):
    global base_names
    global connection
    global cursor
    for dell in range(1, quantity):
        if not (dell - 1) % quantity_t:
            set1 = str(f'DELETE FROM {base_names} WHERE id = ?')
            cursor.execute(set1, (dell,))
            print(f'Удалили {quantity_t}ю запись в таблице начиная с 1й записи')
            display()


def old_users(set_old):
    global full_table
    global base_names
    global connection
    global cursor
    set1 = str(f'SELECT {full_table[0]}, {full_table[2]}, {full_table[3]} FROM {base_names} '
               f'WHERE {full_table[2]} != ?')
    cursor.execute(f'{set1}', (set_old,))
    users = cursor.fetchall()
    print(f'Выборка по записям, у которых возраст не равен {set_old}:')
    for old in users:
        print(f'Имя пользователя: {old[0]}| Почта {old[1]}| Возраст: {old[2]}| Баланс: {old[3]} руб.')


def display():
    global base_names
    cursor.execute(f'SELECT * FROM {base_names}')
    users = cursor.fetchall()
    for user in users:
        print(user)


def finish():
    global connection
    global cursor
    connection.commit()
    cursor.close()


if __name__ == '__main__':
    create_a_database('Users', 'username', 'email',
                      'age', 'balance')
    # create_a_database('Users_2024', 'Имя', 'email',
    #                   'Возраст', 'Баланс')
    print()
    fill_in_the_table('User', 'example',
                      '@gmail.com', 10, 1000)
    print()
    update_balance(2, 500)
    print()
    delete_table(3)
    print()
    old_users(60)
    finish()
    print()
    print(thanks)
