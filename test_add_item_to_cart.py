import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import random


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def is_element_present(self, selector):
    try:
        self.find_element_by_css_selector(selector)
    except NoSuchElementException:
        return False
    return True


def test_add_item_to_cart(driver):
    driver.get("http://localhost/litecart/en/")
    driver.implicitly_wait(5)
    count = driver.find_element_by_css_selector("span.quantity").get_attribute("innerText")
    while ( int(count) < 3 ):
#   choose an item
        random.choice(driver.find_elements_by_css_selector("img.image")).click()
#   check if there are additional options to choose
        if is_element_present(driver, "select"):
            Select(driver.find_element_by_css_selector("select")).options[1].click()
# add item to the cart
        driver.find_element_by_css_selector("[name=add_cart_product]").click()
#   wait for cart quantity update
        count = int(count)+1
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(count)))
#   back to home page
        driver.find_element_by_css_selector("nav#breadcrumbs a").click()
#   open the cart
    driver.find_element_by_css_selector("span.quantity").click()
#   find first item in a row
    driver.find_element_by_css_selector("a.inact").click()
    for i in range(len(driver.find_elements_by_css_selector("a.inact"))):
#   find item's quantity
        quantity = driver.find_elements_by_css_selector("[name=quantity]")[0].get_attribute("value")
#   find item identificator in the table
        item = driver.find_elements_by_css_selector("td.item")[0]
#   delete item
        driver.find_elements_by_css_selector("[name=remove_cart_item]")[0].click()
#   wait for table update
        WebDriverWait(driver, 10).until(EC.staleness_of(item))
        if int(quantity) > 1:
            i = i + int(quantity)










