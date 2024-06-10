// Task.js
import React from 'react';
import './Task.css'; // Ensure you link to a CSS file for Task styles

const Task = ({ task }) => {
    return (
        <div className="task-item">
            <p>{task.text}</p>
        </div>
    );
};

export default Task;
