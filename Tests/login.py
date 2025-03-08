import selenium from webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Loggin :
    def __init__(self,driver)
    self.driver=driver
    self.username=(By.ID,"username")
    self.password=(By.ID,"password")
    self.loggin=(By.ID,"loggin") 