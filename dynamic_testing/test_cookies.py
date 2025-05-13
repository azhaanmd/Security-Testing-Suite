from playwright.sync_api import Page
import pytest
URL = "https://github.com/"

# Helper function to check if cookies have the expected flags
def check_cookie_flags(cookie, expected_flags):
    for flag, expected_value in expected_flags.items():
        if cookie.get(flag) != expected_value:
            pytest.fail(f"Cookie {cookie['name']} failed {flag} check. Expected {expected_value}, found {cookie.get(flag)}.")



# Test case for Secure flag
def test_secure_cookie(new_context):
    cookies = new_context.cookies(URL)  # Get all cookies set by the page
    print(cookies)
    for cookie in cookies:
        check_cookie_flags(cookie, {"Secure": True})  # Check if 'Secure' flag is set to True

# Test case for HttpOnly flag
def test_http_only_cookie(new_context):
    cookies = new_context.cookies(URL)  # Get all cookies set by the page

    for cookie in cookies:
        check_cookie_flags(cookie, {"HttpOnly": True})  # Check if 'HttpOnly' flag is set to True

# Test case for SameSite flag
def test_samesite_cookie(new_context):
    cookies = new_context.cookies(URL)  # Get all cookies set by the page

    for cookie in cookies:
        check_cookie_flags(cookie, {"SameSite": "Strict"})  # Check if 'SameSite' is set to 'Strict'

