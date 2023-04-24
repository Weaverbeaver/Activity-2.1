S = 0
C = 0
V = 0
broke = False
milkshake = {"Chocolate": 2.30, "Strawberry": 3.50, "Vanilla": 2.80}
money = float(input("What is your budget? "))
print("Menu:")
print("")
print("1. Strawberry: £3.50")
print("2. Chocolate: £2.30")
print("3. Vanilla: £2.80")
print("")
choice = input("What can i fix you? ")
if choice.upper() == "Q":
    quit
while broke == False:
    if choice == "1":
        money -= milkshake["Strawberry"]
        if money <= 0:
            broke = True
            print("I'm sorry, you cant afford this.")
            money += milkshake["Strawberry"]
            break
        S += 1
        print ("You have ordered a Strawberry milkshake")
    elif choice == "2":
        money -= milkshake["Chocolate"]
        if money <= 0:
            broke = True
            money += milkshake["Chocolate"]
            print("I'm sorry, you cant afford this. Chocolate milkshakes cost £2.30 and you have", money)
            break
        C += 1
        print ("You have ordered a Chocolate milkshake")
    elif choice == "3":
        money -= milkshake["Vanilla"]
        if money <= 0:
            broke = True
            print("I'm sorry, you cant afford this.")
            money += milkshake["Vanilla"]
            break
        V += 1
        print ("You have ordered a Vanilla milkshake")
print ("You have ordered", S, "Strawberry milshakes,", C, "Chocolate milkshakes and", V, "Valilla milkshakes")
