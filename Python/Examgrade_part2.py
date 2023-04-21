mark = int(input("Enter exam mark (between 1 and 100): "))
level = int(input("Enter student level (1 or 2): "))

if mark < 1 or mark > 100:
  print("Error: marks must be between 1 and 100")
elif level == 1:
  if mark < 50:
    print("Fail")
  elif mark <= 60:
    print("Pass")
  elif mark <= 70:
    print("Merit")
  else:
    print("Distinction")
elif level == 2:
  if mark < 40:
    print("Fail")
  elif mark <= 50:
    print("Pass")
  elif mark <= 65:
    print("Merit")
  else:
    print("Distinction")
else:
  print("Error: invalid student level")
