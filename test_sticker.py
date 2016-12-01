import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/")
    driver.implicitly_wait(10)
    sticker_number = len(driver.find_elements_by_xpath("//div[contains(@class,'sticker')]"))
    product_number = len(driver.find_elements_by_xpath("//*[contains(@href,'products')]"))
    assert sticker_number == product_number

    