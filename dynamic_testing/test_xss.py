import pytest
import requests

# A test to check if the site is vulnerable to a basic reflected XSS attack
def test_basic_xss_attack():
    url = "http://testphp.vulnweb.com/artists.php"
    
    # Try to inject a script into the 'artist' query parameter
    xss_payload = "<script>alert('XSS Basic')</script>"
    params = {"artist": xss_payload}
    
    response = requests.get(url, params=params)
    #print(response.text)
    # If the payload is reflected back in the response, it might be vulnerable
    assert xss_payload not in response.text, "XSS vulnerability may exist!"



def test_reflected_xss():
    # Target URL that echoes back input (only use legally allowed ones)
    target_url = "https://xss-game.appspot.com/level1/frame"
    
    # Payload we want to test
    xss_payload = "<script>alert('XSS Reflected')</script>"
    
    # Send a GET request with payload as query parameter
    response = requests.get(target_url, params={"query": xss_payload})
    #print(response.text)
    # Check if our payload is reflected in the response
    assert xss_payload in response.text, "Potential XSS vulnerability found"