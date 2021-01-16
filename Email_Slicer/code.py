---
#Project Name: Email Slicer
#Author: Priya Mondal
---

#BREAKDOWN OF MAIL ADDRESS-priyapujamondal@gmail.com : USERNAME:priyapujamondal, DOMAIN:gmail.com, @ symbol: Divider.
#  The symbol is required for all SMTP email addresses.

#Get the user's mail address
email = input("What is your email address? ").strip()   #strip function is used to cut any spaces infront, between or atlast of the mail address.

#Slice out the Username
user_name = email[:email.index("@")]       #Slicing the email upto '@' symbol

#Slice out the Domain Name
domain_name = email[email.index("@")+1:]       #Slicing the email after '@' symbol

#Format Message
res = "Your username is '{}' and your domain name is '{}'".format(user_name,domain_name)

#Display the result message
print(res)

 
