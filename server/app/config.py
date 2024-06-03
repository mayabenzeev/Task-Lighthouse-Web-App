import os


class AppConfig:
    """ Configuration class to store client secrets and IDs. """
    SECRET_KEY = os.getenv('SECRET_KEY')
    SESSION_TYPE = 'filesystem'
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    REDIRECT_URI = "http://localhost:8000/oauth2callback"
    SCOPES = [
        'https://www.googleapis.com/auth/calendar',
        'https://www.googleapis.com/auth/userinfo.email'
    ]

    @staticmethod
    def get_scope_url():
        """Return URL-encoded scope string."""
        return ' '.join(AppConfig.SCOPES)

