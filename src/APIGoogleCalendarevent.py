import urllib.parse
import config
def get_authorization_url(client_id, redirect_uri, scope):
    base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    params = {
        "scope": scope,
        "access_type": "offline",
        "include_granted_scopes": "true",
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "client_id": client_id,
    }
    authorization_url = f"{base_url}?{urllib.parse.urlencode(params)}"
    return authorization_url

# Provide your values for client_id and redirect_uri
authorization_url = get_authorization_url(
    client_id=config.CLIENT_ID,
    redirect_uri="https://localhost:63342/oauth2callback",
    scope="https://www.googleapis.com/auth/calendar"
)
print("Go to the following URL and authorize the application:")
print(authorization_url)
