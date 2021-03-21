         # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         #█░██░███░▄▄█░▄▄▀█░▄▄▀█▀▄▄▀█░██░█░▄▄▀██▄████░▄▀██▄██░▄▀███▄░▄█░████░▄▄▀█▄░▄
         #█░██░███░▄▄█░██░█░██░█░██░█░██░█░▀▀▄██░▄███░█░██░▄█░█░████░██░▄▄░█░▀▀░██░█ <<< u/ennouri did that
         #██▄▄▄███▄▄▄█▄██▄█▄██▄██▄▄███▄▄▄█▄█▄▄█▄▄▄███▄▄██▄▄▄█▄▄█████▄██▄██▄█▄██▄██▄█
         #▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

#hope u enjoyed this little script i did, to support me; u can donate:
# BITCOIN: bc1qne5um5g8yw87jvet20yt8yvkkkzxjhazmvavda
# DOGECOIN (to the moon btw): DSAbPC7hPmYWUuAPffRvzTWEDDnTab9C42
# LITECOIN:LRHnRj92ngfC4Fo2R2ZArNSTZ9qkjDmQm9

from selenium import webdriver
driver= webdriver.Chrome("chromedriver.exe")
TARGET = 'replace me i am usless' #replace the text 'replace me i am useless" with the target email
driver.get('https://www.nbc26.com/account/manage-email-preferences')

user_input = driver.find_element_by_id('id_email')
user_input.send_keys(TARGET)
gh = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[3]/fieldset/div/div[1]/h2')
gh.click()
close = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]')
close.click()
import time 
time.sleep(1)
news = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[3]/fieldset/div/div[2]/div/div[1]/input')
news.click()
import time 
time.sleep(1)
news2 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[3]/fieldset/div/div[2]/div/div[2]')
news2.click()
import time 
time.sleep(1)
news3 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[3]/fieldset/div/div[2]/div/div[3]')
news3.click()
import time 
time.sleep(1)
news4 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[3]/fieldset/div/div[2]/div/div[4]')
news4.click()
import time 
time.sleep(1)
news5 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[3]/fieldset/div/div[2]/div/div[5]')
news5.click()
import time 
time.sleep(1)
news6 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[3]/fieldset/div/div[2]/div/div[6]')
news6.click()


import time 
time.sleep(2)

login_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[3]/div/input')
login_button.click()

