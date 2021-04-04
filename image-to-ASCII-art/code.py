---
#Converting PNG Images to ASCII Art
#Author: Priya Mondal
---

#ASCII - American Standard Code for Information Interchange, refer to wiki to know more

#include the necessary module
import pywhatkit as kt

#display the welcome msg
print('Lets turn images to ASCII art')

#Source path is basically the image png file which you want to convert to ASCII
source_path = 'chai.png'

#Target path deciphers the file name with which the ASII art gets saved
target_Path = 'image_to_ASCII_art.text'

#calling the method by giving necessary parameters
kt.image_to_ascii_art(source_path,target_Path)
