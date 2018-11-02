class SearchHelper:
    def __init__(self, app):
        self.app = app

    def get_dropdown_search_list(self):
        wd = self.app.wd
        dropdown_search_list = list()
        for element in wd.find_elements_by_css_selector("li[class='suggest2-item i-bem suggest2-item_js_inited']"):
            text = element.text
            dropdown_search_list.append(text)
        return dropdown_search_list

    def get_results_list(self):
        wd = self.app.wd
        results_list = list()
        for element in wd.find_elements_by_css_selector("div[class='organic__url-text']"):
            text = element.text
            results_list.append(text.lower())
        return results_list

    def search_for_text(self, search_text):
        wd = self.app.wd
        wd.find_element_by_id("text").click()
        wd.find_element_by_name("text").clear()
        wd.find_element_by_name("text").send_keys(search_text)
        wd.find_element_by_css_selector("button[role='button']").click()

    def enter_text(self, search_text):
        wd = self.app.wd
        wd.find_element_by_id("text").click()
        wd.find_element_by_name("text").clear()
        wd.find_element_by_name("text").send_keys(search_text)