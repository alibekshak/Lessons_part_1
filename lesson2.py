#age = int(input("Your age: "))
#height = int(input("Your height: "))


#if age >= 16 and height >= 159:
    #print("Welcome")
#else:
    #print("You are young")




#2
#year = int(input("Year: "))

#if year % 100 == 0 or year % 400 == 0:
    #print(True)
#else:
    #print(False)



# a = float(input("a: "))

# if a % 2 !=0:
#     print("Cool")
# else:
#    print("no way")



# num = int(input("Num: "))
# num2 = int(input("Num2: "))
# aper = input('+ * / - // ')

# if aper == '*':
#     print(f'{num} {aper}{num2}=', num * num2)
# elif aper == '/':
#     print(f'{num} {aper}{num2}=', num / num2)
# elif aper == '+':
#     print(f'{num} {aper}{num2}=', num + num2)
# elif aper == '-':
#     print(f'{num} {aper}{num2}=', num - num2)
# elif aper == '//':
#     print(f'{num} {aper}{num2}=', num // num2)
# else:
#     print("Some thing wrong")


# aper = input(' * + ')
# slovo = input("slovo: ")
# non = int(input("Non: "))

# if ' ' in  slovo :
#     if aper == "*":
#         print(f'{non} {aper}{slovo}=', non * slovo) 
#     elif aper == '+':
#         print(f'{non} {aper}{slovo}=', non + slovo) 
# else:
#     print("non")

# a = input()

# if ' ' in a:
#     print(a, True)
# else: 
#     print('error')


print(''' \U0001f387 Welcom to the Rock Paper Scissor \U0001f387
\U0001f531 Rules of the game:
1:rock \U0001f5ff
2:paper \U0001f4c4
3:scissors \U0001f374''')

user1 = int(input('Select number, user1 \U0001f914 '))
user2 = int(input('Select number, user2 \U0001f914 '))

if user1 == user2:
    print("non win \U0001f4f5 ")
elif user1 == 1 and user2 == 2:
    print("user1 win \U0001f3c5 ")
elif user1 == 2 and user2 == 1:
    print("user2 win \U0001f3c5 ")
elif user1 == 3 and user2 == 1:
    print("user2 win \U0001f3c5 ")
elif user1 == 2 and user2 == 3:
    print("user2 win \U0001f3c5 ")
elif user1 == 1 and user2 == 3:
    print("user1 win \U0001f3c5 ")
elif user1 == 3 and user2 == 2:
    print("user1 win \U0001f3c5 ")
else:
    print("error \U0001f51e ")
print("Congrats you finish the game \U0001f3C1 \U0001f3C6")