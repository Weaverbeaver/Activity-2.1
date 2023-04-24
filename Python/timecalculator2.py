def convert_time(time_str):
    parts = time_str.split(':')
    day = int(parts[0])
    hour = int(parts[1])
    minute = int(parts[2])
    return day, hour, minute

def convert_string(day, hour, minute):
    time_str = f"{hour:02}:{minute:02}"
    return time_str

print("Time Calculator")
print("1-	Add 2 times   ")
print("2-	Find the difference between 2 times  ")
print("3-	Convert to Hours  ")
print("4-	Convert to Minutes  ")
print("5-	Convert Minutes to Time  ")
print("6-	Convert Hours to Time  ")
print("7-	Convert Days to Time  ")
print("8-	Exit  ")
option = input("Please pick an option ")
while option != "9":
    if option == "1":
        time1 = input("enter the first time")
        convert_time(time1)
        time2 = input("enter the second time")
        convert_time(time2)
        time1.day
        
