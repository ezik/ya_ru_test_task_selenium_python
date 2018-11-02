# -*- coding: utf-8 -*-


def test_yandex_logo_turns_to_yandex_site(app):
    app.open_page_by_locator("a[data-statlog='logo']")
    assert app.url_contains("yandex.ru")


def test_mail_link_turns_to_mail_site(app):
    app.open_page_by_locator("a[data-statlog='logout']")
    assert app.url_contains("mail.yandex.ru")


# This test intends to work stable in Firefox with profile, but works so-so in Chrome. At this point I think only proper
# profiling can solve situation. Added experimental options in Chrome profile, in application.py. It didn't help.
def test_mic_icon_click_turns_to_voice_search_popup(app):
    app.wd.find_element_by_css_selector("div[class='input__voice-search']").click()
    assert app.element_is_displayed("div[class='voice-search-popup__content']")





