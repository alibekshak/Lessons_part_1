baza = {
    "Admin":{
        "phone" : "7071232323",
        "name" : "Jon",
        "balance" : 9999, 
        "password" : "123qweasd",
    "endless":{
        "phone" : "7071232323",
        "name" : "Lenon",
        "balance" : 10000, 
        "password" : "1234qweasd"
    }
    }
}

key = None 

while True:
    table = int(input("""
        1 - Зарегистрироваться
        2 - Авторизоваться
        3 - Перевод баланса
        4 - Список пользователей
        5 - Информация
        6 - Номер телефона   
        7 - Выйти
        Выберите операцию:
    """))
    if table ==1:
        if key in None:
            login = input("Ввеите логин: ")
            if login.isalpha():
                name = input("Введите имя: ")
                if name.isalpha():
                    phone = input("Введите номер телефона: +7")
                    if phone.isdigit():
                        password = input("Введите пароль: ")
                        password2 = input("Введите пароль повторн: ")
                        while password !=password2:
                            password = input("Введите пароль: ")
                            password2 = input("Введите пароль повторн: ")
                        else:
                            baza.update({
                                login: {
                                    "name": name,
                                    "phone": phone,
                                    "balance": 1000,
                                    "password": password
                                }
                                }
                            )
                            key = login
                    else:
                        print("Номер должен состоять из цифр")        
                else:
                    print("Имя должно состоять из букв")            
            else:
                print("Логин должно состоять из букв")
        else:
            print("Вы уже зарегестрированны")

    elif table == 2:
        if key is None:
            login = login = input("Ввеите логин: ")
            if login in baza.keys():
                password = input("Введите пароль: ")
                if password == baza[login]["password"]:
                    print("Вы авторизовались")
                    key = login
                else:
                    print("Неверный пароль")
            else:
                print("В базе нет такого пользователя")
        else:
            print("Вы уже авторизванный")
    
    elif table == 3:
        if key is not None:
            login_balance = input("Ввдите логин получателя")
            if login_balance.isalpha() and login_balance in baza.keys():
                summa = int(input("Введите сумму перевода: "))
                if summa <= baza[login]["balance"]:
                    baza[login]["balance"] -= summa
                    baza[login_balance] += summa
                    print("Перевод отправлен")
                else:
                    print("У вас не хватает денег")    
            else:
                print("Не верный логин")    
        else:
            print("Пожалуйста авторизуйтесь")    

    elif table ==4:
        if key is not None:
            print(baza)
        else:
            print("Вы не авторизовались")
    
    elif table == 5:
        if key is not None:
            print(f"""
                Ваши данные 
                name: {baza[key]["name"]}
                balance: {baza[key]["balance"]}
                password {baza[key]["passord"]}
            """)
        else:
            print("Сначало авторизуйися")

    elif table ==6:
        if key is not None:
            print(f'phone number +7{baza[key]["phone"]}')
        else:
            print("Сначало авторизуйися")

    elif table == 7:
        key = None
        print("Вы вышли из акааунта")

# 1
# a = [1, 1, 2, 3, 4, 5, 7, 8, 13, 21, 23, 34 ]
# print(a[1:9])
# for i in a:
#     if i<=13:
#         print(i)

# 2
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# a = [1, 1, 2, 3, 4, 5, 7, 8, 13, 21, 23, 34 ]
# c = []

# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

# 4
# a = {
#     "dd": 12,
#     "da": "fdf",
#     "ds": "dsde"
#     }

# d = {
#     "sdf": "fsdf", 
#     "dsf": "qwer",
#     "asfsf": 1244
# }

# b = {}

# a.update(d)
# b.update(a)
# print(b)


# 5
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

# for i in my_dict.values():
#     if i >=560:
#         print(i)


# 6
# for i in range(4):
#     i = str(i)
#     print(i)
    


# 8
# a = input()

# if a == a[::-1]:
#     print(a, True)
# else:
#     print("Error")

# 9
# n = int(input())
# hours = (n // 3600) % 24
# n = n % 3600
# minutes = n // 60
# n = n % 60
# sec = n
# print(hours, str(minutes // 10) + str(minutes % 10), str(sec // 10) + str(sec % 10), sep=':')

# 10
# a = input("Введите число: ")

# d = ()
# c = []

# d = list(d)
# d.append(a)
# d = tuple(d)
# c.append(a)

# print(d, c)


# 11
# d = [1, 2, "fff", "dssa"]
# print(d[0], d[-1])


# 12
# d = [1, 3, "fffs"]

# for i in d:
#     print(type(d))


# 13
# n = 12
# while n >= 12:
#     print(n + n*n + n*n*n)
#     break


# 14
# x = [1, 20, 25, 22, 3, 23, 44, 90, 150, 200, 237, 400, 432, 467]

# for i in x:
#     if i <= 237:
#         if i % 2 == 0:
#             print(i)


# 15
# ss = [1, 20, 25, 22, 3, 23, 44, 90, 150, 200, 237, 400, 432, 467]
# dd = [1, 2, "fff", "dssa", 20]


# dd.extend(ss)
# dd = set(dd)
# dd = list(dd)
# print(dd)

# 17
# b = 1
# c = 3
# print(b+c)

# 18
# v = "Hellow"
# print(len(v))

# #19
# d = 5
# c = 7
# d, c = c, d
# print(d,c)

# 20

# a = [15, 35, 150, 300, 450, 550, 750, 666, 111]

# for i in a:
#     if i %15 == 0:
#         print(i)


# 21 

# a = [15, 15, 2, 43, 34,  35, 35]

# a = set(a)
# a = list(a)
# print(a)



