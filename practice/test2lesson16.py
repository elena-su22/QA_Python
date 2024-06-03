import pymysql
import pymysql.cursors
from main_config_base import host, user, password, db_name

try:
    connection = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor
)
    print('succsess')
    print('#' * 30)
    try:
        with connection.cursor() as cursor:
            try:
                testexist = 'SELECT * FROM `user`'
                cursor.execute(testexist)
                print('Yes')
            except Exception as ex:
                print('No table')
                print(ex)
            try:
                foundgmailuser= '''CREATE VIEW `veiw_gmail_user`
                    AS SELECT `id`,`name`,`email`,`password`,`reg_date` FROM `user`
                    WHERE `email` LIKE "%@gmail%" AND `reg_date` BETWEEN "2017-01-02" AND "2017-08-31"'''
                cursor.execute(foundgmailuser)
            except:
                None
            foundgmailuser= '''SELECT * FROM `veiw_gmail_user` LIMIT 10'''
            cursor.execute(foundgmailuser)
            getlines = cursor.fetchall()
            for i in getlines:
                print(i)
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)


# Берем таблицу user проверяем что она есть, если она есть, в таблице надо найти всех пользователей с gmail за период 2017 года с  2 января по сентябрь.
# Поля таблицы это id name email password reg_date
# Всех этих пользователей вывести в новое представление, а также первых 10 вывести в консоли питона.
