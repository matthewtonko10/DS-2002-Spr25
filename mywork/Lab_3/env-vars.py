#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

import os

os.environ["FAV_SPORT"] = "Basketbal"
os.environ["FAV_COLOR"] = "Blue"
os.environ["NAME"] = "Matt"

FAV_SPORT = input('What is your favorite sport?')
FAV_COLOR = input('What is your favorite color?')
NAME = input('What is your name?')

os.environ["USER_FAV_SPORT"] = FAV_SPORT
os.environ["USER_FAV_COLOR"] = FAV_COLOR
os.environ["USER_NAME"] = NAME

print(os.getenv("USER_FAV_SPORT"))
print(os.getenv("USER_FAV_COLOR"))
print(os.getenv("USER_NAME"))

