import requests,bs4
example=open('example.html')
examplebeauty=bs4.BeautifulSoup(example)
elemt=examplebeauty.select('#author')
pelemt=examplebeauty.select('p')
print(elemt[0].getText())
print(pelemt[0].getText())
print(str(pelemt[0]))
print(pelemt[0].get('href'))
