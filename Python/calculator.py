num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Calculator Menu:")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
print("5. S")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
   print(num1, "+", num2, "=", (num1 + num2))
elif choice == '2':
   print(num1, "-", num2, "=", (num1 - num2))
elif choice == '3':
   print(num1, "*", num2, "=", (num1 * num2))
elif choice == '4':
   print(num1, "/", num2, "=", (num1 / num2))
else:
   print("Invalid input")