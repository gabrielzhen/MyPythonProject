from selenium import webdriver
browser=webdriver.Chrome()
browser.get('http://gmail.com')
emailElem=browser.find_element_by_id('Email')
emailElem.send_keys('523231019@qq.com')
passwordElem=browser.find_element_by_id('p')
passwordElem.send_keys('Ztj.870418')