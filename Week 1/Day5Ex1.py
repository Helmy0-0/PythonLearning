import re

def clean_text(text):
    #remove punctuation
    text = re.sub(r"[^\w\s]", "", text)
    #remove extra spaces
    text = " ".join(text.split())
    #convert to lowercase
    return text.lower()
input_text = ("   Hello, World!!! Welcome to PYTHon, Programming.... !!   ")
cleaned_text = clean_text(input_text)
print("Cleaned text:", cleaned_text)
