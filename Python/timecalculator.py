# TimeCalculator.py

# function to convert time string to integer components
def convert_time(time_str):
    parts = time_str.split(':')
    day = int(parts[0])
    hour = int(parts[1])
    minute = int(parts[2])
    return day, hour, minute

# function to convert integer components to time string
def convert_string(day, hour, minute):
    time_str = f"{hour:02}:{minute:02}"
    if day > 0:
        time_str = f"{day:02}:{time_str}"
    return time_str

# function to add two times
def add_time(time1, time2):
    day1, hour1, minute1 = convert_time(time1)
    day2, hour2, minute2 = convert_time(time2)
    carry = 0
    minute_sum = minute1 + minute2
    if minute_sum >= 60:
        carry = 1
        minute_sum -= 60
    hour_sum = hour1 + hour2 + carry
    carry = 0
    if hour_sum >= 24:
        carry = 1
        hour_sum -= 24
    day_sum = day1 + day2 + carry
    return convert_string(day_sum, hour_sum, minute_sum)

# function to subtract two times
def subtract_time(time1, time2):
    day1, hour1, minute1 = convert_time(time1)
    day2, hour2, minute2 = convert_time(time2)
    carry = 0
    minute_diff = minute1 - minute2
    if minute_diff < 0:
        carry = 1
        minute_diff += 60
    hour_diff = hour1 - hour2 - carry
    carry = 0
    if hour_diff < 0:
        carry = 1
        hour_diff += 24
    day_diff = day1 - day2 - carry
    if day_diff < 0:
        return "Invalid: Result is negative"
    return convert_string(day_diff, hour_diff, minute_diff)

# function to multiply a time by a scalar
def multiply_time(time_str, scalar):
    day, hour, minute = convert_time(time_str)
    total_minutes = day * 24 * 60 + hour * 60 + minute
    result_minutes = total_minutes * scalar
    day_result, remainder = divmod(result_minutes, 24 * 60)
    hour_result, minute_result = divmod(remainder, 60)
    return convert_string(day_result, hour_result, minute_result)

# function to display the menu and get user choice
def get_choice():
    print("Main Menu:")
    print("1. Add two times")
    print("2. Subtract two times")
    print("3. Multiply a time by a scalar")
    print("9. Quit")
    choice = input("Enter your choice (1-3 or 9): ")
    return choice

# main program
time1 = input("Enter the first time (DD:HH:MM): ")
time2 = input("Enter the second time (DD:HH:MM): ")

choice = get_choice()
while choice != "9":
    if choice == "1":
        print("Result:", add_time(time1, time2))
    elif choice == "2":
        print("Result:", subtract_time(time1, time2))
    elif choice == "3":
        scalar = int(input("Enter the scalar: "))
        print("Result:", multiply_time(time1, scalar))
    else:
        print("Invalid choice!")
    
    choice = get_choice()
