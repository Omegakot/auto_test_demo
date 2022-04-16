
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket(browser):
    browser.get(link)
    basket_btn = browser.find_element_by_id("add_to_basket_form")

    assert basket_btn is not None, "Элемент найден"
    
