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
# driver.find_element_by_id('robotCheckbox').click()
# el_radio_robot = driver.find_element_by_id('robotsRule')
# driver.execute_script('return arguments[0].scrollIntoView(true)', el_radio_robot)
# el_radio_robot.click()

driver.find_element_by_css_selector('button[type="submit"]').click()

# current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')
# print(file_path)
# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))

time.sleep(15)
driver.quit()
