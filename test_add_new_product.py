import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_add_new_product(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.implicitly_wait(5)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
#   open Catalog
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
#   click on "add new product" button
    driver.find_elements_by_css_selector(("a.button"))[1].click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@title,'My Store')]")))
#   competing fields of new product
#   Status - radio button
    driver.find_element_by_xpath("//input[@type='radio' and @value='1']").click()
#   Name
    name = "White duck"
    driver.find_element_by_xpath("//input[@name='name[en]']").send_keys(name)
#   Code
    driver.find_element_by_xpath("//input[@name='code']").send_keys("rd005")
#   Uncheck categories
    driver.find_element_by_xpath("//input[@name='categories[]' and @value='0']").click()
#   Check - Rubber Ducks
    driver.find_element_by_xpath("//input[@name='categories[]' and @value='1']").click()
#   Product Groups
    driver.find_element_by_xpath("//input[@name='product_groups[]' and @value='1-2']").click()
#   Quantity
    driver.find_element_by_css_selector(("[name=quantity]")).send_keys("7")
#   Quantity Unit
    driver.find_element_by_xpath(("//select[@name='quantity_unit_id']/option[@value='1']")).click()
#   Delivery Status
    driver.find_element_by_xpath(("//select[@name='delivery_status_id']/option[@value='1']")).click()
#   Date valid from
    driver.find_element_by_xpath(("//input[@name='date_valid_from']")).send_keys("12172016")
#   Date valid To
    driver.find_element_by_xpath(("//input[@name='date_valid_to']")).send_keys("12212016")
#   Save
#    driver.find_element_by_css_selector("[name=save]").click()
#   Tab Information
    driver.find_element_by_xpath("//a[@href='#tab-information']").click()
#   Manufacturer
    driver.find_element_by_xpath("//select[@name='manufacturer_id']/option[@value='1']").click()
#   Keywords
    driver.find_element_by_css_selector("[name=keywords]").send_keys('White')
#   Short description
    driver.find_element_by_xpath("//input[@name='short_description[en]']").send_keys("White duck")
#   Save
#    driver.find_element_by_css_selector("[name=save]").click()
#   Tab Prices
    driver.find_element_by_xpath("//a[@href='#tab-prices']").click()
#   Purchase price
    driver.find_element_by_css_selector("[name=purchase_price]").send_keys('2')
#   Currency code
    driver.find_element_by_xpath("//select[@name='purchase_price_currency_code']/option[@value='USD']").click()
#   Save
    driver.find_element_by_css_selector("[name=save]").click()
#   open Catalog - Rubber Ducks
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    assert(driver.find_element(By.LINK_TEXT, name))







