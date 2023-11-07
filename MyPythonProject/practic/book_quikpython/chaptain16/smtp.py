import smtplib
smtpObj=smtplib.SMTP('smtp-mail.outlook.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('zhengtingjun@live.cn','aaaaaaa')
smtpObj.sendmail('zhengtingjun@live.cn','523231019@qq.com','Subject:so long \ndear ztj')
smtpObj.quit()