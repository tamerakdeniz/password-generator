import random
import string

def generate_password():
  ozelkarakter = '!@#$%^&*()+-='
  sayi = '0123456789'
  buyukharf = string.ascii_uppercase
  kucukharf = string.ascii_lowercase
  noktalama = string.punctuation

  password_characters = []
  password_characters.extend(list(ozelkarakter))
  password_characters.extend(list(sayi))
  password_characters.extend(list(buyukharf))
  password_characters.extend(list(kucukharf))
  password_characters.extend(list(noktalama))

  password = ''
  for i in range(20):
    password += random.choice(password_characters)

  return password

generated_password = generate_password()
print(generated_password)