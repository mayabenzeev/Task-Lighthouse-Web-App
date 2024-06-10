import React, { useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import TaskColumn from '../../components/ui/TaskColumn/TaskColumn';  // Ensure correct path
import './ProjectDashboard.css';
import '../../index.css';

function ProjectDashboard() {
  const { projectName } = useParams();
  const [tasks, setTasks] = useState({
    todo: [],
    inProgress: [],
    managerReview: [],
    done: []
  });

  const addTask = (column) => {
    const taskText = prompt("Enter the task description:");
    if (taskText) {
      const newTask = { id: Date.now(), text: taskText };
      setTasks(prevTasks => ({
        ...prevTasks,
        [column]: [...prevTasks[column], newTask]
      }));
    }
  };

  const onDragEnd = result => {
    const { source, destination } = result;

    if (!destination) {
      return; // dropped outside the list
    }

    if (source.droppableId === destination.droppableId && source.index === destination.index) {
      return; // dropped in the same place
    }

    const start = tasks[source.droppableId];
    const finish = tasks[destination.droppableId];

    if (start === finish) {
      const newTaskIds = Array.from(start);
      const [removed] = newTaskIds.splice(source.index, 1);
      newTaskIds.splice(destination.index, 0, removed);

      const newTasks = {
        ...tasks,
        [source.droppableId]: newTaskIds
      };

      setTasks(newTasks);
    } else {
      // Moving from one list to another
      const startTaskIds = Array.from(start);
      const [removed] = startTaskIds.splice(source.index, 1);
      const finishTaskIds = Array.from(finish);
      finishTaskIds.splice(destination.index, 0, removed);

      const newTasks = {
        ...tasks,
        [source.droppableId]: startTaskIds,
        [destination.droppableId]: finishTaskIds
      };

      setTasks(newTasks);
    }
  };

  return (
    <DragDropContext onDragEnd={onDragEnd}>
      <div className="task-manager-container">
        <h1>Tasks for {projectName}</h1>
        {Object.keys(tasks).map((key, index) => (
          <TaskColumn
            key={key}
            columnId={key}
            title={key}
            tasks={tasks[key]}
            onAddTask={() => addTask(key)}
          />
        ))}
        <Link to="/home" className="back-home">Back to Homepage</Link>
      </div>
    </DragDropContext>
  );
}

export default ProjectDashboard;
