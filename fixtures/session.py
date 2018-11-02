class SessionHelper:
    def __init__(self, app):
        self.app = app

    def open_main_page(self, url):
        wd = self.app.wd
        wd.get(url)

    def destroy(self):
        wd = self.app.wd
        wd.quit()