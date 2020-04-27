import time
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_bag_button_exists(browser):
    browser.get(link)
    time.sleep(30)
    try:
        btn_add_to_bag = browser.find_element_by_class_name("btn-add-to-basket")
        result = True
    except NoSuchElementException:
        result = False
    assert result is True, "Button is not found!"
