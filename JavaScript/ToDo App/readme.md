📝 Simple ToDo App
==================

A responsive web-based ToDo application that allows users to add, edit, and delete tasks. Tasks are persisted using local storage, ensuring your tasks are saved even after closing the browser.

✨ Features
----------

*   **Add Tasks:** Easily add new tasks with a title, date, and description.
    
*   **Edit Tasks:** Modify existing tasks.
    
*   **Delete Tasks:** Remove tasks you no longer need.
    
*   **Persistent Storage:** All tasks are saved in the browser's local storage, so they remain available across sessions.
    
*   **Modal Confirmation:** A confirmation dialog appears when attempting to close the task form with unsaved changes.
    
*   **Input Validation:** Basic validation to ensure a title is provided for each task.
    
*   **Success Notifications:** Uses SweetAlert2 for user-friendly success messages.
    
*   **Responsive Design:** Adapts to different screen sizes for a consistent user experience.
    

🚀 Technologies Used
--------------------

*   **HTML5:** Provides the semantic structure of the application.
    
*   **CSS3:** Styles the application, making it visually appealing and responsive.
    
*   **JavaScript (ES6+):** Handles all the interactive logic, including DOM manipulation, local storage management, and event handling.
    
*   **Font Awesome:** Used for icons (e.g., the plus icon for "New Task").
    
*   **SweetAlert2:** A beautiful, responsive, customizable, and accessible (WAI-ARIA) replacement for JavaScript's popup boxes.
    

📁 Project Structure
--------------------

*   index.html: The main HTML file containing the structure of the ToDo app, including the task form, task display area, and the confirmation modal.
    
*   style.css: Contains all the CSS rules for styling the application, defining its layout, colors, typography, and responsive behavior.
    
*   script.js: Implements the core logic of the ToDo app, managing task data (add, edit, delete), interacting with local storage, handling form submissions, and controlling modal dialogs.
    

⚙️ Setup and Installation
-------------------------

To run this project locally, follow these simple steps:

1.  git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
2.  cd YOUR_REPO_NAME (Replace YOUR\_USERNAME and YOUR\_REPO\_NAME with your actual GitHub username and repository name.)
    
3.  **Open in Browser:**
    
    *   Simply open the index.html file in your web browser. No server setup is required as it's a client-side application.
        

💡 Usage
--------

1.  **Add New Task:** Click the "New Task" button to open the task form. Fill in the title, date, and description, then click "Add Task".
    
2.  **Edit Task:** Click the "Edit" button on any existing task card to populate the form with its details. Make changes and click "Update Task".
    
3.  **Delete Task:** Click the "Delete" button on any task card to remove it.
    
4.  **Discard Changes:** If you open the task form and make changes (or start a new task) but decide not to save, clicking the close button will prompt a confirmation dialog to discard changes.
