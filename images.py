from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def startSearch():
    ##Initialize the search
    search = input('Search for:')
    params = {'q': search}
    ##Replaces spaces with unnderscores for url search
    dir_name = search.replace(' ', '_').lower()
    ##If a directory with the search term doesnt exist, make a directory for it
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    ## Get the url plugging in the provided search term as the parameter
    r = requests.get('http://www.bing.com/images/search', params=params)
    # Intialize the HTML soup
    soup = BeautifulSoup(r.text, 'html.parser')
    ## Parse the soup for all a tags with a class of thumb
    links = soup.findAll('a', {'class': 'thumb'})

    for item in links:
        try:
            ## Get the link of each a tag
            img_obj = requests.get(item.attrs['href'])
            print("getting", item.attrs['href'])
            title = item.attrs['href'].split('/')[-1]
            try:
                ## Get the image inside of the a tag
                img = Image.open(BytesIO(img_obj.content))
                ## Save that image in the directory
                img.save('./' + dir_name + '/' + title, img.format)
            except:
                print('could not save image')
        except:
            print("could not request Image")
    startSearch()

startSearch()

