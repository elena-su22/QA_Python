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
                testexist = 'SELECT * FROM `good`'
                cursor.execute(testexist)
                print('Yes')
            except Exception as ex:
                print('No table')
                print(ex)    
    finally:
        connection.close()
except Exception as ex: 
    print('Connection rufus')
    print(ex)
 