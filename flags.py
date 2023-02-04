import os
import requests
from time import sleep
from bs4 import BeautifulSoup

data = []


def scrape_block():
    # the URL of the web page that we want to get flag data
    api_url = "https://www.sport-histoire.fr/en/Geography/Flags_of_the_world.php"
    # HTTP headers used to send a HTTP request
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0'
    }
    # Pauses for 0.5 seconds before sending the next request
    sleep(0.5)
    # send the request to get data in the webpage
    response = requests.get(api_url, headers=headers)

 

    soup = BeautifulSoup(response.content, 'html.parser')
    for i, row in enumerate(soup.select('table tbody tr')):
        images = row.select('a img')
        text = row.get_text()
        url = ''
        if i <= 11:
            url = images[0]['src']
        elif i > 11 and len(images):
            url = images[0]['data-src']
            
# get image data and write to disk
        if len(url):
            img_data = requests.get('https://www.sport-histoire.fr' +
                                    url).content
            dir_path = os.path.dirname(os.path.realpath(__file__))
            with open(dir_path + "\\data\\" + text.lower() + '.jpg',
                      'wb') as handler:
                handler.write(img_data)
            print("Downloaded: ", text)
   

if __name__ == "__main__":  # entrance to the main function
    scrape_block()

