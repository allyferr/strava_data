import requests
import urllib3

auth_url = "https://www.strava.com/oauth/token"
payload = {
    'client_id': '106468',
    'client_secret': '3a1ca09af304e278ab397ae7244ba4e7a10dcb57',
    'refresh_token': '2ae39a017be37b92de1b509aa731a97b76c1fdc6',
    'grant_type': "refresh_token",
    'f': 'json'
}


# Request new access token to get header params
def get_new_token():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    print("Requesting Token...\n")
    res = requests.post(auth_url, data=payload, verify=False)
    access_token = res.json()['access_token']
    print("Access Token = {}\n".format(access_token))
    header = {"Authorization": f"Bearer {access_token}"}
    return header
