---
#Jokes Generator using Python
#Author: Priya Mondal
---

#importing the necessary module
import pyjokes

#consider looking to Website: pyjokes.es/api/ for API documentation 
#fetch the joke
joke1 = pyjokes.get_joke()     

#display the joke
print(joke1)

#fetch another joke
joke2 = pyjokes.get_joke(language='en', category='neutral')

#display the joke
print(joke2)

#fetch a bunch of jokes
jokes = pyjokes.get_jokes(language='en', category='neutral')


#using loops to print the number of jokes we want
for i in range(5):     #You can alter the number here for generating more number of jokes
    print(i+1,".",jokes[i])
