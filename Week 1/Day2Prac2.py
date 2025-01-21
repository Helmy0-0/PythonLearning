list = []
num = int(input("Please enter list size: "))
for i in range(1, num + 1):
    value = int(input("Enter number %d: "%i))
    list.append(value)
print("Largest number on the list is: ", max(list))
