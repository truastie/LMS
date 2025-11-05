import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_context():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_context):
    browser = playwright_context.chromium.launch(headless=False, slow_mo=300)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()