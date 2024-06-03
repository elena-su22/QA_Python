# try:
#     v1 = int(input('Введи число: '))
#     v2 = int(input('Введи число: '))
#     del1 = v1/v2
#     print(del1)
# except ZeroDivisionError:
#     print('Не дели на 0')
# except ValueError:
#     print('Введи число!')

# try:
#     file1 = open(r'C:\Users\AttekPC\Desktop\lessontx.txt', 'r')
#     print(file1.read())
#     file1.close()
# except FileNotFoundError:
#     print('Файл не найден')

# list1 = [1, 2, 3, 4, 5, 6]
# def defsum(listn=list1):
#     return sum(listn)
# print(defsum())
# def defdel():
#     v1 = int(input('Введи число: '))
#     try:
#         del1 = defsum()/v1
#         return del1
#     except:
#         return 'Ошибка при делении'
# print(defdel())
