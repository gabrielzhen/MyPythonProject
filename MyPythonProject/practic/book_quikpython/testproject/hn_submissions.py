import requests
from operator import itemgetter
 url='https://hacker-news.firebaseio.com/v0/topstories.json'
 r=requests.get(url)
 print("Status code",r.status_code)

 submission_ids=r.json()
 submission_dircts=submission_ids[:20]