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

username = 'bhjbdh555f' #replace the text 'replace me i am useless" with the username u want, for exemple: DICKLOVER699
TARGET = 'jxxibraxx7@baitify.com' #replace the text 'replace me i am useless" with the target email
driver.get('https://www.adam4adam.com/')
password = 'azerhd5#'
user_input = driver.find_element_by_xpath('/html/body/main/section[1]/div/div/div/form/div/div[1]/input')
user_input.send_keys(username)

user_input = driver.find_element_by_xpath('/html/body/main/section[1]/div/div/div/form/div/div[2]/input')
user_input.send_keys(TARGET)
import time
time.sleep(2)

user_input = driver.find_element_by_xpath('/html/body/main/section[1]/div/div/div/form/div/div[3]/input')
user_input.send_keys(password)
import time
time.sleep(2)
user_input = driver.find_element_by_xpath('/html/body/main/section[1]/div/div/div/form/div/div[4]/input')
user_input.send_keys(password)

sign = driver.find_element_by_xpath('/html/body/main/section[1]/div/div/div/form/button')
sign.click()
import time
time.sleep(3.5)
driver.quit()
