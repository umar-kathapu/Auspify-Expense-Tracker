import json
import os
from datetime import datetime


class ExpenseTracker:

    def __init__(self, file_name="transactions.json"):
        self.file_name = file_name
        self.transactions = self.load_transactions()

    def load_transactions(self):
        if not os.path.exists(self.file_name):
            return []

        try:
            with open(self.file_name, "r") as file:
                return json.load(file)

        except (json.JSONDecodeError, IOError):
            return []

    def save_transactions(self):
        with open(self.file_name, "w") as file:
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self, transaction_type, amount, category, description):
        transaction = {
            "id": len(self.transactions) + 1,
            "type": transaction_type,
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.transactions.append(transaction)
        self.save_transactions()

        return transaction

    def get_transactions(self):
        return self.transactions

    def delete_transaction(self, transaction_id):
        for transaction in self.transactions:
            if transaction["id"] == transaction_id:
                self.transactions.remove(transaction)
                self.save_transactions()
                return True

        return False

    def get_summary(self):
        total_income = sum(
            t["amount"] for t in self.transactions
            if t["type"] == "income"
        )

        total_expenses = sum(
            t["amount"] for t in self.transactions
            if t["type"] == "expense"
        )

        balance = total_income - total_expenses

        return {
            "income": total_income,
            "expenses": total_expenses,
            "balance": balance
        }

    def get_monthly_report(self, year, month):
        monthly_transactions = []

        for transaction in self.transactions:
            transaction_date = datetime.strptime(
                transaction["date"], "%Y-%m-%d %H:%M:%S"
            )

            if transaction_date.year == year and transaction_date.month == month:
                monthly_transactions.append(transaction)

        income = sum(
            t["amount"] for t in monthly_transactions
            if t["type"] == "income"
        )

        expenses = sum(
            t["amount"] for t in monthly_transactions
            if t["type"] == "expense"
        )

        return {
            "income": income,
            "expenses": expenses,
            "savings": income - expenses,
            "transaction_count": len(monthly_transactions)
        }