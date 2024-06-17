import requests
import json,time
from PIL import Image,ImageDraw,ImageFont
from sendDing.SSHConnection import RemoteFileHandler

data=time.strftime('%Y%m%d',time.localtime())
text=data+"日报推送"
png_dir=f'./{data}.png'

def draw_data(text):
    bg_colors='#2898bd'
    word_colors = '#ffe6d0'
    xy=(5,0)
    image=Image.new("RGB",(200,50),color=bg_colors)
    draw_table=ImageDraw.Draw(im=image)
    draw_table.text(xy,text=text,fill=word_colors,font=ImageFont.truetype("STZHONGS.TTF",20))
    image.save(png_dir)

draw_data(text)
webhoke_url = "https://oapi.dingtalk.com/robot/send?access_token=55a0eb974ba5ad9d64d85e0487c7813126106e860ca9f86b6a984a9d58493d3b"
link1="www.baidu.com"


data = {
    "msgtype": "markdown",
    "markdown": {
        "title": "闪葱订单数据",
        "text": "![这是图片](./s.png)"+"\n"+
        f"[百度链接]({link1})"
    }
}
payload = json.dumps(data)
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("POST", webhoke_url, headers=headers, data=payload)

print(response.text)
