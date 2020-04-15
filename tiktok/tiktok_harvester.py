import urllib.request
import requests
from bs4 import BeautifulSoup as bs

session = requests.Session()
session.headers.update({'User-Agent': 'Custom user agent'})


def get_video(url, name="your_video_name.mp4"):
	parent = bs(session.get(url).text, features="html5lib") 
	urllib.request.urlretrieve(parent.find("video")["src"], name)

#### url to tiktok page
url = "https://www.tiktok.com/@meladoodle/video/6809848869178838277"

### file name you want
name =  "meladoodle_1.mp4"


get_video(url, name)