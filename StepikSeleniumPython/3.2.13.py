from selenium import webdriver
import unittest

text = "test_text"
asserttext = "Поздравляем! Вы успешно зарегистировались!"


def registration(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)

    browser.find_element_by_css_selector("div.first_block input.first").send_keys(text)
    browser.find_element_by_css_selector("div.first_block input.second").send_keys(text)
    browser.find_element_by_css_selector("div.first_block input.third").send_keys(text)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

    browser.quit()

    return welcome_text


class testRegistration(unittest.TestCase):
    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        resulttext = registration(link)
        self.assertEqual(asserttext, resulttext, "Что-то пошло не так")

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        resulttext = registration(link)
        self.assertEqual(asserttext, resulttext, "Что-то пошло не так")


if __name__ == "__main__":
    unittest.main()
