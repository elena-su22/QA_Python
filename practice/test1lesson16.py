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
                createteam = '''CREATE TABLE `team` (`название команды` VARCHAR(50),`id` INT PRIMARY KEY,`количество участников` INT CHECK(`количество участников`<11));'''
                cursor.execute(createteam)
            except Exception as ex:
                print(ex)
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)

### Задача: Проверить существует ли таблица good_category. Если таблица существует найти все null значения внутри таблицы для КАЖДОГО СТОЛБЦА(id, parent_id, name), если таблицы не существует вывести сообщение соответствующее. Количество NULL значений вывести в качестве представления а также вывести в консоли питона.
### Провести проверку базы данных на наличие null значений. Показать количество null значений в форме представления. good_category
# CREATE VIEW total_null AS
# SELECT
#     (SELECT COUNT(*) FROM good_category WHERE id IS NULL) + (SELECT COUNT(*) FROM good_category WHERE parent_id IS NULL) +(SELECT COUNT(*) FROM good_category WHERE name IS NULL) AS total_null