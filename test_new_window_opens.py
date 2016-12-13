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


def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.implicitly_wait(5)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
#   open Countries
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.button")))
#   open a country
    random.choice(driver.find_elements_by_css_selector("tr.row td:nth-of-type(5) a")).click()
#   number of links leading to new windows
    select = driver.find_elements_by_css_selector("i.fa.fa-external-link")
    for i in range(len(select)):
        select[i].click()
#   wait until new window opens
        WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) == 2)
        driver.switch_to_window(driver.window_handles[1])
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        select = driver.find_elements_by_css_selector("i.fa.fa-external-link")