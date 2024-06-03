import React from 'react';
import './LoginPage.css';

function LoginPage() {
  const loginUrl = '/oauth2callback'; // Replace with your actual login URL

  const fetchLoginUrl = async () => {
    const response = await fetch('http://localhost:8000/login');
    const data = await response.json();
    console.log(data);
  };

  return (
    <div>
      <h1>Welcome to Our Application</h1>
      <p>Please login.</p>
      <a href={loginUrl} className="btn-login">Login with Google</a>
    </div>
  );
}

export default LoginPage;
