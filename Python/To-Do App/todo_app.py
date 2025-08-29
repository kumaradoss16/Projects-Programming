"""
Complete To-Do List Application
Demonstrates Python lists, loops, and basic CLI interaction
"""

def show_menu():
    """Display the main menu options"""
    print("\n" + "="*40)
    print("📝 TO-DO LIST MENU")
    print("="*40)
    print("1. ➕ Add a new task")
    print("2. 📋 View all tasks")
    print("3. ✅ Mark task as complete")
    print("4. 🗑️  Delete a task")
    print("5. 🚪 Exit")
    print("="*40)

def get_user_choice():
    """Get and validate user menu choice"""
    while True:
        choice = input("Choose an option (1-5): ").strip()
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        print("❌ Please enter a number between 1 and 5.")

def add_task(tasks):
    """Add a new task to the task list"""
    print("\n➕ ADD NEW TASK")
    print("-" * 20)
    
    while True:
        task_description = input("Enter task description: ").strip()
        
        if not task_description:
            print("❌ Task cannot be empty. Please try again.")
            continue
        
        if len(task_description) > 100:
            print("❌ Task too long (max 100 characters). Please shorten it.")
            continue
            
        new_task = {
            'task': task_description,
            'completed': False
        }
        
        tasks.append(new_task)
        print(f"✅ Task '{task_description}' added successfully!")
        print(f"📊 You now have {len(tasks)} task(s) in your list.")
        break

def view_tasks(tasks):
    """Display all tasks with their status"""
    print("\n📋 YOUR TASKS")
    print("-" * 30)
    
    if not tasks:
        print("📭 No tasks yet! Add some tasks to get started.")
        return
    
    for index, task in enumerate(tasks, 1):
        status = "✅" if task['completed'] else "⏳"
        task_text = task['task']
        
        if task['completed']:
            task_text = f"~~{task_text}~~"
            
        print(f"{index:2d}. {status} {task_text}")
    
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    
    print("-" * 30)
    print(f"📊 Total: {total_tasks} | ✅ Completed: {completed_tasks} | ⏳ Pending: {pending_tasks}")

def complete_task(tasks):
    """Mark a task as completed"""
    print("\n✅ MARK TASK AS COMPLETE")
    print("-" * 25)
    
    if not tasks:
        print("📭 No tasks to complete!")
        return
    
    view_tasks(tasks)
    
    while True:
        try:
            task_num = input("\nEnter task number to complete (or 'c' to cancel): ").strip()
            
            if task_num.lower() == 'c':
                print("❌ Operation cancelled.")
                return
            
            task_index = int(task_num) - 1
            
            if task_index < 0 or task_index >= len(tasks):
                print(f"❌ Invalid task number. Please enter 1-{len(tasks)}.")
                continue
            
            if tasks[task_index]['completed']:
                print("ℹ️  This task is already completed!")
                return
            
            tasks[task_index]['completed'] = True
            task_name = tasks[task_index]['task']
            print(f"🎉 Task '{task_name}' marked as completed!")
            break
            
        except ValueError:
            print("❌ Please enter a valid number.")

def delete_task(tasks):
    """Delete a task from the list"""
    print("\n🗑️  DELETE TASK")
    print("-" * 15)
    
    if not tasks:
        print("📭 No tasks to delete!")
        return
    
    view_tasks(tasks)
    
    while True:
        try:
            task_num = input("\nEnter task number to delete (or 'c' to cancel): ").strip()
            
            if task_num.lower() == 'c':
                print("❌ Operation cancelled.")
                return
            
            task_index = int(task_num) - 1
            
            if task_index < 0 or task_index >= len(tasks):
                print(f"❌ Invalid task number. Please enter 1-{len(tasks)}.")
                continue
            
            task_name = tasks[task_index]['task']
            confirm = input(f"⚠️  Are you sure you want to delete '{task_name}'? (y/n): ").strip().lower()
            
            if confirm == 'y':
                deleted_task = tasks.pop(task_index)
                print(f"🗑️  Task '{deleted_task['task']}' deleted successfully!")
                print(f"📊 You now have {len(tasks)} task(s) remaining.")
            else:
                print("❌ Deletion cancelled.")
            break
            
        except ValueError:
            print("❌ Please enter a valid number.")

def main():
    """Main function to run the to-do application"""
    print("=== Welcome to Your Personal To-Do List ===")
    print("This app demonstrates Python lists and loops in action!")
    
    tasks = []
    
    while True:
        show_menu()
        choice = get_user_choice()
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\n🎉 Thank you for using the To-Do List app!")
            print("Keep coding and stay organized! 💻")
            break

if __name__ == "__main__":
    main()
