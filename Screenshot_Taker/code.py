'''
# Author -> Priya Mondal
'''
# Screenshot - Popularly known as ScreenCapture is a digital image that shows the content of a computer display. 
# A common scrrenshot is created by the computer device or the OS installed on the device.
# Module Used -> Pyauto GUI


#With GUI
import pyautogui
import tkinter as tk

root= tk.Tk()
root.title('Sc taker')

#Give your suitable width and height.
canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

#creating a function
def myScreenshot():
    
    myScreenshot = pyautogui.screenshot()
    
    #Always mention the File Path and the name by which you want to store your Screenshot.
    myScreenshot.save(r'D:\PROJECTS\screenshot1.png')

myButton = tk.Button(text='Take Screenshot', command=myScreenshot, bg='green',fg='white',font= 15)
canvas1.create_window(150, 150, window=myButton)

root.mainloop()
