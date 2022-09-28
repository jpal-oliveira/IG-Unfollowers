#See unfollowers
from instabot import Bot

import os 
import glob
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])
#Instatiate bot object
bot = Bot()

#Login
username = input("Username: ")
password = input("Password: ")
bot.login(username = username, password = password)

#Get non followers
non_followers = set(bot.following)-set(bot.followers)

for non_follower in non_followers:
    print(bot.get_username_from_user_id(non_follower))