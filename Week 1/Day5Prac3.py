input = "nama saya helmy"
print(input)

def operation1(input):
    str = input.split()
    str.reverse()
    return str

def operation2(input):
    str = input.split()
    str.reverse()
    return ' '.join(str)

result1 = operation1(input)
result2 = operation2(input)
print(result1) 
print(result2)