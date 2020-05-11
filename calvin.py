from bs4 import BeautifulSoup
import requests
import tweepy
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from os import environ

CONSUMER_KEY = environ['consumer_key']
CONSUMER_SECRET = environ['consumer_secret']
ACCESS_TOKEN = environ['access_token']
ACCESS_TOKEN_SECRET = environ['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def getRandomPage():
    page = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(page.content, 'html.parser')
    head = soup.findAll('h1')[0]
    name = head.contents[0]
    return name



def splitName(name):
    title = ""
    linecount = 0
    if (len(name) > 21):
        list = name.split()
        for i in range (0 ,len(list)):
                if linecount == 0:
                    title += list[i]
                    linecount += len(list[i])
                elif (linecount + len(list[i])>21):
                    title += '\n'
                    title += list[i]
                    linecount = len(list[i])
                else:
                    title += " " + list[i]
                    linecount+= len(list[i])
    else:
        title = name
    return title

def getLocation(draw,text,font):
    length, height = draw.textsize(text, font=font)
    half = length/2
    location = 780-half
    return location


def drawFile():
    img = Image.open("images/BadBoyCalvin.jpg")
    draw = ImageDraw.Draw(img)
    return draw,img

def addText(img, draw, text, location, font):
    draw.text((location,520),text,font=font)
    img.save('sample-out.jpg')
    return

def calvin():
    name = getRandomPage()
    while(not isinstance(name, str)):
        name = getRandomPage()
    text = splitName(name)
    font = ImageFont.truetype("arial.ttf",35)
    draw, img = drawFile()
    location = getLocation(draw,text, font)
    addText(img,draw,text, location, font)
    api.update_with_media("sample-out.jpg")
    return


calvin()