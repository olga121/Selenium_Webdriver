import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture
def driver(request):
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser': 'ALL'}
    wd = webdriver.Chrome(desired_capabilities=d)
    request.addfinalizer(wd.quit)
    return wd


def test_browser_log_checkin(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.implicitly_wait(5)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
#   open Catalog of goods
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.button")))
    elements = driver.find_elements_by_css_selector("table.dataTable a:not([title=Edit]")
    for i in range(3, len(elements)):
        elements[i].click()
        driver.find_element_by_css_selector("button i.fa.fa-times").click()
        # print messages
        for entry in driver.get_log('browser'):
            print(entry)
        elements = driver.find_elements_by_css_selector("table.dataTable a:not([title=Edit]")



#logs = driver.get_log('browser')
#messages = map(lambda l: l['message'], logs)
#has_console_logs = any(map(lambda m: m.find('console log') >= 0, messages))
#print('Success' if has_console_logs else 'Failure')
#driver.quit()
#When the chrome driver is used the console log message is found in the list of browser messages (has_console_log is True).
