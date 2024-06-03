import React, { useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import './TaskManagerPage.css';

function TaskManagerPage() {
  const { projectName } = useParams();
  const [tasks, setTasks] = useState([]);

  const addTask = () => {
    const taskText = prompt("Enter the task description:");
    if (taskText) setTasks([...tasks, { id: Date.now(), text: taskText }]);
  };

  return (
    <div className="task-manager-container">
      <h1>Tasks for {projectName}</h1>
      <div className="task-list">
        {tasks.map(task => (
          <div key={task.id} className="task-item">
            {task.text}
          </div>
        ))}
      </div>
      <button onClick={addTask}>Add Task</button>
      <Link to="/home" className="back-home">Back to Homepage</Link>
    </div>
  );
}

export default TaskManagerPage;
