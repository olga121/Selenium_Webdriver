import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from unittest import TestCase


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def is_element_present_by_xpath(self, xpath):
    try:
        self.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.implicitly_wait(5)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver,10).until(EC.title_is("My Store"))
    select = driver.find_elements_by_css_selector("ul#box-apps-menu li#app-")
    for x in range(0,len(select)):
        select[x].click()
        assert(is_element_present_by_xpath(driver,"//img[contains(@title,'My Store')]"))
        select = driver.find_elements_by_css_selector("ul#box-apps-menu li#app-")
        drop_menu = select[x].find_elements_by_css_selector("ul.docs li")
        if len(drop_menu) > 0:
            for y in range(0, len(drop_menu)):
                drop_menu[y].click()
#                is_element_present_by_xpath(driver,"//img[contains(@title,'My Store')]")
                select = driver.find_elements_by_css_selector("ul#box-apps-menu li#app-")
                drop_menu = select[x].find_elements_by_css_selector("ul.docs li")










