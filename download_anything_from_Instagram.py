#Project : Download Display Picture of Instagram Account
#Author: Priya Mondal

#Instagram - It is an photo and video-sharing social network owned by Facebook. To know more, visit Wikipedia
#Module Used- Instaloader: A tool to download pictures or videos along with their captions and other metadata from Instagram.

#To download - "$ pip3 install instaloader"
import instaloader

#Calling an instance
test = instaloader.Instaloader()

acc = input('Enter the Insta Account Username: ')

#download the data
#Here I am only downloading the Instagram Profile Picture
test.download_profile(acc, profile_pic_only=True)


#Just enter the UserName and here you go. The picture will be downloaded and can be viewed
