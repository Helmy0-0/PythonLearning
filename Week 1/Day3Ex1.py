def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
def print_factorial(n):
    result = factorial(n)
    print(f"factorial {n} = {result}")
    
print_factorial(2)