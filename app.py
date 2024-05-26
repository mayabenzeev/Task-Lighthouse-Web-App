from distutils.command import build
import os
from flask import Flask, request, redirect, session, render_template, url_for
from httplib2 import Credentials
from src import OAuthManager, AppConfig
from dotenv import load_dotenv
load_dotenv()  # This takes environment variables from .env.

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def login():
    """ Login page with link to Google login. """
    auth_url = OAuthManager.get_authorization_url(
        AppConfig.CLIENT_ID, AppConfig.REDIRECT_URI, AppConfig.SCOPE)
    return render_template('login.html', auth_url=auth_url)

@app.route('/oauth2callback')
def oauth2callback():
    """Endpoint to handle the redirect from Google after authorization."""
    code = request.args.get('code')
    if not code:
        return redirect(url_for('login'))  # Redirect to login if no code is provided

    tokens = OAuthManager.exchange_code_for_token(
        code, AppConfig.CLIENT_ID, AppConfig.CLIENT_SECRET, AppConfig.REDIRECT_URI)
    
    session['tokens'] = tokens  # Store tokens in the session

    # Load credentials from the token
    credentials = Credentials(
        token=tokens.get('access_token'),
        refresh_token=tokens.get('refresh_token'),
        token_uri='https://oauth2.googleapis.com/token',
        client_id=AppConfig.CLIENT_ID,
        client_secret=AppConfig.CLIENT_SECRET,
        scopes=[AppConfig.SCOPE]
    )

    # Create a service object to interact with the Google API
    service = build('oauth2', 'v2', credentials=credentials)

    # Get user information
    user_info = service.userinfo().get().execute()
    session['user_info'] = user_info  # Store user info in session

    return redirect(url_for('homepage'))

@app.route('/homepage')
def homepage():
    """Display user home page."""
    user_info = session.get('user_info')
    if not user_info:
        return redirect(url_for('login'))  # Redirect to login if no user info in session
    return render_template('homepage.html', user_info=user_info)

@app.route('/logout')
def logout():
    """Log out the current user by clearing the session."""
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
