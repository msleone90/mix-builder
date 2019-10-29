'''

Author: Michael Leone 
git: github.com/msleone90
mail: msleone90@gmail.com
Requirements: requests, BeautifulSoup

'''

import webbrowser

import requests
from bs4 import BeautifulSoup

# prompt user to enter a song title
input_func = None
try:
    input_func = raw_input('Enter a song to build a YouTube Mix: ')
except NameError:
    input_func = input('Enter a song to build a YouTube Mix: ')

query = input_func.replace(' ', '+')

# searches for the best video match
url = 'https://www.youtube.com/results?search_query=' + query
source = requests.get(url, timeout=5)
plain_text = source.text
soup = BeautifulSoup(plain_text, "html.parser")

# fetches the youtube video URL
videos = soup.findAll('div', {'class': 'yt-lockup-video'})
video = videos[0].contents[0].contents[0].contents[0]

# Uses the URL to build the mix
try:
    link = video['href']
    link_code = link.split('=')
    webbrowser.open('https://www.youtube.com' + link + "&list=RD" + link_code[1] + "&start_radio=1&t=1")
except KeyError:
    print("Couldn't find a video to build a mix, check your network or try another video")