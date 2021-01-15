---
#Project Name: Random Password Generator
#Author: Priya Mondal
---
#What is a Password? - A password, sometimes called a passcode, is a memorized secret, typically a string of characters, usually used to confirm a user's identity.

#Module Used: random.sample, string
import random
import string

print("Welcome to Password Generator!")

length = int(input('\nEnter the length of the Password: '))

#Lower case alphabets, upper case alphabets & Punctuations
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#Compile it all together
all = lower + upper + num + symbols

# Now using Random Module to generate the Password
temp = random.sample(all, length)   #Passing two Parameters
password = "".join(temp)
print(password)


