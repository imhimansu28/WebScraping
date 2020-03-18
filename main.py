import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
link = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hmlist):
    return sorted(hmlist, key=lambda k:k['votes'])

def create_custom_hn(link, subtext):
    hn = []
    for inx, item in enumerate(link):
        
        title = link[inx].getText()
        href = link[inx].get('href', None)
        votes = subtext[inx].select('.score')
        if len(votes):
            point = int(votes[0].getText().replace(' points', ''))
            if point > 99:
                hn.append({'title':title, 'href':href , 'votes':point})
    return sort_stories_by_votes(hn)
    
pprint.pprint(create_custom_hn(link, subtext))
