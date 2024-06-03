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
            pasteinfo = '''DELETE FROM `good` WHERE `name` LIKE "Человек"'''
            cursor.execute(pasteinfo)
            connection.commit()
            testexist = '''SELECT * FROM `good` WHERE `name` LIKE "Человек"'''
            cursor.execute(testexist)
            exist = cursor.fetchall()
            if exist == ():
                print('No Человек')
            else:
                print('Человек still exist')        
    finally:
        connection.close()
except Exception as ex: 
    print('Connection rufus')
    print(ex)
 