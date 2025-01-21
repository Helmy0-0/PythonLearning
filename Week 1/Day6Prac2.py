def operation(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.lower().split()
            
            search = input("Enter Word: ").lower()
            frequency = words.count(search)
            if frequency>0:
                print(f"The Word '{search}' appear {frequency} time(s) in the file")
            else:
                print(f"the word '{search}' is not found")
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"An error occured {e}")
operation('wordcount.txt')