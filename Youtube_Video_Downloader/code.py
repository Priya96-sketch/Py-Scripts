#Module Used -> Pytube
# Project -> Fetching the Video Title, Fetch the Thumbnail Image, Download a Youtube Video
# Features of Pytube: 
# 1 - Support for both progressive and dash streams
# 2 - Easily register on download progress and on download complete callbacks
# 3 - Command Lined Interface included
# 4 - Outputs caption tracks to .srt format(SubRipSubtitle)
# 5 - Caption Track Support
# 6 - Ability to capture thumbanail URL
# 7 - Extensively Documented Source Code
# 8 - No-Third Part Dependencies

#import the package. We are importing Youtube class from pytube module.
from pytube import YouTube

#Get the URL
url = 'https://www.youtube.com/watch?v=YcVKtJz0YFs'

#Now calling the Youtube Method.
my_video = YouTube(url)


# Here Fetching of the YOUTUBE VIDEO TITLE will be done. 
print("*********************Video Title************************")
#get Video Title
print(my_video.title)

# Here Fetching of the YOUTUBE THUMBNAIL IMAGE will be done. 
print("********************Tumbnail Image***********************")
#get Thumbnail Image
print(my_video.thumbnail_url)

# Here Fetching of the YOUTUBE VIDEO will be done. 
print("********************Download video*************************")

#get all the stream resolution for the 
#for stream in my_video.streams:
    #print(stream)


#set stream resolution. You can choose highest or lowest resolution or can download the audio version only.
my_video = my_video.streams.get_lowest_resolution()

#or
#my_video = my_video.streams.first()

#Download video
my_video.download()
