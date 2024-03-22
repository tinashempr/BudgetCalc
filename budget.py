class BudgetTracker:
    def _init_(self):
        self.income = []
        self.expenses = []

    def add_income(self, amount, source):
        self.income.append((amount, source))

    def add_expense(self, amount, expense):
        self.expenses.append((amount, expense))

    def calculate_savings(self):
        total_income = sum(amount for amount, source in self.income)
        total_expenses = sum(amount for amount, expense in self.expenses)
        return total_income - total_expenses

    def display_report(self):
        print("Income:")
        for amount, source in self.income:
            print(f"Source: {source}, Amount: {amount}")
        print("\nExpenses:")
        for amount, expense in self.expenses:
            print(f"Expense: {expense}, Amount: {amount}")
        print("\nTotal Income: ", sum(amount for amount, source in self.income))
        print("Total Expenses: ", sum(amount for amount, expense in self.expenses))
        print("Savings: ", self.calculate_savings())
