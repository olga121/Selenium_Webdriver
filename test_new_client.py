import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_new_client(driver):
    driver.get("http://localhost/litecart/en/")
    driver.implicitly_wait(20)
#   open new contact form
    driver.find_elements_by_css_selector(("[href $=create_account]"))[0].click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@title,'My Store')]")))
#   fill contact form
    change_field_value(driver, "tax_id", "tax_id")
    change_field_value(driver, "company", "company")
    change_field_value(driver, "firstname", "firstname")
    change_field_value(driver, "lastname", "lastname")
    change_field_value(driver, "address1", "address1")
    change_field_value(driver, "address2", "address2")
    change_field_value(driver, "postcode", "postcode")
    change_field_value(driver, "city", "city")
    change_field_value(driver, "email", "email4@email.ru")
    verify_email_addres("email4@email.ru")
    change_field_value(driver, "phone", "123456789")
    change_field_value(driver, "password", "contact.password")
    change_field_value(driver, "confirmed_password", "contact.password")
    driver.find_element_by_xpath("//select[@name='country_code']/option[text()='Albania']").click()
#   submit the form
    driver.find_element_by_name("create_account").click()
#   logout
    driver.find_elements_by_css_selector(("[href $=logout]"))[0].click()
#   login
    change_field_value(driver, "email", "email4@email.ru")
    change_field_value(driver, "password", "contact.password")
    driver.find_elements_by_css_selector(("[name='login']"))[0].click()
#   logout
    driver.find_elements_by_css_selector(("[href $=logout]"))[0].click()


def change_field_value(self, field_name, text):
    if text is not None:
        self.find_element_by_name(field_name).click()
        self.find_element_by_name(field_name).clear()
        self.find_element_by_name(field_name).send_keys(text)

def verify_email_addres(email):
    addressToVerify = email
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
    if match == None:
        print('Bad Syntax')
        raise ValueError('Bad Syntax')
