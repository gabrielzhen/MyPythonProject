#!/user/bin/env python
from atexit import register
from re import compile
from threading import Thread 
from time import ctime
from urllib.request import urlopen

amzon='https://www.amazon.com/dp/'
isbns={
    '0132269937':'core python programming',
    '0132356139':'python web development with django'
}
def getranking(isbn):
    page=urlopen('%s%s'%(amzon,isbn))
    data=page.read()
    page.close()
    return data

def showranking(isbn):
    print('--- %r ranks: %s'%(isbns[isbn],getranking(isbn)))

def main():
    for isbn in isbns:
        showranking(isbn)

main()