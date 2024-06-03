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
            # create_table_students = 'CREATE TABLE `students`(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(32), email VARCHAR(32), age SMALLINT)'
            # cursor.execute(create_table_students)
            # pasteinfo = '''INSERT INTO `students` (`name`,`email`,`age`) VALUES ("Oleg","Oleg@com",32), ("Oleg2","Oleg2@com",22), ("Oleg3","Oleg3@com",12), ("Oleg4","Oleg4@com",42), ("Oleg5","Oleg5@com",52)'''
            # cursor.execute(pasteinfo)
            # connection.commit()
            # showtable = 'SELECT * FROM `students` LIMIT 5'
            # cursor.execute(showtable)
            # getlines = cursor.fetchall()
            # for i in getlines:
            #     print(i)
            create_view_good='''CREATE VIEW veiw_good AS SELECT `id`,`category_id`,`name`,`count`,`price` FROM `good` WHERE `name` LIKE "%Айс Ти%"'''
            cursor.execute(create_view_good)
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)
 