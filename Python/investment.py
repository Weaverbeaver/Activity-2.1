# Prompt the user for inputs
initial_investment = float(input("Enter the initial investment amount in pounds: "))
target_value = float(input("Enter the target value in pounds: "))
interest_rate = float(input("Enter the interest rate as a percentage: "))

interest_rate = interest_rate /100

years = 0
while initial_investment < target_value:
    initial_investment = initial_investment + (initial_investment * interest_rate)
    years += 1
    print(f"After year {years}: {initial_investment:.2f} pounds")

# Display the result
print(f"It will take {years} years to grow your initial investment of {initial_investment:.2f} pounds to {target_value:.2f} pounds at an interest rate of {interest_rate*100}%.")
