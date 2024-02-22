from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
import analyze


driver = webdriver.Chrome()
driver2 = webdriver.Chrome()

username = 'anupamsoni9691.6@gmail.com'
password = 'anupamsoni9691.6'


def login():
    driver.get('https://trendlyne.com/visitor/loginmodal/?next=/features/')
    time.sleep(2)
    driver.find_element(By.ID, 'id_login').send_keys(username)
    driver.find_element(By.ID, 'id_password').send_keys(password)
    driver.find_element(By.XPATH, '''//*[@id="login"]/div[5]/div[1]/div/form/div[3]/button''').click()

login()

driver.get("https://trendlyne.com/portfolio/superstar-shareholders/index/institutional/")
main_data = []


def get_superstar_data(superstar_url, superstar_name):
    driver2.get(superstar_url.replace('superstar-shareholders', 'bulk-block-deals').replace('latest/', ''))
    time.sleep(2)
    stocks = driver2.find_element(By.XPATH, '''//*[@id="bbdealTable"]/tbody''').find_elements(By.TAG_NAME, 'tr')
    count = 0
    for stock in stocks:
        count = count + 1
        if (stock.text != 'No trades match this criteria'):
            items = [r.text for r in stock.find_elements(By.TAG_NAME, 'td')]
            # print(items)
            items.append(superstar_name)
            main_data.append(items)
        # if count > 5:
        #     break


time.sleep(2)
count_ss = 0
for page in range(0, 6):
    for row in driver.find_element(By.XPATH, '''//*[@id="groupTable"]/tbody''').find_elements(By.TAG_NAME, 'tr'):
        superstar = row.find_elements(By.TAG_NAME, 'td')[0].find_element(By.TAG_NAME, 'a')
        superstar_url = superstar.get_attribute('href')
        superstar_name = superstar.text
        print(superstar_name)
        try:
            get_superstar_data(superstar_url, superstar_name)
        except:
            print('error')
            pass
        count_ss = count_ss + 1
        # if count_ss > 2:
        #     break
    driver.find_element(By.ID, 'groupTable_next').find_element(By.TAG_NAME,'a').click()
header = ['stock','client','market','type','action type',	'Date',	'avg','count','change', 'superstar']
df = pd.DataFrame(main_data)
df.to_csv("latest_data.csv", header=header, index=False)

time.sleep(2)
analyze.main()
