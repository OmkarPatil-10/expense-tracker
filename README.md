
# Expense Tracker GUI

This project is a simple Expense Tracker application built using Python and Tkinter. The application allows users to track their monthly expenses by adding expense details such as name, category, and amount. Users can also set a monthly budget and view a summary of their expenses, including remaining budget and expenses categorized by type.


## Features

- Set and track a monthly budget.
- Add expenses with name, category, and amount.
- View a summary of total expenses, remaining budget, and daily budget.
- View expenses categorized by type.
- Persistent storage of expenses using a CSV file.

## Requirements

- Python 3.x
- Tkinter (comes with standard Python installation)

## Installation

Run the application

```bash
  python gui.py
```
    
## Usage

1. Setting Monthly Budget:

- Enter your desired monthly budget in the "Monthly Budget" field.
2. Adding Expenses:

- Enter the expense name in the "Expense Name" field.
- Enter the expense category in the "Category" field.
- Enter the amount spent in the "Amount" field.
- Click the "Add Expense" button to add the expense to the tracker.
3. Viewing Expenses:

- Click the "View Expenses" button to see a summary of your expenses, including the total monthly budget, total expenses, remaining budget, daily budget remaining, and expenses categorized by type.

# Code Overview
## Expense Class
- The Expense class represents an individual expense with attributes for name, category, and amount.

## ExpenseTrackerGUI Class
The ExpenseTrackerGUI class handles the main functionality of the GUI application:

- Initializes the main window and widgets.
- Loads existing expenses from a CSV file.
- Adds new expenses to the list and updates the CSV file.
- Displays a summary of expenses and budget information.
## Functions
- load_expenses_from_csv: Loads existing expenses from a CSV file.
- add_expense: Adds a new expense to the tracker and updates the CSV file.
- view_expenses: Displays a summary of expenses, remaining budget, and expenses by category.

# Example

Below is an example of how to use the application:

1. Set a monthly budget.
2. Add expenses with details like name, category, and amount.
3. View the summary to check your total expenses and remaining budget.


# Contribution
Contributions are welcome! Please create a pull request or open an issue to discuss your ideas for improvements or new features.
