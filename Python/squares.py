n = 1
while n <= 100:
    square = n ** 2
    print(n, "squared is", square)
    if square > 2000:
        print("The square of", n, " is bigger than 2000")
        break
    n += 1
