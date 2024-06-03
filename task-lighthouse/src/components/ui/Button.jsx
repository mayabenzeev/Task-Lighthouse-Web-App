import React from 'react';

function Button({ onClick, children, className }) {
    return (
        <button onClick={onClick} className={`main-btn ${className}`}>{children}</button>
    );
}

export default Button;
