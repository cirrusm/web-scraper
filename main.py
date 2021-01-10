from bs4 import BeautifulSoup
import requests

search = input("Enter Search Term: ")
params = {'q': search}
r = requests.get('http://www.bing.com/search', params=params)

soup = BeautifulSoup(r.text, 'html.parser')
#searching for ol element, with id attribute of b_results
results = soup.find(f"ol", {'id' : "b_results"})
#searching for li element with b_algo class
links = results.findAll('li', {'class': 'b_algo'})

for item in links:
    item_text = item.find('a').text
    item_href = item.find('a').attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
        print("Parent:", item.find('a').parent.parent.find('p').text)

        children = item.find('h2')
        
        
