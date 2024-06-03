import re
import string

# stud1 = {'name':'Lena', 'grades':[4,5,3,5]}
# stud2 = {'name':'Alex', 'grades':[5,5,3,5]}
# stud3 = {'name':'Ilya', 'grades':[3,5,3,4]}
# stud4 = {'name':'Olga', 'grades':[4,4,3,5]}
# liststudent = [stud1, stud2, stud3, stud4]
# def filterstudent(listst = liststudent):
#     bestlist = []
#     for i in listst:
#         sumgrades = 0
#         for ii in i['grades']:
#             sumgrades += ii
#         midgrades = sumgrades/4
#         if midgrades > 4:
#             bestlist.append(i['name'])
#     return bestlist      
# print(filterstudent())

# str1 = 'Hello, hello, world!'
# def worldfreq(str1 = str1):
#     textwithoutpunct = re.sub(r'[^\w\s]', '', str1)
#     listtext = textwithoutpunct.split()
#     #вместо 2х предыдущих строк можно listtext = re.findall(r'\b\w+\b', text), будут убраны знаки препинания и поделен текст по пробелам
#     dict1 = {}
#     for i in listtext:
#         i1 = i.lower()
#         if i1 in dict1:
#             dict1[i1] += 1
#         else:
#             dict1[i1] = 1
#     return dict1
# print(worldfreq())

# logs = [
#     '192.168.0.1 /home',
#     '192.168.0.1 /about',
#     '192.168.0.2 /home',
#     '192.168.0.1 /home',
#     '192.168.0.2 /contact',
#     '192.168.0.1 /about',
# ]
# dictlog = {}
# def loganalyze(logs=logs):
#     for i in logs:
#         listlog = i.split('/')
#         if listlog[0] not in dictlog:
#             dictlog[listlog[0]] = [listlog[1]]
#         else:
#             list1 = dictlog[listlog[0]]
#             list1.append(listlog[1])
#             setlist1 = set(list1)
#             list1 = list(setlist1)
#             dictlog[listlog[0]] = list1
#     for i in dictlog:
#         v1 = len(dictlog[i])
#         dictlog[i] = v1
#     return dictlog
            
# print(loganalyze())




# strphone = '+79112223344'
# def phonecheck(phone=strphone):
#     if len(phone) != 12:
#         return False
#     elif phone[0] != '+':
#         return False
#     phone = phone[1:]
#     for i in phone:
#         if i.isdigit() == False:
#             return False
#         else:
#             return True    
# print(phonecheck())

# text1 = 'Hello? world!'
# len1 = len(text1)




# def validtextlen(textx = text1, lenx = len1):
#     if len(textx) <= lenx:
#         return True
#     else:
#         return False
# print(validtextlen(text1,17))
# print(validtextlen(text1,7))
# print(validtextlen())

# email1 = '1wedf23@eee.com'
# def validemail(emailx = email1):
#     emailpattern = r'^\w+\d+\@\w+\.\w+$'
#     if re.match(emailpattern,emailx):
#         return True
#     else:
#         return False

# print(validemail())

#passpattern = r'^\+\d+\w+$'

pass1 = '+124fgd'

def validpass(passx=pass1):
    passpattern = r'^[+]?(\d+\w+)$'
    if re.match(passpattern,passx):
        return True
    else:
        return False
    
print(validpass())