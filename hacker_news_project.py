import requests
from bs4 import BeautifulSoup
import pprint #PREETY PPRINT BUILTIN MODULE

res = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(res.text, "html.parser")

link = soup.select(".titleline")
subtext = soup.select(".subtext")


def sort_by_votes(hnlist):
    return sorted(hnlist,key=lambda k:k['votes'],reverse = True)

def custom_hn(links,subtext):
    hn = []
    for idx,item in enumerate(links):
        title = item.getText()
        href = item.select('a',None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points",""))
            if points > 99:
                hn.append({'title':title,'link':href,'votes':points})
    return sort_by_votes(hn)



pprint.pprint(custom_hn(link,subtext))