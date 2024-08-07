# main.py
# python-mini-projects @Mitesh

import random
import string
import math

password_length = int(input("Enter Length of Password:"))

    
## 1st Method 

characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.sample(characters,password_length))

print("1st Method:",password)

## 2nd Method  

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation


# 50-30-20 Rule
letterslen = password_length//2
numberslen = math.ceil(password_length*0.3)
symbolslen = password_length-letterslen-numberslen

password = random.sample(letters,letterslen)+random.sample(numbers,numberslen)+random.sample(symbols,symbolslen)
random.shuffle(password)
password = "".join(password)
print("2nd Method:",password)
