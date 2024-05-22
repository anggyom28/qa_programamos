from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()


name = driver.find_element(By.XPATH, "//input[contains(@id,'userName')]")
name.send_keys("Anggy")
time.sleep(2)

email = driver.find_element(By.XPATH, "//input[contains(@id,'userEmail')]") .send_keys("Anggy0428@gmail.com")
time.sleep(2)

current_address = driver.find_element(By.XPATH, "//textarea[contains(@id,'currentAddress')]") . send_keys("Hola mundo")
time.sleep(2)

permanent_address = driver.find_element(By.XPATH, "//textarea[contains(@id,'permanentAddress')]") .send_keys("cualquier cosa")
time.sleep(2)

button = driver.find_element(By.XPATH,"//button[contains(@id,'submit')]") .click()
time.sleep(2)
driver.close()




