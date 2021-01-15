---
#Project Name: BUILD A TRANSLATOR
#Author: Priya Mondal
#Module Used: googletrans
---

#import the package
from googletrans import Translator

# Store some text for translation in french language
text = ''' Guten Morgan '''

# Create an instance of Translator to use
translator = Translator()

# detect the language
lang = translator.detect(text)
print(lang)


# Call the translate()
res = translator.translate(text, dest = 'en')

#print the result
print(res)
