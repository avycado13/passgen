import string
import secrets
import pyperclip
def password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
       password = ''.join(secrets.choice(alphabet) for i in range(10))
       if (any(c.islower() for c in password)
              and any(c.isupper() for c in password)
              and sum(c.isdigit() for c in password) >= 3):
    
          break
    pyperclip.copy(password)
    print(password)
def passphrase():
  pin_digits = int(input("Enter word amount for Passphrase: "))
  with open('words.txt') as f:
    words = [word.strip() for word in f]
    passphrase = ' '.join(secrets.choice(words) for i in range(pin_digits))
  pyperclip.copy(passphrase)
  print(passphrase)
def pin():
  pin_digits = int(input("Enter length for pin: "))
  pin = ''.join(secrets.choice(string.digits) for i in range(pin_digits))
  print(pin)
print(
'''
----------------------------------
  Please choose:
  1 - Generate a secure password
  2 - Generate a secure passphrase
  3 - Generate a secure PIN
----------------------------------
'''
)
option = input("Enter choice: ").strip()
if option == "1":
  password()
elif option == "2":
  passphrase()
elif option == "3":
  pin()
