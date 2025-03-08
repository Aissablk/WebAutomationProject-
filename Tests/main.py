from selenium import webdriver

if  __name__="__main__":
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login") 
     login_page = Login(driver)
     login_page.enter_user("John Doe")
     login_page.enter_password("ThisIsNotAPassword")
     login_page.login_button
     
    driver.quit()