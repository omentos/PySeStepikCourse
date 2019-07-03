from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_busket_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert is_element_by_css_exist(browser,
                                   "form#add_to_basket_form > button[type='submit']"), print("basket button not found")


def is_element_by_css_exist(browser, css_selector):
    wait = WebDriverWait(browser, 5)
    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector)))
    return True if elements else False
