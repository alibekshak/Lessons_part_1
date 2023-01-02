# #dict - изменяемы тип данных
# #set 

# # di = {}#dic
# # f = dict()#dic

# n = {"name" : "Ali",
#     "age" : 3
# }
# # print(n)
# # print(n["name"], n["age"])

# # print(n.keys())# -  выводит ключи 
# # print(n.values())# - выводит значения 
# # print(n.items())# - выводит все 

# # print(n.pop("name"))

# # n.popitem()#удаляет последний элмент 
# # print(n)



# # f ={"fff" : "ddd"}
# # n.update(f)# обьединяет словари 
# # print(n)

# # a = n.fromkeys("d", 123)
# # print(a)


# m = {"x" : 4, "y" :4 }
# # m.setdefault("z", 123)# - добавляет ключь и значение 
# # print(m)



# # m[1]= 1234# добавляет новые значения в словарь 
# # print(n)

# n=m.copy()# - копирует данные в переменной n
# print(n)







# set  - убирает дубликаты
# a = {"name", 123, 44.3, "name"}
# print(a)


# print(list(a))# периобазует в list []



# b = frozenset([1, 2, "ee"])# -не изменяемый set
# print(b)


# aa = {1, True, "fffa", 442}
# bb = {"name", True, 12}
# cc = {33, 44, "name", 442}

# # print(cc.isdisjoint(bb)) # - есть ли схожие элементы  True, False 

# # print(aa.union(bb)) # - сливает 2 seta и удалит похожие элименты

# # print(aa.intersection(cc))# - показывает одинаковые значения 

# # print(aa.difference(cc))# - смотрит какие значения нет в cc

# print(aa.discard(True)) # - 

#0
# a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13 ,14, 15}

# a.discard(7)
# print(a)

#1 and 2
# aa = {"fff", True}
# bb = {"fff", False, 333, True}

# print(bb.intersection(aa))

# print(bb.difference(aa))


#3 
# qq ={12, True, "ffs", 33.6, "fdsf"}
# qq.add(7)
# print(qq)

# qq.pop()
# print(qq)


#4
# ff = {"borsh": 180, "lagman": 100}
# ff["besh"]=120
# print(ff)

# ff["lagman"]=150
# print(ff)

# ff.pop("borsh")
# print(ff)


#5 
# ar = {
#     "drink":["Fanta", "Cola", "Sprite"]
# }

# print(ar)


#7
# dicti = {
    
# }
# name = input("Name: ")
# password = str(input("Password: "))

# name1 = input("Name: ")
# password1 = str(input("Password: "))

# name2 = input("Name: ")
# password2 = str(input("Password: "))

# dicti[name]= password
# dicti[name1]= password1
# dicti[name2]= password2
# print(dicti)


#11
# a = ["Суринам", "Аргентина", "Куба", "Суринам"]

# a = set(a)

# a = list(a)
# print(a)


#101
# a = input("Вещи: ")
# b = input("Вещи: ")
# c = input("Вещи: ")
# d = input("Вещи: ")
# e = input("Вещи: ")
# f = input("Вещи: ")
# suitcase = []
# suitcase.append(a)
# suitcase.append(b)
# suitcase.append(c)
# suitcase.append(d)
# suitcase.append(e)
# suitcase.append(f)


# if len(suitcase) >= 5:
#     print(' Больше 5 нельзя')
#     print(suitcase)
#     suitcase.pop(5)
#     print(suitcase)



# h = []
# for i in range(1,7):
#     h.append(i)
# a = h.pop(5), print(h) if len(h) >= 5 else print('Все хоршо')


print("""
    Для успешной регистрации введите:
    Логин
    Пароль
    Имя
    Дату рождения
""")

login = input("Логин: ")
password = str(input("Пароль: "))
name = input("Имя: ")
birthday = input("День рождения: ")
num =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
simple_password = ['123','12312321', '1234567890', '0987654321','0001','000001','000001','09876543211234567890']
baza = {  }

if login.isalpha() and len(password) >= 8 and name != num and "." in birthday and  simple_password != password:
    baza["login"]=login
    baza["password"]=password
    baza["name"]=name
    baza["birthday"]=birthday
    print(baza)
    print("Для аторизации введите логин и пороль.")
    login1 = input("Login: ")
    password1 = str(input("Password: "))
    if login1 in baza["login"] and password1 in baza["password"]:
        print("Вы успешно авторизовались")
        print("Если вы хотите сменить имя, нажмите 1.\
            Для изменения даты рождения, нажмите 2")
        a = int(input("Выберите цифру: "))

        if a == 1:
            print("Для смены имени введите логин и пороль.")
            login1 = input("Login: ")
            password1 = str(input("Password: "))
            if login1 in baza["login"] and password1 in baza["password"]:
                print ("Введите новое имя.")
                name1 = input("name: ")
                baza["name"] = name1
                print(baza)

        elif a == 2:
            print("Для смены даты раждения введите логин и пороль.")
            login1 = input("Login: ")
            password1 = str(input("Password: "))
            if login1 in baza["login"] and password1 in baza["password"]:
                print ("Введите новую дату рождения.")
                birthday1 = input("Birthday: ")
                baza["birthday"] = birthday1
                print(baza)

        else:
            print("Такой операции нет")
    else:
        print("Не правильный логин или пароль.")        
else:
    print("Ошибка, неверные данные !")





