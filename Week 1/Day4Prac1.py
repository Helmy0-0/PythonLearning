input_list = [1, 2, 3, 2, 1, 4, 5, 4]
def operation(input_list):
    # Remove duplicates by converting the list to a set
    unique_items = list(set(input_list))
    # Reverse the list
    unique_items.reverse()
    return unique_items

result = operation(input_list)
print(result) 