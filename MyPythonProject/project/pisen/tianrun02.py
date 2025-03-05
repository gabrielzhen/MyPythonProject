import hashlib
import base64
 
def get_file_md5_base64(file_path):
    # 打开文件，读取数据
   #with open(file_path, 'rb') as file:
     #   data = file.read()
    
    # 计算MD5
    #md5 = hashlib.md5(base64.encode(file_path))
    file_bytes = file_path.encode('utf-8')
    md5 = hashlib.md5(file_bytes)
    
    # 获取128位的二进制数据
    md5_digest = md5.digest()
    
    # 对二进制数据进行Base64编码
    md5_base64 = base64.b64encode(md5_digest).decode('utf-8')
    print(md5_base64)
    return md5_base64
 
# 使用函数
file_path ='http://localhost:8069/odoo/deliveries/6?debug=1'  # 替换为你的文件路径
md5_base64_encoded = get_file_md5_base64(file_path)