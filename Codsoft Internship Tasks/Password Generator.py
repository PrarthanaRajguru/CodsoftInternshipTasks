import random
import string

print("Hello, Welcome to the password generator")
length = int(input("\nEnter the length of the password: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all_chars = lower + upper + num + symbols

temp = random.sample(all_chars, length)
password = "".join(temp)
print(password)

