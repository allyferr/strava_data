import os
import requests
import urllib3

auth_url = "https://www.strava.com/oauth/token"
payload = {
    'client_id': os.environ.get("CLIENT_ID"),
    'client_secret': os.environ.get("CLIENT_SECRET"),
    'refresh_token': os.environ.get("REFRESH_TOKEN"),
    'grant_type': "refresh_token",
    'f': 'json'
}


# Request new access token to get header params
def get_new_token():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    print("Requesting Token...\n")
    res = requests.post(auth_url, data=payload, verify=False)
    access_token = res.json()['access_token']
    header = {"Authorization": f"Bearer {access_token}"}
    return header
