import requests
from urllib.parse import urlencode

# Configuration: replace these with your actual details
CLIENT_ID = '377653864442-1ncf0ealf9fm2gt8sc8j9bg1revqg5ul.apps.googleusercontent.com'
REDIRECT_URI = 'https://task-lighthouse.com'
AUTH_URL = 'https://accounts.google.com/o/oauth2/v2/auth'
TOKEN_URL = 'https://oauth2.googleapis.com/token'
SCOPE = 'https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/calendar.events'

# Step 1: Redirect user to Google's OAuth server
params = {
    'response_type': 'code',
    'client_id': CLIENT_ID,
    'redirect_uri': REDIRECT_URI,
    'scope': SCOPE,
    'access_type': 'offline'  # For refresh token
}
print(f"Go to the following URL to authorize: {AUTH_URL}?{urlencode(params)}")

# Step 2: Google redirects to your `redirect_uri` with a code, simulate it here
auth_code = input("Enter the authorization code: ")

# Step 3: Exchange the authorization code for an access token
data = {
    'code': auth_code,
    'client_id': CLIENT_ID,
    'redirect_uri': REDIRECT_URI,
    'grant_type': 'authorization_code'
}
response = requests.post(TOKEN_URL, data=data)
response_json = response.json()
access_token = response_json.get('access_token')
refresh_token = response_json.get('refresh_token')
print("Access Token:", access_token)
print("Refresh Token:", refresh_token)
