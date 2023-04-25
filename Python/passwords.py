# common_passwords = ["password", "password123", "password!"]

# def check_password(common_passwords):
#     user_passwords = input("whats your password?")
#     if user_passwords in common_passwords:
#         print("Thats very insecure")
#     else:
#         print("Your password is secure")
#     print(common_passwords)

# check_password(common_passwords)

number1 = 0
number2 = 0
number3 = 0

def math(number1, number2, number3):
    number1 = int(input("Hello friend! please input a number! "))
    number2 = int(input("Bonjour ami! please input a second number! "))
    print("The addition of the two numbers is", number1 + number2)
    print("The subtraction of the two numbers is", number1 - number2)
    print("The multiplication of the two numbers is", number1 * number2)
    number3 = int(input("Hola amigo! Please input a third number! "))
    if number1 < number2:
        if number1 < number3:
            print(number3, "is the biggest number!!!")
            return
        elif number3 < number2:
            print(number3, "is a big boy number.")
            return
    elif number2 < number3:
        print("Dang,", number2, "is the biggest number.")


    if number1 / 2:
        print("even")
    else:
        print("odd")

math(number1, number2, number3)
