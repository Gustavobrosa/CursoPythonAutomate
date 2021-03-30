# wait learning
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get('http://google.com')

try:
    element = WebDriverWait(driver, 35).until(
        EC.presence_of_element_located((By.ID, "rrrog-pdq"))
    )
finally:
    driver.quit()
print ('até aqui OK')


##tsf > div:nth-child(2) > div.A8SBwf > div.FPdoLc.tfB0Bf > center > input.gNO89b


