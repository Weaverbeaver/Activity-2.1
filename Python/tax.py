salary = 0
def getincometax(salary):
    salary = int(input("please enter your salary"))
    if 0 <= salary <= 11850:
        print("you dont have to pay any tax")
    elif 11851 <= salary <= 34500:
        print("you pay 20% tax")
        tax20 = (salary - 11850)*0.2
        print("Your tax this year is", tax20)
        return
    elif 34501 <= salary <= 150000:
        print("you pay 40% tax")
        tax20 = (11850)*0.2
        tax40 = (salary - (34500 - 11850))*0.4 + tax20

        print("Your tax this year is", tax40)
    elif salary > 150000:
        print("you pay 45% tax")
        tax20 = (11850)*0.2
        tax40 = (34500)*0.4
        tax45 = (salary - (150000 - 34500))*0.45 + tax20 + tax40
        print("Your tax this year is", tax45)
    else:
        print("please enter a valid salary")

getincometax(salary)