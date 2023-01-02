#1
# a = int(input("Введите число: "))
# b = int(input("Введите число:"))

# if a<b:
#     print(a)
# else:
#     print(b)

# #2
# name = input("Введите имя: ")
# age = int(input("Введите возраст: "))

# if age >= 18:



#while and for - циклы
#break - условие заканьчиваетя 


# string = "Hellow"
# for i in string:
#     print(1)

# # int is not iter object

# for i in range(12):#- 
#     print(i)


# list ={1, 2, 3, 4, 5, 6}
# dict1 = {
#     "name":"Adm",
#     "pop":"LL", 
#     "age": 22
# } 

# for i in dict1.keys():
#     print(i)

# i = 1000
# while i>1:
#     i-=100 # i = -100
#     print(i)


# i = 1000
# while i >= 0:
#     print("Hellow")
#     print(i)


# list1 = [1, 2, 3, 4, 5, 6, 7, 8,]
# list2 = []
# list3 = []

# for i in list1:
#     if i % 2 == 0:
#         list2.append(i)
#     else:
#         list3.append(i)
# print(list2)
# print(list3)


# i =10
# while i != 0:
#     i-=2
#     print(i)
#     if i == 5:
#         break



# lis1 = [1, 2, 3, 4, 5, 6, 7, 774]

# for item in lis1:
#     if item == 3:
#         print(item)
#         break
#     else:
#         continue



# for i in range(5):
#     print("*")

# for i in range(5):
#     print("*", end= "")
#     for j in range(3):
#         print("*", end="\n ")
#         for k in range(2):
#             print("*", end="\n")
#             for d in range(2):
#                 print("*", end = "")


#0
# list1 = ["aple", "banana", "cherry"]

# while True:
#     a = input("Фрукт: ")
#     list1.append(a)
#     if len(list1) == 8:
#         print(list1)
#         print(list1[3], list1[4], list1[5], list1[6], list1[7])
#         break


 #1       
# a = 1000

# while a > 0:
#     a -=7
#     print("pain")
#     if a < 0:
#         print("alive")


#2


# for a in range(4):
#     print("hellow Pyrthon")

# a = "hellow Pyrthon"

# cou = 0
# while cou<4:
#     print(a)
#     cou+=1


#3
# a = "hellow Python"
# w = "Hellow Java"
# nam = 0
# while nam<4:
#     print(a)
#     nam+=1
# else:
#     print(w)


# for i in range(6):
#     for j in range(6-i):
#         print(" ",end="")
#     for k in range(i+1):
#         print("*",end=" ")
#     print("\n")



# for i in range(1):
#     print("*".rjust(3, " "))
#     for j in range(1):
#         print("***".center(5, " "))
#     for k in range(1):
#         print("*".center(5, "*"))
#     for q in range(1):
#         print("***".center(5, " "))
#     for l in range(1):
#         print("*".rjust(3, " "))
    

# baza = {
#     "login1" : {
#         "phone" : "+77071232323",
#         "name" : "Jon",
#         "balance" : 9999, 
#         "password" : "123qweasd"
#     }, 
#     "login2" :{
#         "phone" : "+77776883221",
#         "name" : "Nik",
#         "balance" : 9350, 
#         "password" : "123QWEASD"
#     }
# }

# m = None

# while True:
#     if m is None:
#         print(" Добро пожаловать! ")
#         a = int(input("""
#         1 - Зарегистрироваться
#         2 - Авторизоваться
#         3 - Перевод баланса
#         4 - Список пользователей
#         5 - Информация
#         6 - Номер телефона   
#         7 - Выйти
#         Выберите операцию:
#     """))
#     if a == 1:
#         login = input("Введите логин: ")
#         name = input("Введите имя: ")
#         phone = input("Введите номер телефона: ")
#         password = int(input("Введите пароль: "))
#         password1 = int(input("Введите пароль повторно: "))
#         while password != password1 or len(password) < 8:
#             password = input("Создать пароль не меньше 8:")
#             password1 = input("Повтарите свой пароль")
#         else:
#             baza.update({
#                 login: {
#                     "phone" : phone,
#                     "name" : name,
#                     "balance" : 1000,
#                     "password" : password
#                 }
#             })
#             print(baza)
   
#     elif a == 2:
#         if m is None:
#             login = input("Введите логин: ")
#             password = int(input("Введите пароль: "))
#             if login in baza.keys and password == baza[login]["password"]:
#                 print("Вы авторизованы")
#             else:
#                 print("Неверный логин или пароль")

#     elif a ==3:
#         if m is not None:
#                 sum = str(input("Введите сумму: "))
#                 if sum < baza[login]["balance"]:
#                     logbalans = input("Введите логин получателя: ")
#                     if logbalans in baza[login]:
#                         sum += logbalans["balance"]
#                         print(logbalans["balance"])

#                     else:
#                         print("Такого логина не существует")
                
#                 else:
#                     print("Сумма перевода превышает Ваш текуший баланс")


#     elif a == 4:
#         login = input("Введите логин: ")
#         password = int(input("Введите пароль: "))
#         if login in baza.keys and password == baza[login]["password"]:
#             print(baza[login]["name"])
#         else:
#             print("Неверный логин или пароль")


#     elif a == 5:
#         login = input("Введите логин: ")
#         password = int(input("Введите пароль: "))
#         if login in baza.keys() and password == baza[login]["password"]:
#             print(baza.keys())
#         else:
#             print("Неверный логин или пароль")

#     elif a == 6:
#         login = input("Введите логин: ")
#         password = int(input("Введите пароль: "))
#         if login in baza.keys() and password == baza[login]["password"]:
#             print(baza[login]["phone"])
#         else:
#             print("Неверный логин или пароль")

#     elif a ==7:
#         print("До скорой встречи")
#         break


