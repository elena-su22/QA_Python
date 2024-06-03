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
            pasteinfo = '''INSERT INTO `good` (`id`,`category_id`,`name`,`count`,`price`) VALUES (2000,7,"Oleg",200,32)'''
            cursor.execute(pasteinfo)
            connection.commit()
            try:
                testexist = '''SELECT * FROM `good` WHERE `name` LIKE "Oleg"'''
                cursor.execute(testexist)
                print('Yes')
            except Exception as ex:
                print('No Oleg')
                print(ex)
                
    finally:
        connection.close()
except Exception as ex: 
    print('Connection rufus')
    print(ex)
 