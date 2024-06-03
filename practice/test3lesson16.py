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
            foundorder24= '''SELECT `id`,`status_id`,`user_id`,YEAR(`creation_date`) FROM `order` WHERE `status_id` LIKE "2" OR `status_id` LIKE "4" '''
            cursor.execute(foundorder24)
            getlines = cursor.fetchall()
            for i in getlines:
                print(i)
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)



# Взять таблицу order и вывести в консоль питона всех строки для которых status_id будет 2 и 4 , и дату представить в формате (ГОД) без месяца времени и дня.