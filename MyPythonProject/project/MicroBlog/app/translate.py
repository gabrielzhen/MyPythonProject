import requests
from flask_babel import _ 
from app import app

def translate(text):
    data={'kw':text}
    r=requests.post('https://fanyi.baidu.com/sug',
                    data)
    if r.json()['errno']==0:
        return r.json()['data'][0]['v']
    else:
        return None