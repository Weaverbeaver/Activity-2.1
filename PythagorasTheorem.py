print("1. Find the length of A given B and C ")
print("2. Find the length of B given A and C ")
print("3. Find the length of C given A and B ")


choice = input("Enter your choice: ")

if choice == "1":
  b = float(input("Enter length of side B: "))
  c = float(input("Enter length of side C: "))
  a = (c**2 - b**2)**0.5
  print("Length of side A is:", a)
elif choice == "2":
  a = float(input("Enter length of side A: "))
  c = float(input("Enter length of side C: "))
  b = (c**2 - a**2)**0.5
  print("Length of side B is:", b)
elif choice == "3":
  a = float(input("Enter length of side A: "))
  b = float(input("Enter length of side B: "))
  c = (a**2 + b**2)**0.5
  print("Length of side C is:", c)
else:
  print("Invalid choice")
