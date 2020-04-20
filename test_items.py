import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_bag(browser):
    browser.get(link)
    time.sleep(30)
    btn_add_to_bag = browser.find_element_by_class_name("btn-add-to-basket")
    assert btn_add_to_bag, 'Элемент не найден'
