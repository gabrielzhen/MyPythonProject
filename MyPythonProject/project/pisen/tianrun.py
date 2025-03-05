import base64,hmac
from datetime import datetime,timezone
from unittest import skip
import urllib.parse
from hashlib import sha1
import pymysql

class DbConnect:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        connection = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                     database=self.database)
        return connection

    def query(self, sql):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def execute(self, sql):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        connection.close()

    def executemany(self, sql, data):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.executemany(sql, data)
        connection.commit()
        row_count = cursor.rowcount
        cursor.close()
        connection.close()
        print(f"执行影响的行数: {row_count}")

def urlencode_base64_hmac_sha1(access_key_secret, url_param):
    """
    计算 URLEncode(base64(hmac-sha1(AccessKeySecret, urlParam))).

    :param access_key_secret: 密钥（字符串）
    :param url_param: URL 参数（字符串）
    :return: 编码后的结果字符串
    """
    # 将密钥和参数转换为字节
    key = access_key_secret.encode('utf-8')
    message = url_param.encode('utf-8')
    # 使用 HMAC-SHA1 算法进行签名
    signature = hmac.new(key, message, sha1).digest()
    # 对签名结果进行 Base64 编码
    base64_signature = base64.b64encode(signature).decode('utf-8')
    #  base64_signature = base64.b64encode(signature).decode('utf-8')
    # 对 Base64 编码结果进行 URL 编码
    return base64_signature

def fullurl(title,method,main_path,url_set):
    domain='api-bj.clink.cn'
    accessid='bf6c0ed9f46ea03068ff6f2560510edb'
    accesskey='P4L9e21zwM4pc92A7G6t'
    expires=86400

    timestamp=datetime.now(timezone.utc)
    pub_set=f"AccessKeyId={accessid}&Expires={expires}&Timestamp={timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')}"
    pub_set_encode=f"AccessKeyId={accessid}&Expires={expires}&Timestamp={urllib.parse.quote(timestamp.strftime('%Y-%m-%dT%H:%M:%SZ'))}"
    # private set  需要decode
    if method=='GET' and len(url_set)>0:
        privite_set=''
        sorted_set={k: url_set[k] for k in sorted(url_set)}
        for key,value in sorted_set.items():
            privite_set=privite_set+'&'+urllib.parse.quote(key)+'='+urllib.parse.quote(value)
    else:
        privite_set=''

    print('url参数：'+privite_set)
    # union all set
    all_set=f"{method}{domain}{main_path}?{pub_set_encode}{privite_set}"
    # print(all_set)
    urlencoded_signature = urllib.parse.quote(urlencode_base64_hmac_sha1(accesskey,all_set),safe='')
    # urlencoded_signature = urlencode_base64_hmac_sha1(accesskey,all_set)
    print(urlencoded_signature)
    signature=f"&Signature={urlencoded_signature}"
    #令牌之前需要undecode  令牌不需要在undecode 拼接
    req_url=f"https://{domain}{main_path}?{pub_set_encode}{privite_set}"
    req_url=urllib.parse.unquote(req_url)
    req_url=f"{req_url}{signature}"
    print('----------------')
    print(req_url)
    print('----------------')
    t_db = DbConnect('192.168.6.115', 9030, 'admin', 'pisen1', 'Pisen_TMP')
    t_db.execute(f'insert into KeFu_Dapan values("{title}","{method}","{privite_set}","{req_url}")')

# public set
title='呼叫7日报表'
method='POST'
main_path='/cc/stat_new_queue'
url_set={
}
fullurl(title,method,main_path,url_set)

title='在线7日报表'
method='POST'
main_path='/livechat/stat_queue_period_list'
url_set={
}
fullurl(title,method,main_path,url_set)

url_set={
    'date':'20241207',
    'dateEnd':'20241207',
    'qnos':'1100,2004'
}

url_set={
    'startTime':'20241207',
    'endTime':'20241207',
    'qnos':'0001,0002,0003'
}