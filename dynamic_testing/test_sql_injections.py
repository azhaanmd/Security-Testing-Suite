import requests

def test_sql_injection_login():
    """
    Test SQL Injection on the login page of demo.testfire.net.
    Attempts to bypass authentication using a crafted SQL payload.
    """
    url = "https://demo.testfire.net/bank/login.jsp"

    # SQL Injection payload
    payload = {
        "uid": "' OR '1'='1",
        "passw": "anything",
        "btnSubmit": "Login"
    }

    try:
        # Send POST request with SQLi payload
        response = requests.post(url, data=payload, timeout=10)

        print(f"Status Code: {response.status_code}")
        print(f"Response URL: {response.url}")

        # Check if login was successful by looking for redirect to login success page
        assert "login.jsp" in response.url, "Login was successful; SQL Injection worked. The site is vulnerable."

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
