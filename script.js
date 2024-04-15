
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
                    <img class="rename" src="rename-icon.png" onclick="renameTask(this)"/>`;
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
