const taskForm = document.getElementById("task-form");
const confirmCloseDialog = document.getElementById("confirm-close-dialog");
const openTaskFormBtn = document.getElementById("open-task-form-btn");
const closeTaskFormBtn = document.getElementById("close-task-form-btn");
const addOrUpdateTaskBtn = document.getElementById("add-or-update-task-btn");
const cancelBtn = document.getElementById("cancel-btn");
const discardBtn = document.getElementById("discard-btn");
const tasksContainer = document.getElementById("tasks-container");
const titleInput = document.getElementById("title-input");
const dateInput = document.getElementById("date-input");
const descriptionInput = document.getElementById("description-input");

const taskData = JSON.parse(localStorage.getItem("data")) || [];     // array will store all the task along with their associated data like title, date and description and also save them to localstorage.
let currentTask = {};     // used to track the state when editing and discarding tasks.


const removeSpecialChars = (string) => {
    return string.replace(/[^a-zA-Z0-9\s]/g, "");
}

const addOrUpdateTask = () => {
    if (!titleInput.value.trim()) {
        alert("Please provide a title");
        return;
    }
    // item -> represents the current task looking at in the taskData list
    // item.id -> unique identifier of that item.
    // currentTask.id -> unique identifier of a specific task that your are currently working with.
    const dataArrIndex = taskData.findIndex((item) => item.id === currentTask.id);     // findIndex() return the index pf the first element in an array (provide the index of each task).
    const taskObj = {
        id: `${removeSpecialChars(titleInput.value).toLowerCase().split(" ").join("-")}-${Date.now()}`,
        title: removeSpecialChars(titleInput.value),
        date: dateInput.value,
        description: removeSpecialChars(descriptionInput.value),
    };
    if (dataArrIndex === -1) {
        taskData.unshift(taskObj);     // unshift() is an array method that is used to add one or more elements to the beginning of an array.
    } else {
        taskData[dataArrIndex] = taskObj;
    }
    localStorage.setItem("data", JSON.stringify(taskData));
    updateTaskContainer();
    reset();
    showSuccessAlert();
};

const updateTaskContainer = () => {
    // Remove the Exisitng contents of taskContainer before adding a new task.
    tasksContainer.innerHTML = "";
    taskData.forEach(({ id, title, date, description }) => {
        tasksContainer.innerHTML += `
                <div class="task" id="${id}">
                    <p><strong>Title: </strong>${title}</p>
                    <p><strong>Date: </strong>${date}</p>
                    <p><strong>Description: </strong>${description}</p>
                    <button type="button" class="btn" onclick="editTask(this)">Edit</button>
                    <button type="button" class="btn" onclick="deleteTask(this)">Delete</button>
                </div>`;
    });
}

// Function to find the index of the task you want to delete first
const deleteTask = (buttonEl) => {
    const dataArrIndex = taskData.findIndex((item) => item.id === buttonEl.parentElement.id);      // This line figure out which task you want to delete. 'dataArrIndex = "index"'
    buttonEl.parentElement.remove();     // immediately remove the entire visual task card.
    taskData.splice(dataArrIndex, 1);

    localStorage.setItem("data", JSON.stringify(taskData));
}

const editTask = (buttonEl) => {
    const dataArrIndex = taskData.findIndex((item) => item.id === buttonEl.parentElement.id);
    currentTask = taskData[dataArrIndex];
    titleInput.value = currentTask.title;
    dateInput.value = currentTask.date;
    descriptionInput.value = currentTask.description;
    addOrUpdateTaskBtn.innerText = "Update Task";
    taskForm.classList.toggle("hidden");
}

// Function to resolve to clear the input fields after adding a task
const reset = () => {
    addOrUpdateTaskBtn.innerText = "Add Task";     // Change the button name for Add Task in the task form during edit session.
    // Clear the text in the input field
    titleInput.value = "";
    dateInput.value = "";
    descriptionInput.value = "";

    taskForm.classList.toggle("hidden");
    currentTask = {};
}

if (taskData.length) {
    updateTaskContainer();
}

openTaskFormBtn.addEventListener("click", () => {
    taskForm.classList.toggle("hidden");      // work for <form> tag
})

closeTaskFormBtn.addEventListener("click", () => {
    const formInputsContainValues = titleInput.value || dateInput.value || descriptionInput.value;
    // If the user attempts to edit a task bu decides not to make any change before closing the form.
    const formInputValuesUpdated = titleInput.value !== currentTask.title || dateInput.value !== currentTask.date || descriptionInput.value !== currentTask.description;
    // If any those input fields has a value, then use the showModal() or reset().
    if (formInputsContainValues && formInputValuesUpdated) {
        confirmCloseDialog.showModal();
    } else {
        reset();
    }
})

cancelBtn.addEventListener("click", () => {
    confirmCloseDialog.close();     // used to close a modal dialog box on an web page.
});

// When user click the discard button, you want to close the modal showing the 'cancel' and 'Discard' button, then hide the form modal.
discardBtn.addEventListener("click", () => {
    confirmCloseDialog.close();
    reset();
})

taskForm.addEventListener("submit", (e) => {
    e.preventDefault();
    // Display the task on the page
    addOrUpdateTask();
})

function showSuccessAlert() {
    Swal.fire({
        title: "Success!",
        text: "Task is added.",
        icon: "success",
        confirmButtonText: "OK"
    });
}
