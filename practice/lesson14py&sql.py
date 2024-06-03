import mysql.connector

try:
    config = {
        'host' : 'localhost',
        'user' : 'elenasu221',
        'password': 'JMETMz6r-rVDQ8WL',
        'database': 'elenasu221'}
    print('connection is successfull')
except Exception as ex:
    print('no connection')
    print(ex)

#код только для создания файлов, для остального другие методы
# with open('elenasu221.sql','r',encoding='utf-8') as file:
#     #sql_script = file.read()
#     #print(sql_script)
#     line1 = file.readlines()
#     for i in line1:
#         if "CREATE TABLE `user`" in i:
#             print(i)

