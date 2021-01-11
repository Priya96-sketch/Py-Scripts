---
#Automating Whatsapp using Python Codes
#Author: Priya Mondal
---

#import the necessary module!
import pywhatkit as kt
import getpass as gp

#display welcome msg
print("Hey!! Let's Automate Python")

#capture the target phone number
p_num = gp.getpass(prompt='PhoneNumber: ', stream=None)     #This prompt along with stream is used for taking the input from the user

#capture the message
msg='I love Python'

call the method
kt.sendwhatmsg(p_num,msg,19,10)

--------------------------------------------------------------

#Above can be done with 2lines of Code as well

import pywhatkit as kt
kt.sendwhatmsg("+919*********", "I love Python!", 10, 25)

