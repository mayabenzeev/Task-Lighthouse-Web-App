// TaskColumn.js
import React from 'react';
import { Droppable, Draggable } from 'react-beautiful-dnd';
import Task from './Task';

const TaskColumn = ({ columnId, title, tasks }) => (
    <div className="column-container">
        <div className="column-header">
            <h2>{title}</h2>
        </div>
        <Droppable droppableId={columnId}>
            {(provided, snapshot) => (
                <div 
                    ref={provided.innerRef}
                    {...provided.droppableProps}
                    className="column"
                >
                    {tasks.map((task, index) => (
                        <Draggable key={task.id} draggableId={task.id.toString()} index={index}>
                            {(provided, snapshot) => (
                                <div
                                    ref={provided.innerRef}
                                    {...provided.draggableProps}
                                    {...provided.dragHandleProps}
                                    className={`task-item ${snapshot.isDragging ? 'is-dragging' : ''}`}

                                >
                                    <p>{task.text}</p>
                                </div>
                            )}
                        </Draggable>
                    ))}
                    {provided.placeholder}
                </div>
            )}
        </Droppable>
    </div>
);

export default TaskColumn;
