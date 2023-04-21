n = int(input("Input a nunmber to be factorised"))
factorial = 1
x = n

if n == 0:
    print("The factorial of 0 is 1.")
else:
    while n > 1:
        print("Multiplying", factorial, "by", n)
        factorial *= n
        n -= 1
    print("The factorial of", x, "is", factorial)