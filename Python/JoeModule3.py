# grade = int(input("What is your grade?"))
# if grade >= 85:
#     print("distinction")
# elif grade >= 65:
#     print("pass")
# elif grade <= 65:
#     print("fail")

unit = input("enter the unit of your weight ")
weight = float(input("enter the weight you want to be converted "))
unit = unit.lower()

if unit == "kg":
    weight = weight * 2.20462
    newunit = "lbs"
elif unit == "lbs":
    weight = weight * 0.453592
    newunit = "kg"
else:
    print("please put a suitable unit")

print("your converted weight is", weight, newunit)