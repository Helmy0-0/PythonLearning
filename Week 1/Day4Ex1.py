person = {"name": "John", "age": 36, "grade": "A"}
print(person)
#add new key-value pair
person["address"] = "123 Main Street"
#update value
person["age"] = 32
#remove grade
if "grade" in person:
    del person["grade"]
print(person)