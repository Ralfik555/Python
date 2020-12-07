# isOk = 1
# print(isOk,type(isOk))
# if isOk:
#     print('TRUE')


#START LAB3
#zad 1
# options = ['load data', 'export data', 'analyze & predict']
# print(options)
# handler = True
# while handler:
#     x = input('what do you want to do? choose number')
#     try:
#         x = int(x)
#         try:
#             print(x,options[x])
#         except:
#             print("there is not such an option")
#     except:
#         print("this is not a number")
#     if not x:
#         handler = False


#zad 1 extended

# options = ['load data', 'export data', 'analyze & predict']
#
# def DisplayOptions(options):
#     for i,option in enumerate(options):
#         print("{} - {}".format(i+1, option))
#     choice = input("choose your option")
#     return choice
#
# choice = 'x'
# while choice:
#     choice = DisplayOptions(options)
#     if choice:
#         try:
#             choice_num = int(choice)
#             try:
#                 print(choice_num,options[choice_num-1])
#             except:
#                 print("there is not such an option")
#                 print('----------------------')
#         except:
#             print("this is not a number")
#             print('----------------------')
#     else:
#         print('FINISH')
#End LAB3

import os

# path = r'/home/rafal/Desktop/Python_projects/py_adv_udemy/Section_1/test'
#os.remove(path)

# if os.path.isfile(path):
#     print('File %s exist' % path)
# else:
#     print('Creating a file %s' % path)
#     open(path,'x').close()
#     print('File %s created' % path)

# result = os.path.isfile(path) or open(path,'x').close()
# print(result)

#KOMENTARZ
#w wypadkach logicznych gdzie mamy or/and, jesli na przyklad mamy OR i pierwsza wartosc jest TRUE to juz drugiej nie sprawdza.
#jesli mamy AND i pierwsza jest FALSE to nie sprawdza juz drugiej bo i bez tego potrafi oszacowac wynik

#START LAB4

path = r'/Section_1/LAB6/LAB4'

def HowManyWords(path):
    file = open(path,"r")
    content = file.read()
    print(len(content.split()))
    return len(content.split())


result = os.path.isfile(path) and HowManyWords(path)




#END LAB4