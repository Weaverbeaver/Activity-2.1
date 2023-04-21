while True:
    math_mark = int(input("Enter Math mark (0-100): "))
    if 0 <= math_mark <= 100:
        break
    else:
        print("Invalid mark! Please enter a value between 0 and 100.")
while True:
    english_mark = int(input("Enter English mark (0-100): "))
    if 0 <= english_mark <= 100:
        break
    else:
        print("Invalid mark! Please enter a value between 0 and 100.")

while True:
    ict_mark = int(input("Enter ICT mark (0-100): "))
    if 0 <= ict_mark <= 100:
        break
    else:
        print("Invalid mark! Please enter a value between 0 and 100.")

average_mark = (math_mark + english_mark + ict_mark) / 3

result = ""
if average_mark >= 65:
    result = "Pass"
else:
    result = "Fail"

print(f"Average mark: {average_mark:.2f}")
print(f"Result: {result}")
