from flask import request, redirect, session, url_for, render_template
from .oauth_manager import get_authorization_url, exchange_code_for_token
from .api_manager import get_user_info

def init_routes(app):
    @app.route('/')
    def login():
        auth_url = get_authorization_url()
        return render_template('login.html', auth_url=auth_url)

    @app.route('/oauth2callback')
    def oauth2callback():
        code = request.args.get('code')
        if not code:
            return redirect(url_for('login'))

        tokens = exchange_code_for_token(code)
        user_info, updated_tokens = get_user_info(tokens['access_token'], tokens['refresh_token'])
        session['user_info'] = user_info
        session['tokens'] = updated_tokens

        return redirect(url_for('homepage'))

    @app.route('/homepage')
    def homepage():
        user_info = session.get('user_info')
        if not user_info:
            return redirect(url_for('login'))
        return render_template('homepage.html', user_info=user_info)

    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login'))
