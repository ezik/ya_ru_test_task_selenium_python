# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize("text", ["playrix", "gamedev", "homescapes"])
def test_search_for_text_returns_appropriate_results(app, text):
    app.search.search_for_text(text)
    assert app.menu_item_present("Поиск")
    # Filter is added to remove russian search results
    results_list = list(filter(lambda x: text in x, app.search.get_results_list()))
    print(results_list)
    assert len(results_list) > 0


@pytest.mark.parametrize("text", ["playrix", "game development"])
def test_dropdown_list_contains_search_text(app, text):
    app.search.enter_text(text)
    for row in app.search.get_dropdown_search_list():
        assert row.startswith(text)


def test_current_url_contains_search_text(app):
    search_term = "playrix"
    app.search.search_for_text(search_term)
    assert app.url_contains(search_term)

