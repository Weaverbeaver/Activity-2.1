min_value = 1
max_value = 100
tries = 0

while tries < 3:
    user_input = int(input(f"Enter an integer between {min_value} and {max_value}: "))
    if user_input.isdigit():
        user_number = int(user_input)
        if min_value <= user_number <= max_value:
            print("You entered:",user_number)
            break
    print("Invalid input. Please try again.")
    tries += 1

if tries == 3:
    print("None")