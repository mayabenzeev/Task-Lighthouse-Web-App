import React from 'react';
import { useNavigate } from 'react-router-dom';
import Button from '../../components/ui/Button';
import './HomePage.css';

function HomePage() {
  const navigate = useNavigate();

  const goToTaskManager = () => {
    navigate('/tasks/Project1');  // Replace 'Project1' with the desired project name
  };

  return (
    <div className="home-container">
      <h1>Welcome to Your Dashboard</h1>
      <Button onClick={goToTaskManager} className="main-page-btn">
        Go to Task Manager
      </Button>
      <div className="navigation">
        <a href="/logout" className="logout-button">Logout</a>
      </div>
    </div>
  );
}

export default HomePage;
