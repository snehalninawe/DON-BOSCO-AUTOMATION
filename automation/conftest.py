import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.maximize_window()
    
    # Implicit Wait
    driver.implicitly_wait(10)
    driver.get("https://devops.evolutionco.in/nextgen/")
    
    username = driver.find_element(By.NAME,"email")
    username.send_keys("admin@evolutionco.com")
        
    password = driver.find_element(By.NAME,"password")
    password.send_keys("evoxdbit@1234")
        
    loginBtn=driver.find_element(By.XPATH,"//input[@type='submit']")
    loginBtn.click()
    
    time.sleep(3)
    dropdown = driver.find_element(By.XPATH,"(//div[contains(@class,'nice_Select bgLess mb-0 infix_session')])[1]")
    
    dropdown.click()
    
    time.sleep(1)
    
    options = dropdown.find_element(By.XPATH, ".//li[normalize-space()='2026-2027 test2']")
    
    options.click()
    time.sleep(5)
    
    yield driver
    time.sleep(5)
    driver.quit()
    

    