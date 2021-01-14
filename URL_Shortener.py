---
#Project: URL Shortener
#Author: Priya Mondal
---
#What is URL? -> Uniform Resource Locator.It's basically a web address used to locate. Having 3parts: PROTOCOL, DOMAIN, PATH.
#Module Used: pyshorteners

import pyshorteners as sh

#You can take user input for the Link
link = 'https://en.wikipedia.org/wiki/URL'

s = sh.Shortener()

print(s.tinyurl.short(link))
