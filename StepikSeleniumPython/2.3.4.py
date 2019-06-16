import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'
driver = webdriver.Chrome()

driver.get(link)

driver.find_element_by_css_selector('button[type="submit"]').click()
driver.switch_to.alert.accept()

x = int(driver.find_element_by_id('input_value').text)
y = calc(x)

driver.find_element_by_id('answer').send_keys(y)

driver.find_element_by_css_selector('button[type="submit"]').click()


time.sleep(15)
driver.quit()
