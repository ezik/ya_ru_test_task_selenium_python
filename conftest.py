import pytest
from fixtures.application import Application

fixture = None
base_url = "https://ya.ru/"


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")

    if fixture is None or not fixture.is_valid():
        print("Fixture was created...")
        fixture = Application(browser=browser)
        fixture.session.open_main_page(base_url)
    return fixture


@pytest.fixture(scope="function", autouse=True)
def before(app):
    app.session.open_main_page(base_url)


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        print("Destroying fixture...")
        fixture.session.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
