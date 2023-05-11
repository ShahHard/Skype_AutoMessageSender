# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re

def driver():
    global driver 
    driver = webdriver.Chrome()

    
def test_untitled_test_case():
    driver()
    driver.get("https://www.skype.com/en/")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='customMeControl']/a[1]/span[1]").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Use Skype online").click()
    time.sleep(3)
    login_form = driver.find_element(By.XPATH, "//*[@id='i0281']")
    
    login_form.find_element(By.XPATH, "//*[@id='i0116']").click()
    login_form.find_element(By.ID, "i0116").send_keys("hard@elsner.com.au")
    time.sleep(3)
    driver.find_element(By.ID, "idSIButton9").click()
    driver.find_element(By.ID, "i0118").clear()
    driver.find_element(By.ID, "i0118").send_keys("Alpesh@shah14")
    time.sleep(3)
    driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(2)
    driver.find_element(By.ID, "idBtn_Back").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[3]/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div[1]/button").click()
    time.sleep(2)
    global Favorites_list
    Favorites_list = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div/div[1]/div/div/div[3]/div")

    
    for i in range(1, len(Favorites_list)+1):
        wait = WebDriverWait(driver, 10)
        get_profile = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div/div[1]/div/div/div[3]/div["+str(i)+"]")
        
        if get_profile.get_attribute('role') == "button":
            get_profile.click()
            message_field = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div")))           
            message_field.send_keys("Good Morning")
            
            #uncomment this If you want to send a message
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/button').click()




        
    

    
    """driver.get("https://login.live.com/ppsecure/post.srf?mkt=en-US&cobrandid=2befc4b5-19e3-46e8-8347-77317a16a5a5&id=293290&uaid=464f08016bbf4ebdbbbc2f3fa3616b40&client_flight=ReservedFlight33,ReservedFligh&pid=0&opid=4DFB9E7A45CA8D80&route=C107_BAY")
    driver.get("https://lw.skype.com/login/oauth/proxy?client_id=572381&redirect_uri=https%3A%2F%2Fweb.skype.com%2FAuth%2FPostHandler%3FopenPstnPage%3Dtrue&state=54cd7ad8-06ca-4dc9-865a-b38f4394b750&wa=wsignin1.0")
    driver.get("https://login.skype.com/login/microsoft?client_id=572381&redirect_uri=https%3A%2F%2Fweb.skype.com%2FAuth%2FPostHandler%3FopenPstnPage%3Dtrue&state=54cd7ad8-06ca-4dc9-865a-b38f4394b750")"""
    """ 
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
"""

