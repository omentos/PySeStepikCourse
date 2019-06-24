import math
import time
import pytest
from selenium import webdriver

ids = [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


def answer():
    return math.log(int(time.time()))


@pytest.mark.parametrize('id', ids)
def test_alien_message(browser, id):
    link = f"https://stepik.org/lesson/{id}/step/1"
    aw = str(answer())
    browser.get(link)
    browser.find_element_by_tag_name('textarea').send_keys(aw)
    browser.find_element_by_css_selector('button.submit-submission').click()
    hint = browser.find_element_by_css_selector('.smart-hints__hint')
    result = hint.text

    assert result == 'Correct!', f"Ответ '{aw}' не верен. Результат: '{result}'"
