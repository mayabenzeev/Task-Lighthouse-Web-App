from flask import request, redirect, session, url_for, render_template
from .oauth_manager import get_authorization_url, exchange_code_for_token
from .api_manager import get_user_info
from .mongo_utils import get_mongo_client, add_user, get_user_projects
import os
from flask import send_from_directory

def init_routes(app):
    db = get_mongo_client()  # Initialize db once for further use across routes

    @app.route('/')
    def serve_react_app():
        return send_from_directory('build', 'index.html')
    # @app.route('/')
    # def login():
    #     auth_url = get_authorization_url()
    #     return render_template('login.html', auth_url=auth_url)

    @app.route('/oauth2callback')
    def oauth2callback():
        code = request.args.get('code')
        if not code:
            return redirect(url_for('serve_react_app'))

        tokens = exchange_code_for_token(code)
        user_info, updated_tokens = get_user_info(tokens['access_token'], tokens['refresh_token'])
        session['user_info'] = user_info
        session['tokens'] = updated_tokens

        # MongoDB's user login check or register
        # Find the user id of the Google account in the db
        user = db.users.find_one({"user_id": user_info['id']})
        if not user:
            # User doesn't exist, so add them to the database
            user_data = {
                "user_id": user_info['id'],
                "email": user_info.get('email'),
                "projects": []
            }
            add_user(user_data)
        else:
            # Load projects shared with the user
            user_projects = get_user_projects(user_info['id'])
            session['projects'] = user_projects  # Store projects in session for homepage
            # TODO: Connect the projects page!!!! session is going to give this information

        return redirect('/home')

    @app.route('/home')
    def homepage():
        user_info = session.get('user_info')
        if not user_info:
            return redirect(url_for('serve_react_app'))
        # Fetch projects from session
        projects = session.get('projects', [])
        # TODO: Connect the projects page!!!! session is going to give this information
        return send_from_directory('build', 'index.html')

    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('/'))
    
    @app.route('/<path:path>')
    def static_proxy(path):
        # Serve static files from the React build directory
        return send_from_directory('build', path)