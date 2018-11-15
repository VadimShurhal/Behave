import random
from selene import browser, config
from selene.browsers import BrowserName
from selene.support import by
from selene.support.conditions import have
from selene.support.jquery_style_selectors import s, ss

config.browser_name = BrowserName.CHROME

class Google():

    def __init__(self):
        pass

    def open_site(self):
        browser.open_url('https://www.google.com.ua')
        return self

    def set_text(self):
        s('#lst-ib').send_keys('python + behavior').press_enter()
        return self

    def see_list(self):
        url = browser.driver().current_url
        assert 'search' in url
        return self

