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
            # try:
            #     createteam = '''CREATE TABLE `team` (`название команды` VARCHAR(50),`id` INT PRIMARY KEY,`количество участников` INT CHECK(`количество участников`<11));'''
            #     cursor.execute(createteam)
            # except Exception as ex:
            #     print(ex)
            # pasteinfo = '''INSERT INTO `team` (`название команды`,`id`,`количество участников`) VALUES ("Пантеры",1,10),("Тигры",2,9),("Львы",3,7),("Ягуары",4,3),("Леопарды",5,2),("Гепарды",6,3),("Рыси",7,8),("Ягуарунди",8,6),("Пумы",9,2),("Барсы",10,8)'''
            # cursor.execute(pasteinfo)
            # connection.commit()
            # found5= '''SELECT * FROM `team` WHERE `количество участников`>5'''
            # cursor.execute(found5)
            # getlines = cursor.fetchall()
            # if not getlines:
            #     print('Нет больших команд')
            # else:
            #     for i in getlines:
            #         print(i)
            # try:
            #     foundAB= '''CREATE VIEW `veiw_user`
            #         AS SELECT `id`,`name`,`email`,`password`,`reg_date` FROM `user`
            #         WHERE YEAR(`reg_date`) = 2018 AND `name` LIKE "А%" OR `name` LIKE "Б%" OR `name` LIKE "% А%" OR `name` LIKE "% Б%"'''
            #     cursor.execute(foundAB)
            # except:
            #     None
            try:
                foundottea= '''CREATE VIEW `veiw_good_notea` AS SELECT
                    `id`,`category_id`,`name`,`count`,`price` FROM `good`
                    WHERE `name` NOT LIKE "Айс Ти%"'''
                cursor.execute(foundottea)
            except Exception as ex:
                print(ex)
            updateinfo = '''UPDATE `veiw_good_notea` SET `name` = "Текила", `count` = 100,`price` = 100 WHERE `id` = 7'''
            cursor.execute(updateinfo)
            connection.commit()
            updateinfo = '''UPDATE `veiw_good_notea` SET `name` = "Вода", `count` = 100,`price` = 100 WHERE `id` = 8'''
            cursor.execute(updateinfo)
            connection.commit()
            updateinfo = '''UPDATE `veiw_good_notea` SET `name` = "Жидкий азот", `count` = 100,`price` = 100 WHERE `id` = 9'''
            cursor.execute(updateinfo)
            connection.commit()
            updateinfo = '''UPDATE `veiw_good_notea` SET `name` = "Яд", `count` = 100,`price` = 100 WHERE `id` = 10'''
            cursor.execute(updateinfo)
            connection.commit()
            updateinfo = '''UPDATE `veiw_good_notea` SET `name` = "Грязь", `count` = 100,`price` = 100 WHERE `id` = 11'''
            cursor.execute(updateinfo)
            connection.commit()
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)

