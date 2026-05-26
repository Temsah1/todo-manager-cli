# DecodeLabs — CLI To-Do Manager 🚀

A robust, terminal-based To-Do List Application built with Python. This project allows users to manage their daily tasks efficiently through a Command Line Interface (CLI) with persistent data storage using JSON.

---

## ✨ Features
* **Persistent Storage:** Tasks are automatically saved and loaded from a `tasks.json` file.
* **Task Management:** Full CRUD operations (Create, Read, Update, Delete) for tasks.
* **Priority System:** Assign **High (!!!)**, **Medium (!)**, or **Low** priorities to your tasks.
* **Smart Sorting:** Tasks are automatically grouped by status (Pending vs Done) and sorted by priority.
* **Filters & Search:** Quick view filters for All, Pending, or Completed tasks, plus a keyword search feature.

---

## 📁 Project Structure
```text
decodelabs-todo-manager/
│
├── todo_list.py        # Main Python application file
├── tasks.json          # Database file (generated automatically)
├── .gitignore          # File to ignore unnecessary files
└── README.md           # Project documentation
```

---

## 🚀 How to Run the Project

### Prerequisites
Make sure you have **Python 3.x** installed on your system.

### Steps:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/decodelabs-todo-manager.git
   cd decodelabs-todo-manager
   ```

2. **Run the application:**
   ```bash
   python todo_list.py
   ```

---

## 🛠️ Built With
* **Python 3** (Standard Libraries: `json`, `os`, `datetime`)
