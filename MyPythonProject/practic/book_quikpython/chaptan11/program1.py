from selenium import webdriver
import sys
#todo accept the paramater form the order
order=sys.argv[1:2] 
content=sys.argv[2:3]
#print (order)
#print(content)
#todo use seleuinm model to login the website
browser=webdriver.Chrome()
browser.get('http://mail.qq.com')
browser.switch_to.frame('login_frame')
#todo put the paramater into website and send
try:
    emailElem=browser.find_element_by_xpath('//*[@id='u']')
    emailElem.send_keys('523231019@qq.com')
    passwordElem=browser.find_element_by_name('password')
    passwordElem.send_keys('Ztj.870418')
    passwordElem.submit()
except:
    print('gogogo')