import pytest
from selenium import webdriver
#used fixture decorater to make use of setup() function on class level of test case page by use of "marker" decorater
@pytest.fixture(scope="class")
#def setup() work with teardown and using "request" fixture as argument to use same driver in other pages
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    #driver.save_screenshot("homePage.png")
    #invoked driver will aggigned to request on class level
    request.cls.driver=driver
    #yield is used for teardown the flow
    yield
    driver.close()
