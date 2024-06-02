import requests
import urllib.parse
from .config import AppConfig

def get_authorization_url():
    params = {
        "scope": AppConfig.get_scope_url(),
        "access_type": "offline",
        "include_granted_scopes": "true",
        "response_type": "code",
        "redirect_uri": AppConfig.REDIRECT_URI,
        "client_id": AppConfig.GOOGLE_CLIENT_ID,
        "prompt": "consent"
    }
    return f"https://accounts.google.com/o/oauth2/v2/auth?{urllib.parse.urlencode(params)}"

def exchange_code_for_token(code):
    data = {
        'code': code,
        'client_id': AppConfig.GOOGLE_CLIENT_ID,
        'client_secret': AppConfig.GOOGLE_CLIENT_SECRET,
        'redirect_uri': AppConfig.REDIRECT_URI,
        'grant_type': 'authorization_code',
    }
    response = requests.post("https://oauth2.googleapis.com/token", data=data)
    if response.status_code != 200:
        raise Exception("Failed to exchange token")
    return response.json()
