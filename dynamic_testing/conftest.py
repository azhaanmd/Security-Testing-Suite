import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def new_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture(scope="module")
def new_context():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        yield context
        browser.close()
