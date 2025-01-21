while True:
    num = int(input("Enter a number: "))
    fact = 1


    if num < 0:
        print("Sorry, factorial cant in negative number")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            fact *= i
    print("Result: ", fact)
    
