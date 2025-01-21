import datetime
def log_message(filename):
    print("Log message program")
    print("Type 'exit' to stop logging messages \n")
    while True:
        message = input(" Enter Your Message: ")
        if message.lower() == 'exit':
            print("Exiting logging program")
            break
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            log_entry = f"[{timestamp}] {message}\n"
            with open(filename, 'a') as file:
                file.write(log_entry)
            print("Messages logged succesfully")
        except Exception as e:
            print(f"An error occured {e}")
log_message('logfile.txt')