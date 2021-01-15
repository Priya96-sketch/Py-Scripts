---
#Project - Create GIF Converter
#Author: Priya Mondal
---

#What is GIF? -> GRAPHICAL INTERCHANGE FORMAT. Series of images of soundless videos that loops continuously that doesn't requirs any press 
# play button. AKA ANIMATED IMAGES.
#Gifs are basically the compressed format of the video and they are used in places where very few colors are used,they are mostly used 
# in logos as such. These gifs are compressed using lossless data compression in-order not to degrade the video quality.

#Module Used : Moviepy is a python module for video editing which can be used for basic operations such as cuts, concatenation, title insertion,
# video composeting, video processing and for adding advanced effects. To know more, go through Moveipy documentation.

from moviepy.editor import *

#loading video
#Here for sample "myvideo.mp4" is being used. Modify it as per your need.
clip=VideoFileClip('myvideo.mp4')

#getting only 3 first seconds from video
clip = clip.subclip(0,3)

#Saving video clip as gif
clip.write_gif('mygif.gif')
