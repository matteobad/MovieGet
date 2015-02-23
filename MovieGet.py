import requests
import re
import subprocess


URL = 'http://www.cb01.org/'
headers = {'User-Agent': 'Streamer 0.1',
           'Accept-Encoding': 'gzip, deflate'}

streaming = ['Backin', 'Cloudzilla', 'Firedrive', 'Moevideo',
             'Speedvideo', 'Videomega', 'Videopremium', 'Nowvideo']

Chrome = '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --kiosk '
def getSource(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text


def searchFilm(name='fight club'):
    if not name:
        name = input('Titolo del film: ->')

    url = URL+'?s='+name.replace(' ', '+')
    source = getSource(url)

    match = re.search(URL+name.replace(' ', '-')+'\S+/', source)
    result = []
    if match:
        source = getSource(match.group(0))
        for site in streaming:
            match = re.search(r'http.+'+site+'</a>', source)
            if match:
                result.append(match.group(0).replace('" target="_blank">'+site+'</a>', ''))

    for link in result:
        subprocess.call(Chrome+'"'+link+'"')
                

searchFilm()

    
        
