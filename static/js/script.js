
const taskValue = document.getElementById("task-text");
const taskContainer = document.getElementById("task-container");
const listItems = document.getElementById("list-item");
const addUpdateClick = document.getElementById("AddTaskClick");


taskValue.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        addUpdateClick.click();
    }
});

window.createTask = function() {
    if (taskValue.value.trim() === "") {
        alert("Please enter a task");
        taskValue.focus();
        return; // Stop function execution if the input is empty
    }
    let li = document.createElement("li");
    li.className = "task-body"; // Use your existing class for tasks
    li.innerHTML = `<span class="task-text">${taskValue.value}</span>
                    <img class="rename" src="/static/img/rename-icon.png" onclick="renameTask(this)"/>`;
    listItems.appendChild(li); // Append the new task to the list
    taskValue.value = ""; // Clear the input after adding the item
};

window.renameTask = function(img) {
    let taskTextSpan = img.previousElementSibling; // The span that contains the task text
    let currentText = taskTextSpan.textContent;

    // Create a new input element
    let input = document.createElement('input');
    input.type = 'text';
    input.value = currentText;
    input.className = 'task-edit-input'; // Add a class for styling if needed

    // Replace the span with the input
    taskTextSpan.parentNode.replaceChild(input, taskTextSpan);

    // Select the input text
    input.focus();
    input.select();

    // Handle the end of editing
    input.addEventListener('blur', function() {
        finishEdit(input);
    });
    input.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            finishEdit(input);
        }
    });
};

function finishEdit(input) {
    let newSpan = document.createElement('span');
    newSpan.className = 'task-text';
    newSpan.textContent = input.value.trim() === '' ? 'Untitled Task' : input.value;

    // Replace input with the new span
    input.parentNode.replaceChild(newSpan, input);
}


document.addEventListener('DOMContentLoaded', (event) => {
    var dragSrcEl = null;

    function handleDragStart(e) {
        this.style.opacity = '0.4';
        dragSrcEl = this;
        e.dataTransfer.effectAllowed = 'move';
        e.dataTransfer.setData('text/html', this.outerHTML);
    }

    function handleDragOver(e) {
        if (e.preventDefault) {
            e.preventDefault();
        }
        e.dataTransfer.dropEffect = 'move';
        return false;
    }

    function handleDragEnter(e) {
        this.classList.add('over');
    }

    function handleDragLeave(e) {
        this.classList.remove('over');
    }

    function handleDrop(e) {
        e.preventDefault();
        if (e.stopPropagation) {
            e.stopPropagation();
        }

        if (dragSrcEl !== this) {
            // Check if we're dropping into a column or before another task
            const hasClassColumn = this.classList.contains('column');
            if (hasClassColumn) {
                this.appendChild(dragSrcEl);
            } else {
                this.parentNode.insertBefore(dragSrcEl, this);
            }
        }
    }

    function handleDragEnd(e) {
        this.style.opacity = '1';
        columns.forEach(column => {
            column.classList.remove('over');
        });
    }

    let columns = document.querySelectorAll('.column');
    columns.forEach(column => {
        column.addEventListener('dragover', handleDragOver, false);
        column.addEventListener('dragenter', handleDragEnter, false);
        column.addEventListener('dragleave', handleDragLeave, false);
        column.addEventListener('drop', handleDrop, false);
    });

    function updateDraggableItems() {
        let items = document.querySelectorAll('.task-body');
        items.forEach(item => {
            item.setAttribute('draggable', 'true');
            item.addEventListener('dragstart', handleDragStart, false);
            item.addEventListener('dragend', handleDragEnd, false);
        });
    }

    updateDraggableItems(); // Initial update for existing items

    window.createTask = function() {
        if (taskValue.value.trim() === "") {
            alert("Please enter a task");
            taskValue.focus();
            return;
        }

        let li = document.createElement("li");
        li.className = "task-body";
        li.innerHTML = `<span class="task-text">${taskValue.value}</span>
                        <img class="rename" src="/static/img/rename-icon.png" onclick="renameTask(this)"/>`;
        listItems.appendChild(li); // Append the new task to the list
        taskValue.value = ""; // Clear the input after adding the item

        updateDraggableItems(); // Re-bind draggable items including new ones
    };
});

