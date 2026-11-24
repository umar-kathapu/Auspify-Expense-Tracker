# 💰 Expense Tracker System

A simple Python-based Expense Tracker application that helps users manage their income and expenses, monitor their balance, and generate monthly financial reports. The application stores transaction data locally using JSON for persistent storage.

## 🚀 Features

- Add income transactions
- Add expense transactions
- Predefined income and expense categories
- View all transactions
- Delete transactions by ID
- Calculate total income and expenses
- View current balance
- Generate monthly financial reports
- JSON-based data persistence
- Input validation and error handling

## 🛠️ Technologies Used

- Python 3.11
- JSON
- Object-Oriented Programming (OOP)
- datetime
- Matplotlib

## 📂 Project Structure

```text
Task_5_Expense_Tracker/
│
├── main.py
├── expense_tracker.py
├── transactions.json
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Expense-Tracker.git
```

### 2. Navigate to the project directory

```bash
cd Expense-Tracker
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## ▶️ How to Run

Execute the following command:

```bash
python main.py
```

## 📋 Available Operations

| Option | Operation |
|---|---|
| 1 | Add Income |
| 2 | Add Expense |
| 3 | View Transactions |
| 4 | Delete Transaction |
| 5 | Balance Summary |
| 6 | Monthly Report |
| 7 | Exit |

## 💾 Data Storage

All transaction details are stored in `transactions.json`.

The application automatically saves transaction data and loads it when the application is restarted, ensuring previously recorded data is retained.

## 📊 Monthly Report

The monthly report provides:

- Total income for the selected month
- Total expenses for the selected month
- Net savings
- Number of transactions

## 🎯 Objective

The objective of this project is to develop a practical Python application for personal financial management while demonstrating Python programming, file handling, JSON data storage, OOP concepts, date/time handling, and input validation.

---

Developed as part of the **Auspify Technologies Python Development Internship**.