# 📝 Python To-Do CLI App

A beginner-friendly, interactive command-line To-Do List written in Python.  
This project demonstrates **lists**, **loops**, **functions**, and user interaction for anyone learning Python or looking for a practical CLI project.

---

## 🚀 Features

- **Add** new tasks with input validation
- **View** all tasks with clear statuses and numbering
- **Mark** any task as complete
- **Delete** tasks safely with confirmation
- Simple, user-friendly interface
- Well-commented, modular code for easy learning and extension

---

## 🛠 Installation

### Requirements
- Python 3.x (recommended: Python 3.7 or newer)
- Works on Windows, macOS, and Linux

### Setup

1. **Download the Source Code**
   - Download or clone this Project directory:
     If you just need the main.py file:
        - Click on main.py
        - Click "Raw" button
        - Right-click → "Save As" to download the file
          
or Click on https://download-directory.github.io paste the link https://github.com/kumaradoss16/Projects-Programming/new/main/Python/To-Do%20App, and download the "Python To-Do CLI App" directory.

Right-click → "Save As" to download the file

2. **Run the Application**
   - Using your terminal or command prompt, run:
     ```
     python main.py
     ```
     Or, if you use `python3`:
     ```
     python3 main.py
     ```

---

## 📦 Usage

### Step-by-step Instructions

1. **Start the app.**
    - You’ll see a menu offering five options.
2. **Add a new task.**
    - Enter a description when prompted. Empty or too-long entries are not allowed.
3. **View your tasks.**
    - See numbered tasks, each showing if they’re completed.
4. **Complete a task.**
    - Enter a task number from the list; the status will update.
5. **Delete a task.**
    - Enter the number and confirm your choice.
6. **Exit the app.**
    - Choose option 5 to end your session.

---

## 🗂️ Code Structure

The project is organized into several clear, beginner-friendly functions:

| Function        | Purpose                                                      |
| --------------- | ------------------------------------------------------------ |
| `show_menu()`   | Display the main options to the user                         |
| `get_user_choice()` | Get and validate menu input from the user                |
| `add_task(tasks)` | Prompt for and add a new task to the list                  |
| `view_tasks(tasks)` | List all current tasks with status and stats             |
| `complete_task(tasks)` | Mark a selected task as completed                     |
| `delete_task(tasks)` | Delete a task from the list after confirmation          |
| `main()`        | Main loop tying all functions together; runs the application |

**Key Concepts Used:**
- Python lists and dictionaries
- Loops (`while`, `for`)
- Functions and modular code
- Input validation and error handling
- User-friendly output with emojis and formatted text

---

## 💡 Example Commands and Output

> **Adding a Task**
```

Choose an option (1-5): 1

➕ ADD NEW TASK
--------------------
Enter task description: Learn Python CLI apps
✅ Task 'Learn Python CLI apps' added successfully!
📊 You now have 1 task(s) in your list.

```

> **Viewing Tasks**
```

Choose an option (1-5): 2

📋 YOUR TASKS
------------------------------
1. ⏳ Learn Python CLI apps
------------------------------
📊 Total: 1 | ✅ Completed: 0 | ⏳ Pending: 1

```

> **Completing a Task**
```

Choose an option (1-5): 3

✅ MARK TASK AS COMPLETE
-------------------------
📋 YOUR TASKS
------------------------------
1. ⏳ Learn Python CLI apps
------------------------------

Enter task number to complete (or 'c' to cancel): 1
🎉 Task 'Learn Python CLI apps' marked as completed!

```

> **Deleting a Task**
```

Choose an option (1-5): 4

🗑️ DELETE TASK
---------------
📋 YOUR TASKS
------------------------------
1. ✅ ~~Learn Python CLI apps~~
------------------------------

Enter task number to delete (or 'c' to cancel): 1
⚠️ Are you sure you want to delete 'Learn Python CLI apps'? (y/n): y
🗑️ Task 'Learn Python CLI apps' deleted successfully!
📊 You now have 0 task(s) remaining.

```

---

## 📖 Contribution Guidelines

Contributions are welcome!

- **Improvements:** Suggest or submit pull requests for new features or code improvements.
- **Bugs:** If you find any issues, please open an issue report on GitHub.
- **Learning:** New to open source? Fork the repo and try adding a feature, like saving tasks to a file!

---

## 🌱 Future Improvements (Optional)

- Save/load tasks with a file or database
- Task priorities and deadlines
- Search or sort tasks
- Export to-do list as text or CSV

---

> **Tip:** Simply copy-paste the contents above into `README.md`.
> Update the project links, author, or license to fit your repository.
> This format will look clean and professional on GitHub, is SEO optimized, and is a helpful resource for Python beginners!


