import tkinter as tk
from tkinter import ttk
import csv
import os

class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

class ExpenseTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.expenses = []
        self.monthly_budget = tk.DoubleVar()
        
        # Load existing expenses from CSV file
        self.load_expenses_from_csv()

        # Budget Entry
        budget_frame = ttk.Frame(self.root)
        budget_frame.pack(pady=10)
        ttk.Label(budget_frame, text="Monthly Budget:").pack(side=tk.LEFT, padx=10)
        ttk.Entry(budget_frame, textvariable=self.monthly_budget).pack(side=tk.LEFT)

        # Expense Entry
        expense_frame = ttk.Frame(self.root)
        expense_frame.pack(pady=10)
        ttk.Label(expense_frame, text="Expense Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(expense_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(expense_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
        self.category_entry = ttk.Entry(expense_frame)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(expense_frame, text="Amount:").grid(row=2, column=0, padx=5, pady=5)
        self.amount_entry = ttk.Entry(expense_frame)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(expense_frame, text="Add Expense", command=self.add_expense).grid(row=3, columnspan=2, padx=5, pady=5)

        # View Expenses Button
        ttk.Button(self.root, text="View Expenses", command=self.view_expenses).pack(pady=10)

        # Summary Text
        self.summary_text = tk.Text(self.root, height=10, width=50)
        self.summary_text.pack()

    def load_expenses_from_csv(self):
        if os.path.exists('expenses.csv'):
            with open('expenses.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.expenses.append(Expense(row[0], row[1], float(row[2])))

    def add_expense(self):
        name = self.name_entry.get()
        category = self.category_entry.get()
        amount = float(self.amount_entry.get())

        expense = Expense(name, category, amount)
        self.expenses.append(expense)

        self.name_entry.delete(0, 'end')
        self.category_entry.delete(0, 'end')
        self.amount_entry.delete(0, 'end')

        # Write new expense to CSV file
        with open('expenses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([expense.name, expense.category, expense.amount])

    def view_expenses(self):
        total_expenses = sum(expense.amount for expense in self.expenses)
        remaining_budget = self.monthly_budget.get() - total_expenses
        daily_budget = remaining_budget / 30  # Assuming 30 days in a month

        self.summary_text.delete('1.0', tk.END)
        self.summary_text.insert(tk.END, f"Total Monthly Budget: ₹{self.monthly_budget.get():.2f}\n")
        self.summary_text.insert(tk.END, f"Total Expenses: ₹{total_expenses:.2f}\n")
        self.summary_text.insert(tk.END, f"Total Remaining Budget: ₹{remaining_budget:.2f}\n")
        self.summary_text.insert(tk.END, f"Daily Budget Remaining: ₹{daily_budget:.2f} per day\n")
        self.summary_text.insert(tk.END, "\nExpenses by Category:\n")

        expenses_by_category = {}
        for expense in self.expenses:
            if expense.category in expenses_by_category:
                expenses_by_category[expense.category] += expense.amount
            else:
                expenses_by_category[expense.category] = expense.amount

        for category, amount in expenses_by_category.items():
            self.summary_text.insert(tk.END, f"{category}: ₹{amount:.2f}\n")

def main():
    root = tk.Tk()
    app = ExpenseTrackerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
