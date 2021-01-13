---
#Project - Generate Wikipedia Summary
#Author : Priya Mondal
---

# What is Wikipedia : Open free content online Encyclopedia created with the effort of a collaborative community of users known as Wikipedians.
# Module used : pywhatkit
import pywhatkit as kt
print("Let's generate wiki summary")

#Capture what you will search. Examples taken as samples.
target1 = 'Coronavirus'
target2 ='Python'


#Calling the info. Here the 1st parameter deciphers the target you want to search to get a summary. 2nd parameter depicts the number of
# lines of code you want.

kt.info(target2, lines=3)
print('\n')
kt.info(target1, lines= 4)  
