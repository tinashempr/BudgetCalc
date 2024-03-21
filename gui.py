import tkinter as tk
from tkinter import messagebox

class PersonalBudgetCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Budget Calculator")
        
        # Create main frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=20, pady=20)

        # Create labels
        tk.Label(self.main_frame, text="Income:").grid(row=0, column=0)
        tk.Label(self.main_frame, text="Expense:").grid(row=1, column=0)
        tk.Label(self.main_frame, text="Savings Goal:").grid(row=2, column=0)

        # Create entry fields
        self.income_entry = tk.Entry(self.main_frame)
        self.expense_entry = tk.Entry(self.main_frame)
        self.savings_entry = tk.Entry(self.main_frame)

        self.income_entry.grid(row=0, column=1)
        self.expense_entry.grid(row=1, column=1)
        self.savings_entry.grid(row=2, column=1)

        # Create buttons
        self.add_button = tk.Button(self.main_frame, text="Add", command=self.add_transaction)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

    def add_transaction(self):
        income = self.income_entry.get()
        expense = self.expense_entry.get()
        savings = self.savings_entry.get()

        # Perform validation and processing here
        # For simplicity, just displaying the values for now
        messagebox.showinfo("Transaction Details", f"Income: {income}\nExpense: {expense}\nSavings Goal: {savings}")

def main():
    root = tk.Tk()
    app = PersonalBudgetCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
