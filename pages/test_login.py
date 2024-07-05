import driver
from selenium.webdriver.common.by import By
from pages import test_landingpage
class login():
    def __int__(self, driver):
        self.driver=driver
    def test_login(self,driver):
        self.driver=driver

        login = self.driver.find_element(By.XPATH, "(//a[normalize-space()='Login'])").click()
        un = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username'][value='John Doe']").get_attribute(
            "value")
        up = self.driver.find_element(By.XPATH, "//input[@value='ThisIsNotAPassword']").get_attribute("value")
        uname = self.driver.find_element(By.XPATH, ("//input[@id='txt-username']"))
        uname.send_keys(un)
        pasword = self.driver.find_element(By.XPATH, "//input[@id='txt-password']")
        pasword.send_keys(up)
        ##CLICK ON LOGIN BUTTON
        self.driver.find_element(By.XPATH, "//button[@id='btn-login']").click()