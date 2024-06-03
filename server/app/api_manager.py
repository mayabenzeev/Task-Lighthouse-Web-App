from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from .config import AppConfig


def get_user_info(access_token, refresh_token):
    credentials = Credentials(
        token=access_token,
        refresh_token=refresh_token,
        token_uri='https://oauth2.googleapis.com/token',
        client_id=AppConfig.GOOGLE_CLIENT_ID,
        client_secret=AppConfig.GOOGLE_CLIENT_SECRET,
        scopes=AppConfig.SCOPES
    )

    # Check if token is expired and refresh it if necessary
    if credentials.expired:
        credentials.refresh(Request())

    # Create a service object to interact with the Google API
    service = build('oauth2', 'v2', credentials=credentials)
    user_info = service.userinfo().get().execute()

    new_tokens = {
        'access_token': credentials.token,
        # Update the tokens after refresh if necessary
        'refresh_token': refresh_token if credentials.refresh_token is None else credentials.refresh_token
    }
    return user_info, new_tokens
