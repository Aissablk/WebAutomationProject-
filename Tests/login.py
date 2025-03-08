from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys


class Loggin :
    def __init__(self,driver):
    self.driver=driver
    self.username=(By.ID,"username")
    self.password=(By.ID,"password")
    self.loggin=(By.ID,"loggin") 
    
    def enter_user(self,user):
        self.driver.find_element(*self.username).send_keys(user) 
    def enter_password(self,passwd):
        self.driver.find_element(*self.password).send_keys(passwd)
    def login_button(self,login):
        login_button_action=self.driver.find_element(*self.loggin)
        ActionChains(self.driver)\
            .move_to_element(login_button_action)\
            .click_and_hold()\
            .pause(1)\
            .release()\
            .perform() 