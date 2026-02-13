from database.connection import get_connection, setup_database
from models.user import User, UserManager
from models.task import Task, TaskManager


def signup():
    firstname = input("Enter firstname: ")
    lastname = input("Enter lastname: ")
    password = input("Enter password: ")
    return firstname, lastname, password


def login():
    firstname = input("Enter firstname: ")
    password = input("Enter password: ")
    return firstname, password


def authenticate(user_manager):
    while True:
        choice = input("Do you have an account? (y/n): ").lower()

        if choice == "y":
            firstname, password = login()
            user = user_manager.find_user(firstname, password)
            if user:
                print(f"Welcome, {firstname}!")
                return user[0]
            print("Invalid credentials. Please try again.")

        elif choice == "n":
            firstname, lastname, password = signup()
            user = User(firstname, lastname, password)
            user_manager.save_user(user)
            print(f"Account created for {firstname}!")

            logged_in_user = user_manager.find_user(firstname, password)
            if logged_in_user:
                print(f"Welcome, {firstname}!")
                return logged_in_user[0]

        else:
            print("Please enter 'y' or 'n'.")


def create_task(user_id, task_manager):
    taskname = input("What are you working on today? ")
    description = input("Enter task description: ")
    category = input("Enter task category: ")

    task = Task(user_id, taskname, description, category, status="started")
    print(f"Task '{taskname}' started...")

    input("Press Enter to stop the task: ")
    task.stop()

    task_manager.save_task(task)
    duration = task.get_duration()
    print(f"Task '{taskname}' completed in {duration:.1f} seconds.")


def show_task_history(user_id, task_manager):
    tasks = task_manager.get_user_tasks(user_id)
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Task History ---")
    for task in tasks:
        taskname, description, category, starttime, endtime, status = task
        print(f"  {taskname} [{category}] - {status}")
        print(f"    {description}")
        print(f"    Started: {starttime}, Ended: {endtime or 'In progress'}")
    print()


def main():
    con = get_connection()
    setup_database(con)

    user_manager = UserManager(con)
    task_manager = TaskManager(con)

    user_id = authenticate(user_manager)

    while True:
        activity = input("Enter 'n' for new task, 'h' for history, 'q' to quit: ").lower()

        if activity == "h":
            show_task_history(user_id, task_manager)
        elif activity == "n":
            create_task(user_id, task_manager)
        elif activity == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

    con.close()


if __name__ == "__main__":
    main()




