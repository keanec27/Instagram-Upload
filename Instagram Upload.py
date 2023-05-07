from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time, urllib.request
import pyautogui
import requests
import os 
import keyboard

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.instagram.com/")
pas="" #password
time.sleep(3)
username=driver.find_element(By.CSS_SELECTOR,"input[name='username']")
password=driver.find_element(By.CSS_SELECTOR,"input[name='password']")
username.clear()
password.clear()
username.send_keys("b_tester_1")
password.send_keys(pas)
login = driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

time.sleep(7)

not_now="/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button"
notnow=driver.find_element(By.XPATH,not_now).click()
noti_no="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"
notino=driver.find_element(By.XPATH,noti_no).click()

time.sleep(7)

post="/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[6]/div/div/a"
posting=driver.find_element(By.XPATH,post).click()
time.sleep(5)

but = ""
try:
    but = driver.find_element(By.XPATH, '//button[text()="Select From Computer"]').click()
except:
    but = driver.find_element(By.XPATH, '//button[text()="Select from computer"]').click()

time.sleep(3)
# USE PATH RELATIVE TO DEFAULT FOLDER
img_path="" #image path
keyboard.write(img_path)
keyboard.press_and_release("enter")

time.sleep(8)

but = driver.find_element(By.XPATH, '//button[text()="Next"]').click()

time.sleep(4)

but = driver.find_element(By.XPATH, '//button[text()="Next"]').click()

time.sleep(4)

#INSERT CAPTION 

cap=""   
caption=driver.find_element(By.CSS_SELECTOR,"textarea[placeholder='Write a caption...']")
caption.clear()
caption.send_keys(cap)

time.sleep(4)
but = driver.find_element(By.XPATH, '//button[text()="Share"]').click()

time.sleep(300)





