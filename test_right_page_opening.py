import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_page_opening(driver):
    driver.get("http://localhost/litecart/en/")
    driver.implicitly_wait(10)
    product_name_front = driver.find_element_by_css_selector("#box-campaigns div.name").get_attribute('innerText')
    regular_price_fr = driver.find_element_by_css_selector("#box-campaigns s.regular-price").get_attribute('innerText')
    campaign_price_fr = driver.find_element_by_css_selector("#box-campaigns strong.campaign-price").get_attribute(
        'innerText')
    driver.find_elements_by_css_selector("#box-campaigns a.link")[0].click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@title,'My Store')]")))
    product_name = driver.find_element_by_css_selector("#box-product h1").get_attribute('innerText')
    regular_price= driver.find_element_by_css_selector("#box-product s.regular-price").get_attribute('innerText')
    campaign_price= driver.find_element_by_css_selector("#box-product strong.campaign-price").get_attribute('innerText')
    assert (product_name_front == product_name)
    assert (regular_price_fr == regular_price)
    assert (campaign_price_fr == campaign_price)
