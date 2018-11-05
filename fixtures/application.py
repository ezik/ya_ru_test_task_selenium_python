from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.chrome.options import Options
from fixtures.session import SessionHelper
from fixtures.search import SearchHelper

# This profile path is added to use firefox instance with suppressed mic prompt.
# In public version, username is removed due to security reasons
ff_profile = FirefoxProfile("/Users/<username>/Library/Application Support/Firefox/Profiles/zdzu0yrg.default")
chrome_profile = Options()
chrome_profile.add_argument("use-fake-device-for-media-stream")
chrome_profile.add_argument("use-fake-ui-for-media-stream")
chrome_profile.add_argument("--disable-notifications")
chrome_profile.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 1
            })


class Application:
    def __init__(self, browser):
        if browser == "firefox":
            self.wd = webdriver.Firefox(ff_profile)
        elif browser == "chrome":
            self.wd = webdriver.Chrome(options=chrome_profile)
        else:
            raise ValueError("Cannot recognize browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.search = SearchHelper(self)

    def open_page_by_locator(self, locator):
        wd = self.wd
        wd.find_element_by_css_selector(locator).click()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def url_contains(self, text):
        wait = WebDriverWait(self.wd, 10)
        return wait.until(ec.url_contains(text))

    def menu_item_present(self, text):
        wd = self.wd
        return len(wd.find_elements_by_xpath("//*[contains(text(), " + text + ")]")) > 0

    def element_is_displayed(self, css_selector):
        wd = self.wd
        return wd.find_element_by_css_selector(css_selector).is_displayed()




