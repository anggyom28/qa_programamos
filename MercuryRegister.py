from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/newtours/")
driver.maximize_window()
driver.execute_script("window.scrollTo(0,500)")


button = driver.find_element(By.LINK_TEXT,"REGISTER") .click()
time.sleep(2)

email = driver.find_element(By.XPATH, "//input[contains(@id,'email')]") .send_keys("anggy0428@gmail.com")
time.sleep(2)

password = driver.find_element(By.XPATH, "//input[contains(@name,'password')]") .send_keys("a123456")
time.sleep(2)

confirmPassword = driver.find_element(By.XPATH, "//input[contains(@name,'confirmPassword')]") .send_keys("a123456")
time.sleep(2)

button = driver.find_element(By.XPATH,"//input[@src='images/submit.gif']") .click()
time.sleep(2)

confirmationMessage = driver.find_element(By.XPATH,"//b[contains(.,'Note: Your user name is anggy0428@gmail.com')]")
driver.close()