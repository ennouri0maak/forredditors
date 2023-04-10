#!/usr/bin/env python3
         # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         #█░██░███░▄▄█░▄▄▀█░▄▄▀█▀▄▄▀█░██░█░▄▄▀██▄████░▄▀██▄██░▄▀███▄░▄█░████░▄▄▀█▄░▄
         #█░██░███░▄▄█░██░█░██░█░██░█░██░█░▀▀▄██░▄███░█░██░▄█░█░████░██░▄▄░█░▀▀░██░█ <<< u/ennouri did that
         #██▄▄▄███▄▄▄█▄██▄█▄██▄██▄▄███▄▄▄█▄█▄▄█▄▄▄███▄▄██▄▄▄█▄▄█████▄██▄██▄█▄██▄██▄█
         #▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

# hope u enjoyed this little script i did, to support me; u can donate:
# BITCOIN: bc1qne5um5g8yw87jvet20yt8yvkkkzxjhazmvavda
# DOGECOIN (to the moon btw): DSAbPC7hPmYWUuAPffRvzTWEDDnTab9C42
# LITECOIN:LRHnRj92ngfC4Fo2R2ZArNSTZ9qkjDmQm9

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from json import load

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
email = load(open('config.json'))['email']

driver.get('https://www.crosswalk.com/newsletters/')

input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'emailAddress')))
input.send_keys(email)

# Fancy hack to click all checkboxes
driver.execute_script("$(\"input[type='checkbox']\").click();")

button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'SubmitButton')))
button.click()

WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'Oswald'), 'Thank you for signing up!'))
