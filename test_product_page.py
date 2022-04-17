from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import Page_Object


def test__guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser,link)
    page.open()
    x =  Page_Object(browser,link)
    x.add_to_basket()
    x.solve_quiz_and_get_code()

