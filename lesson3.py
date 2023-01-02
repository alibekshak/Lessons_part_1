# name = input("Name: ")
# print(name.title())
# #title() - все начальные буквы пишутся с большой буквы 

# print(name.upper())
# #upper - все буквы пишутся выерхнем регистре 

# print(name.lower())
# #lower - все буквы пишутся в нижнем регистре 

# print(name.swapcase())
# #swapcase - все большие в маленькие и маленькие в большие

# print(name.capitalize())
# #capitalize - начальные буквы вверхний регистр 

# a = "111"
# print(a.isdigit())
# #isdigit - все ли состоит из цифр 

# print(a.isalpha())
# #isalpha - все ли состоит из букв 

# print(a.isidentifier())
# #isidentifier - все ли у нас пишется слитно 

# print(a.islower())
# #islower - все ли у нас в нижнем регистре, isupper тоже самое только верхнем регистре 

# print(a.istitle())
# #istitle -  все ли у нас начинается с большой буквы 

# print(a.isspace())
# #isspace - есть ли у нас пробелы 

# print(a.isprintable())
# #isprintable - все ли мы можем принатавать 



# text = "Hellow Bektyr"
# print(text.strip("Hell"))
# #strip - удаляет начала текста или буквы 



# text = "Hellow"
# print(text.center(10, "*"))
# #center  - выравнивает строки 

# print(text.rjust(10, "*"))
# #rjust - выравнивание строки с парва 


# text = "Tina"
# print(f"Hi, {text}")



# print('age: {0}, name: {1}'.format("12", "London"))
#format - добавляет в сторку данные 




# text = input()

# print(text.isalpha())
# print(text.isdigit())

# if text.isdigit():
#     print(True)
# else:
#     (False)


# text = "python, go"
# print(text.replace("go", "python"))
# #replace -  замена текста 

# print(text.find("a"))
#find - ищет буквы в индексе 

# print(text.index("g"))
# #index - ищет букву в индексе 

# print("*".join(text))
#join - добавляет в текст 


# text = "Hellow world"
# print(text.count("l"))
# #count - считает буквы цыфры и т.д. так же можно добавить индексы 


# print(text.split())
# #split - разделит на текст и обернет в list

# print(text.splitlines())
# #splitline - весь текс обернет в list

# print(text.partition("Hellow"))
# #partition - делит букву или слово и добовляет в массив 

# print(text.startswith("H"))
# #startswich - начинается ли текс с буквы или слова  True False

# print(len(text))
# #len - считает колличество букв 



# text = "Hellow"
# print(text[-1:-7:-1]) #срез 



# password = input("Введите пароль: ")
# password2 = input("Введите пароль повторно: ")

# if password == password2: 
#     if len(password2) >= 8:
#         if "123" not in password2:
#             print("Пароль подходит")

#         else:
#            print("Простой пароль") 
#     else:
#         print("Ваш пороль должен састоять из 8 символов")
# else:
#     print("Пароль не подходит")

# print("*".join(password2))

# text = "HEllow"
# print(text[3:].upper())
# print(text[:3].lower())


# name = input("Name: ")
# age = input("Age: ")
# movie = input("What movie do you like ? ")

# print(f"Hello {name}, i love that movie {movie} ")


# name = input("Name: ")
# print("What is your name?", '*'.join(name))


# a = " что что что"
# print(a.replace("ч", "4"))



# login = input("Enter login: ")
# password = input("Enter password: ")


# if login == login.lower():
#     if len(password) >= 8:
#         if "134567890".find(password):
#             if "wqertyuiopasdfghjklzxcvbnm".find(login.lower()):

#                 print(f"Your password is {password}, your login is {login.lower()}")
           
#             elif "йцукенгшщзхъфывапролджэёячсмитьбю".find(login.lower()):
#                 print("Error, fffff")
            
            
#             else:
#                 print("Error, dot't use ru language")
            

#         else:
#             print("Error, nead namber")
        

#     else:
#         print("Error, less then 8 symbol")

# else:
#     print("Error")