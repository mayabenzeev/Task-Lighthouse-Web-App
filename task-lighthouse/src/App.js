import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage/LoginPage';
import HomePage from './pages/HomePage/HomePage';
import TaskManagerPage from './pages/TaskManagerPage/TaskManagerPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPage/>} />
        <Route path="/home" element={<HomePage/>} />
        <Route path="/tasks/:projectName" element={<TaskManagerPage/>} />
        <Route path="/logout" element={<LoginPage />} />
        <Route path="/" element={<LoginPage />} /> {/* Default route */}
      </Routes>
    </Router>
  );
}

export default App;
