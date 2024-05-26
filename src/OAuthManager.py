import urllib.parse
import requests

class OAuthManager:
    """ Manages the OAuth2 flow for Google authentication. """
    AUTH_BASE_URL = "https://accounts.google.com/o/oauth2/v2/auth"
    TOKEN_URL = "https://oauth2.googleapis.com/token"

    @staticmethod
    def get_authorization_url(client_id, redirect_uri, scope):
        # """ Build the authorization URL to initiate OAuth. """
        params = {
            "scope": scope,
            "access_type": "offline",
            "include_granted_scopes": "true",
            "response_type": "code",
            "redirect_uri": redirect_uri,
            "client_id": client_id,
        }
        authorization_url = f"{OAuthManager.AUTH_BASE_URL}?{urllib.parse.urlencode(params)}"
        return authorization_url

    @staticmethod
    def exchange_code_for_token(code, client_id, client_secret, redirect_uri):
        """ Exchange the authorization code for an access token. """
        data = {
            'code': code,
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': redirect_uri,
            'grant_type': 'authorization_code',
        }
        response = requests.post(OAuthManager.TOKEN_URL, data=data)
        return response.json()
