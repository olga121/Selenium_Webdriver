import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def check_alphabetical_order(self, selector, attribute):
    elements = self.find_elements_by_css_selector(selector)
    previous_value = elements[0].get_attribute(attribute)
    for i in range(1, len(elements)):
        next_value = elements[i].get_attribute(attribute)
        if previous_value > next_value and next_value > "0":
            return False
        previous_value = next_value
    return True


def check_alphabetical_order_dropdown_menu(self, selector, attribute):
    element = Select(self.find_element_by_css_selector(selector))
    previous_value = "0"
    for i in range(1, len(element.options)):
        next_value = element.options[i].get_attribute(attribute)
        if previous_value > next_value and next_value > "0":
            return False
        previous_value = next_value
    return True


def test_click_through_countries(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.implicitly_wait(5)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get(" http://localhost/litecart/admin/?app=countries&doc=countries")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.button")))
    assert (check_alphabetical_order(driver, "tr.row td:nth-of-type(5)", "innerText"))
    zones = driver.find_elements_by_css_selector("tr.row td:nth-of-type(6)")
    for j in range(0, len(zones)):
        if zones[j].get_attribute("innerText") != "0":
            driver.find_elements_by_css_selector("tr.row td:nth-of-type(5) a")[j].click()
            assert(check_alphabetical_order(driver, "#table-zones td:nth-of-type(3)", "innerText"))
            driver.find_element_by_xpath("//a[contains(@href,'doc=countries')]").click()
            zones = driver.find_elements_by_css_selector("tr.row td:nth-of-type(6)")
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.button")))


def test_click_through_geo_zones(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.implicitly_wait(5)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get(" http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.button")))
    countries = driver.find_elements_by_css_selector("tr.row td:nth-of-type(3) a")
    for i in range(len(countries)):
        countries[i].click()
        assert (check_alphabetical_order_dropdown_menu(driver, "#table-zones td:nth-of-type(3) select", "innerText"))
        driver.find_element_by_css_selector("[href $=geo_zones]").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.button")))
        countries = driver.find_elements_by_css_selector("tr.row td:nth-of-type(3) a")






