import os
import requests
import json

def get_balance():
    # Attempt to get the key from environment
    api_key = os.environ.get("TWO_CAPTCHA_API_KEY")
    
    if not api_key:
        print("Error: TWO_CAPTCHA_API_KEY environment variable not set.")
        return

    # Debug: Check key length and format (redacted for safety)
    # print(f"Using key of length: {len(api_key)}")

    url = "https://api.2captcha.com/getBalance"
    payload = {
        "clientKey": api_key
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        # The API documentation says POST to https://api.2captcha.com/getBalance
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        if data.get("errorId") == 0:
            print(f"Current Balance: ${data.get('balance')}")
        else:
            # Handle specific error cases from 2Captcha
            error_code = data.get("errorCode")
            error_desc = data.get("errorDescription")
            print(f"2Captcha API Error: {error_code} - {error_desc}")
            if error_code == "ERROR_KEY_DOES_NOT_EXIST":
                print("Tip: Please double check that your API key is correct and active in your 2Captcha dashboard.")
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    get_balance()
