from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
  
driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
    
elemento = driver.find_element(By.NAME, "q")
elemento.send_keys("Facebook")
elemento.send_keys(Keys.RETURN)

time.sleep(2)

elemento = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//h3[@class='LC20lb MBeuO DKV0Md'][contains(.,'Facebook - Inicia sesión o regístrate')]"))) .click()
print("Test Passed: 'Facebook - Log In or Sign Up' found in search results")

time.sleep(2)

driver.close()