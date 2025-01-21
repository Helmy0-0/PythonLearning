import re

def ganti_email(text):
    pola_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    ganti_dengan = '[EMAIL HIDDEN]'
    return re.sub(pola_email, ganti_dengan, text)
text = "Kirimkan email ke john.doe@example.com"
hasil = ganti_email(text)
print(hasil)  