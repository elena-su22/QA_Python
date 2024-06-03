import re

# email1 = str(input())
# def emailchek(email=email1):
#     if len(email) < 6:
#         return False
#     if '@' not in email:
#         return False
#     listemail = email.split("@")
#     if len(listemail)!=2:
#         return False
#     if len(listemail[0]) < 6:
#         return False
#     listdomen = listemail[1].split(".")
#     if len(listdomen)<2:
#         return False
#     for i in email:
#         if i.isalpha() == False and i.isdigit() == False and i != '.' and i != "-":
#             return False
#         else:
#             return True
# print(emailchek())

# list1 = [1,2,3,4,5]
# list2 = [1,2,2,4,4]
# def uniqlist(list):
#     slist = set(list)
#     if len(list) == len(slist):
#         return True
#     else:
#         return False
# print(uniqlist(list1))
# print(uniqlist(list2))


user_database = {
    "user1@example.com": {'name':'User', 'password': 'Qwe12343r'},
    "user2@example.com": {'name':'Vasya', 'password': 'Qwe12343r'},
    "user3@example.com": {'name':'Petya', 'password': 'Qwe12343r'},
    "user4@example.com": {'name':'Sereja', 'password': 'Qwe12343r'},
}
def func():
    x = True
    while x:
        name1 = input('имя')
        if name1 == 'exit':
            x = False
            break
        email1 = input('почта')
        pass1 = input('пароль')
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern,email1):
            print('Почта содержит недопустимые символы')
            continue
        parts = email1.split('@')
        if len(parts[0])<4:
            print('Почта слишком короткая')
            continue
        for i,ii in user_database.items():
            if i == email1:
                print('Почта уже зарегистрированна')
                continue
        if len(name1) < 2:
            print('Имя слишком короткое')
            continue
        patternname = r'^[a-zA-Z-]{2,}$'
        if not re.match(patternname,name1):
            print('Имя содержит недопустимые символы')
            continue
        if len(pass1) < 7:
            print('Пароль слишком короткий')
            continue
        has_low = False
        has_up = False
        has_dig = False
        for i in pass1:
            if i.islower():  
                    has_low = True
            elif i.isupper():
                    has_up = True
            elif i.isdigit():
                    has_dig = True
        if has_low == False or has_up == False or has_dig == False:
            print('Пароль содержать в себе как минимум 1 заглавную букву, 1 цифру, 1 знак')
            continue
        print('Пользователь зарегистрирован')
        user_database[email1] = {'name':name1, 'password':pass1}
        base = input('Хотите увидеть базу? Да/Нет')
        if base == 'Да':
            print(user_database)
func()