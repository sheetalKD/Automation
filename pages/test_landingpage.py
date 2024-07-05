import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.test_login import login
#added this page to pytest (reffer vedio 48 at 11:35)

#with the use of marke decorater calling setup fixture from conftest.py page
@pytest.mark.usefixtures("setup")
class Test_landing():
    def test_home(self):
        self.test_expender()
        lin= login()
        lin.test_login(self.driver)
        self.test_apointment()
        time.sleep(10)
        # driver.close()

    def test_expender(self):
        #self.driver = driver
        finder = self.driver.find_element(By.XPATH, "(//i[@class='fa fa-bars'])[1]")
        finder.click()
        time.sleep(5)

    def test_apointment(self):
        #self.driver = driver
        facility = self.driver.find_element(By.NAME, "facility")
        dd = Select(facility)
        dd.select_by_value("Seoul CURA Healthcare Center")
        ck = self.driver.find_element(By.XPATH, "(//input[@id='chk_hospotal_readmission'])[1]").click()
        radio = "Medicaid"
        self.driver.find_element(By.XPATH, f"//label[normalize-space()='{radio}']").click()
        req_date = "6/18/2024"
        date = self.driver.find_element(By.XPATH, "(//input[@id='txt_visit_date'])[1]").send_keys(req_date)

        self.driver.find_element(By.XPATH, "(//textarea[@id='txt_comment'])[1]").send_keys("Booking for testing")
        self.driver.find_element(By.ID, "btn-book-appointment").click()

        self.test_expender()
        self.test_history()

    def test_history(self):
        #self.driver = driver
        hist = self.driver.find_element(By.CSS_SELECTOR, "a[href='history.php#history']").click()

#as this file is used as pytest therefor no need to create object of class
# hom = Testlanding()
# hom.home()


