import requests

# We're testing a real website to see if it uses security headers that protect users.
# You can replace this with any site you want to audit.
URL = "https://www.github.com"

# Test 1: Check Content-Security-Policy
def test_content_security_policy():
    """
    This header protects the site from XSS attacks (Cross-Site Scripting).
    It tells the browser which scripts are allowed and blocks dangerous ones.
    """
    response = requests.get(URL)
    csp = response.headers.get("Content-Security-Policy")
    assert csp is not None, "Missing Content-Security-Policy header. Site may be vulnerable to XSS."

# Test 2: Check X-Frame-Options
def test_x_frame_options():
    """
    This header prevents clickjacking attacks.
    It blocks the site from being embedded in iframes on other websites.
    """
    response = requests.get(URL)
    x_frame = response.headers.get("X-Frame-Options")
    assert x_frame is not None, "Missing X-Frame-Options header. Site may be vulnerable to clickjacking."

# Test 3: Check X-Content-Type-Options
def test_x_content_type_options():
    """
    This header stops browsers from trying to guess file types (no MIME sniffing).
    Prevents sneaky file tricks from hackers.
    """
    response = requests.get(URL)
    x_content = response.headers.get("X-Content-Type-Options")
    assert x_content == "nosniff", "X-Content-Type-Options is missing or not set to 'nosniff'."

# Test 4: Check Strict-Transport-Security
def test_strict_transport_security():
    """
    This header tells browsers to always use HTTPS (secure connection).
    Helps prevent 'man-in-the-middle' attacks on public Wi-Fi.
    """
    response = requests.get(URL)
    hsts = response.headers.get("Strict-Transport-Security")
    assert hsts is not None, "Missing Strict-Transport-Security header. HTTPS may not be enforced."

# Test 5: Check Referrer-Policy
def test_referrer_policy():
    """
    This header controls what information (like URLs) the browser shares when navigating.
    Helps prevent leaking sensitive paths or tokens.
    """
    response = requests.get(URL)
    ref_policy = response.headers.get("Referrer-Policy")
    assert ref_policy is not None, "Missing Referrer-Policy. Sensitive info could be leaked via referrer."

# Test 6: Check Permissions-Policy
def test_permissions_policy():
    """
    This header restricts access to browser features (like camera, mic, location).
    Prevents abuse from malicious scripts or iframes.
    """
    response = requests.get(URL)
    permissions = response.headers.get("Permissions-Policy") or response.headers.get("Feature-Policy")
    assert permissions is not None, "Missing Permissions-Policy or Feature-Policy. Feature abuse possible."
