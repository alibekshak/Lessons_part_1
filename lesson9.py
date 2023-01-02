# GITHUB
# ---------------------------------------------------------------------------------------------------------

# Если хотим запушить все на новую репозиторию 
# rm -rf                                    = Удаляем папку .git которая уже связано к старой репозитории
# git init                                  = инитцализирует и создает папку .git
# git remote add origin (shh репозитория)   = Копируем ssh нашего репозирия и вставляем
# git add .                                 = Выделяем все наши файлы
# git commit -m "all"                       = Коментим репозиторию
# git push -u origin master                 = Пушим все в ветку мастер

# ---------------------------------------------------------------------------------------------------------

# Если хотим отправить на тот же репозитории тогда не удаляем папку .git
# git add .                                 = Выделяем все наши файлы
# git commit -m "all"                       = Коментим репозиторию
# git push -u origin master                 = Пушим все в ветку мастер

# ---------------------------------------------------------------------------------------------------------
# OPEN and WITH

# a = ("Ali\n", "Jon\n", "Bob\n" )
# f = open("ITCbootcamp.txt", "w")# w- писать в файле 
# f.write("Hello World\n")# добавляет в файл 
# # f.write("Hellow You \t")
# # f.writelines(a)
# # f.close()# - закрывает файл, не можем добавить данные после close

# # a+ - читает и добавляет данные 
# # w - можно только добовлять данные 
# # r - читает файл

# # with open("ITC.txt", "a+") as f:# - тоже саздает файл и закрывает его 
# #     f.write("Hello")

# f = open("ITCbootcamp.txt", "r")
# a = f.read()# -  читает колличество указанных симвалов а также может прачитать полностью все данные в файле
# print(a)
#readline - читает указанную строчку 
# f.close()


# login = input("Введите логин:")
# password = input("Введите пароль:")
# with open("user.txt", "r") as f:
#     # f.write(f"логин: {login}, пароль {password}")
#     a = f.read()
#     for i in a:
#         if i == "w":
#             print("Да")
#         else:
#             print("Нет")


# ff = []
# with open("python.txt", "r") as f:
#     d = f.read()

#     for i in d.split():
#         for j in i:
#             if j =="t" or j == "T":
#                 ff.append(i)
# print(ff)

# login = input("Login: ")   
# password = input("Password: ")
# with open("database.txt", 'w') as f:
#     f.write(f"{login}", {password})

# with open("database.txt", 'r') as a:
#     ww = a.readline()
#     print(ww)


# 1
# while True:
#     baza = int(input("""
#         Зарегестрироватся -1
#         Авторизация - 2
#     """))
#     if baza == 1:
#         login = input("Login: ")
#         password = input("Password: ")
#         password1 = input("Passwoed agen: ")
#         while password == password1:
#             password = input("Password: ")
#             password1 = input("Passwoed agen: ")
#         else:
#             with open ("database.txt", 'a+') as fail:
#                 db = fail.readline()
#                 for i in db:
#                     if i == f"{login}, {password}":
#                         print("Not welcome")
                    
#                     else:
#                         for i in range(1):
#                             with open("database.txt", "a+") as ned_dir:
#                                ned_dir.write(f"{login}", {password})
#                                print("Congrate")
#     elif baza == 2:
#         login = input("Login: ")
#         with open ("database.txt", 'a+') as df:
#             for i in df:
#                 if login in i:
#                     password = input("Password: ")
#                     with open ("database.txt", 'a+') as df:
#                         for i in df:
#                             if password in i:
#                                 print("Congrat")

#                             else:
#                                 print("Error, password") 
#                 else:
#                     print("Error, login")


# 2
# s = ["Alibek\n", "Guluzim\n", "Adi\n", "Miraz\n", "Stas\n", "Darhan\n", "Salamon\n", "Roman\n"]
# with open("Itcbootcamp.txt", "w") as a:
#     a.write("Hellow :\n")
#     a.writelines(s)
#     a.write("Hellow Itc - Bootcamp \n")


# Home work
while True:
    start =  int(input("""
    1 - Создать файл 
    2 - Открыть файл 
    """))
    if start == 1:
        name_fail = input("Название файла: ")
        text = input("Ваши текст: ")
        with open(name_fail, "w") as f:
            f.write(text)
            print("Файл был создан")

    elif start == 2:
        name_fail = input("Название файла для его открытия: ")
        with open(name_fail,"r") as f:
            read = f.read()
            print(read)



