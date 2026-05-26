import json
import os
from datetime import datetime

SAVE_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(SAVE_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks):
    title = input("  Task title: ").strip()
    if not title:
        print("  [!] Title cannot be empty.")
        return

    print("  Priority — 1) Low  2) Medium  3) High")
    choice = input("  Choose (default = 2): ").strip()
    priority_map = {"1": "Low", "3": "High"}
    priority = priority_map.get(choice, "Medium")

    task = {
        "id": tasks[-1]["id"] + 1 if tasks else 1,
        "title": title,
        "done": False,
        "priority": priority,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"\n  [+] Added: '{title}' [{priority}]")


def view_tasks(tasks, filter_by="all"):
    filtered = []

    if filter_by == "done":
        filtered = [t for t in tasks if t["done"]]
    elif filter_by == "pending":
        filtered = [t for t in tasks if not t["done"]]
    else:
        filtered = tasks

    if not filtered:
        print("\n  No tasks to show.")
        return

    priority_order = {"High": 0, "Medium": 1, "Low": 2}
    filtered = sorted(filtered, key=lambda t: (t["done"], priority_order.get(t["priority"], 1)))

    priority_symbol = {"High": "!!!", "Medium": "! ", "Low": "  "}
    status_symbol   = {True: "x", False: " "}

    print()
    print(f"  {'ID':<5} {'':^3} {'P':<5} {'Title':<35} {'Created'}")
    print("  " + "-" * 65)

    for task in filtered:
        status   = status_symbol[task["done"]]
        priority = priority_symbol.get(task["priority"], "  ")
        title    = task["title"][:33] + ".." if len(task["title"]) > 35 else task["title"]
        print(f"  {task['id']:<5} [{status}]  {priority:<5} {title:<35} {task['created']}")

    print()
    total   = len(tasks)
    done    = sum(1 for t in tasks if t["done"])
    pending = total - done
    print(f"  Total: {total}  |  Done: {done}  |  Pending: {pending}")


def complete_task(tasks):
    view_tasks(tasks, filter_by="pending")
    try:
        task_id = int(input("  Enter task ID to mark as done: "))
    except ValueError:
        print("  [!] Invalid ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["done"]:
                print("  [!] Already marked as done.")
            else:
                task["done"] = True
                save_tasks(tasks)
                print(f"\n  [+] '{task['title']}' marked as done.")
            return

    print("  [!] Task not found.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("  Enter task ID to delete: "))
    except ValueError:
        print("  [!] Invalid ID.")
        return

    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            removed = tasks.pop(i)
            save_tasks(tasks)
            print(f"\n  [-] Deleted: '{removed['title']}'")
            return

    print("  [!] Task not found.")


def edit_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("  Enter task ID to edit: "))
    except ValueError:
        print("  [!] Invalid ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            print(f"  Current title: {task['title']}")
            new_title = input("  New title (leave blank to keep): ").strip()
            if new_title:
                task["title"] = new_title

            print(f"  Current priority: {task['priority']}")
            print("  Priority — 1) Low  2) Medium  3) High")
            choice = input("  Choose (leave blank to keep): ").strip()
            priority_map = {"1": "Low", "2": "Medium", "3": "High"}
            if choice in priority_map:
                task["priority"] = priority_map[choice]

            save_tasks(tasks)
            print(f"\n  [~] Task #{task_id} updated.")
            return

    print("  [!] Task not found.")


def search_tasks(tasks):
    keyword = input("  Search keyword: ").strip().lower()
    if not keyword:
        return

    results = [t for t in tasks if keyword in t["title"].lower()]

    if not results:
        print(f"\n  No tasks found matching '{keyword}'.")
    else:
        print(f"\n  Found {len(results)} result(s) for '{keyword}':")
        view_tasks(results)


def show_menu():
    print("\n" + "=" * 40)
    print("      DecodeLabs — To-Do Manager")
    print("=" * 40)
    print("  1. Add task")
    print("  2. View all tasks")
    print("  3. View pending tasks")
    print("  4. View completed tasks")
    print("  5. Mark task as done")
    print("  6. Edit task")
    print("  7. Delete task")
    print("  8. Search tasks")
    print("  9. Exit")
    print("=" * 40)


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("  Choose an option (1-9): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks, filter_by="pending")
        elif choice == "4":
            view_tasks(tasks, filter_by="done")
        elif choice == "5":
            complete_task(tasks)
        elif choice == "6":
            edit_task(tasks)
        elif choice == "7":
            delete_task(tasks)
        elif choice == "8":
            search_tasks(tasks)
        elif choice == "9":
            print("\n  Goodbye!\n")
            break
        else:
            print("\n  [!] Invalid option. Choose between 1 and 9.")


if __name__ == "__main__":
    main()
