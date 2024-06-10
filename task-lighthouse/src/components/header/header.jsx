// Header.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css'; // Make sure you link the CSS file for styling

const Header = () => {
    return (
        <header className="site-header">
            <h1 className="site-title">My Website</h1>
            <nav className="header-nav">
                <ul>
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/about">About</Link></li>
                    <li><Link to="/contact">Contact</Link></li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;
