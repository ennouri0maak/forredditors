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
# Edge service
from selenium.webdriver.edge.service import Service
# Edge Driver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from json import load

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
email = load(open('config.json'))['email']
username = email.split('@')[0][:15]
password = 'azerhd5#'

driver.get('https://www.adam4adam.com/')

field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "app_bundle_user_registration_type_username")))
field.send_keys(username)

field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "app_bundle_user_registration_type_email")))
field.send_keys(email)

field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "app_bundle_user_registration_type_plainPassword_first")))
field.send_keys(password)

field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "app_bundle_user_registration_type_plainPassword_second")))
field.send_keys(password)

field.submit()

import time
time.sleep(5)
