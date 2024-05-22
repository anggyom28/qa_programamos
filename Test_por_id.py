from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

name = driver.find_element(By.ID, "userName")
name.send_keys("anggy")
time.sleep(2)

email = driver.find_element(By.ID, "userEmail") .send_keys("Ang8@gmail.com")
time.sleep(2)

current_address = driver.find_element(By.ID, "currentAddress") .send_keys("suiza")
time.sleep(2)

permanent_address = driver.find_element(By.ID, "permanentAddress") .send_keys("cualquier cosa")
time.sleep(2)

#comando para hacer scroll
# driver.execute_script("window.scrollTo(0,250")
# time.sleep(2)

button = driver.find_element(By.ID, "submit") .click()
time.sleep(2)
driver.close()
