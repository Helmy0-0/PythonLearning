def check_even_odd(number):
    if number %2==0:
        return "Even"
    else:
        return "Odd"
def process_number(number):
    result = check_even_odd(number)
    print(f"number {number} is {result}")
process_number(10)
process_number(7)