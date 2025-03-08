from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver=webdriver.Chrome()

driver.get('https://katalon-demo-cura.herokuapp.com/')

page_element=driver.find_element(By.ID,"btn-make-appointment")

ActionChains(driver)\
    .move_to_element(page_element)\
    .click_and_hold()\
    .pause(1)\
    .release()\ 
    .perform() 

time.sleep(3)  
driver.quit() 