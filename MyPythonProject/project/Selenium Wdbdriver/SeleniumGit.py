from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation
import pandas

option=webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
# Chrome浏览器
driver = webdriver.Chrome(options=option)
driver.get('https://github.com/collections/machine-learning')
projects=driver.find_elements(By.XPATH,"//h1[@class='h3 lh-condensed']")
project_list={}
for project in projects:
    proj_name=project.text
    proj_url=project.find_elements(By.XPATH,"a")[0].get_attribute('href')
    # print(proj_name,"----------",proj_url)
    project_list[proj_name]=proj_url
driver.close()

projuct_df= pandas.DataFrame.from_dict(project_list,orient='index')

# Manipulate the table
projuct_df['project_name'] = projuct_df.index
projuct_df.columns = ['project_url', 'project_name']
project_df = projuct_df.reset_index(drop=True)
print(projuct_df)
projuct_df.to_csv("github.csv")