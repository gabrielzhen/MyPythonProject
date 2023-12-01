#图片加水印
import os
from PIL import Image,ImageDraw,ImageFont

def get_position(x,w,h):
    print(w-20,h-50)
    return w-20,h-50


def add_watermark(filename,font_size,text,font_opa,position_id):
    
    original_image=Image.open(filename).convert("RGBA")    
    draw=ImageDraw.Draw(original_image)
    font=ImageFont.truetype('Open-24-Display-St-1.ttf', font_size)
    #post=get_position(position_id,original_image.width,original_image.height)
    draw.text((10,10),text,font=font,fill=(200, 100, 200, 100))
    if not os.path.exists('watermark'):
        os.makedirs('watermark')
    outfilename='watermark/{}'.format(filename)
    print(outfilename)
    original_image.save(outfilename,'PNG')
    

if __name__=='__main__':
    text=input('输入水印文字')
    font_size=int(input('输入字体大小[20]:') or '20')
    font_opa=int(input('输入文字透明度[50]:') or '50')
    position_id=int(input('''输入文字位置：
    # 1: 左上, 2: 中上, 3: 右上
    # 4: 中左, 5: 正中, 6: 中右
    # 7: 左下, 8: 下中, 9: 右下'''))

    for f in os.listdir():
        if f.endswith('.png') or f.endswith('.jpg'):
            print('给%s增加水印'%format(f))
            add_watermark(f,font_size,text,font_opa,position_id)