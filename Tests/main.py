from selenium import webdriver
from login import Loggin 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login") 
    login_page = Loggin(driver)
    login_page.enter_user("John Doe")
    login_page.enter_password("ThisIsNotAPassword")
    login_page.login_button
    
    try:
        # Wait for an element on the new page to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='col-sm-12 text-center']/h2"))
        )
        print("Login successful, new page loaded!")
    except Exception as e:
        print("Failed to load new page:", e)

    # You can add more actions here if needed

    time.sleep(5)  # Just to keep the browser open for a while
    driver.quit()