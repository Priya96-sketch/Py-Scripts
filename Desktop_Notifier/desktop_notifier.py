---
#Project Name: DESKTOP NOTIFIER
#Author: Priya Mondal
---

#Module used: plyer - Plyer is a platform-independent api to use features commonly found on various platforms, notably mobile ones, in Python.

from pyler import notification


#specify the parameters
title = 'Hello everyone!'

message= 'Thankyou for reading! Take care!'

#Lets look what the Parameter mean: title   -> Title of the Notification
#                                   message  -> Message of the Notification
#                                   app_icon -> Icon to be displayed along with the message
#                                   timeout  -> Time to display the message for, defaults to 10
#                                   toast    -> Simple message instead of full notification

notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 10,
                    toast=False)
