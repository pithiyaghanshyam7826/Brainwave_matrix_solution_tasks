import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self):
        self.balance = 1000
        self.pin = "1234"
        self.authenticated = False
        self.create_ui()

    def authenticate(self):
        entered_pin = self.pin_entry.get()
        if entered_pin == self.pin:
            self.authenticated = True
            self.show_main_menu()
        else:
            self.error_label.config(text="Incorrect PIN. Try again.", fg="red")

    def check_balance(self):
        self.balance_label.config(text=f"Current Balance: ${self.balance}")

    def deposit(self):
        amount = self.get_amount()
        if amount > 0:
            self.balance += amount
            self.balance_label.config(text=f"Current Balance: ${self.balance}")
            self.success_label.config(text="Deposit successful!", fg="green")
            self.clear_entry()
        else:
            messagebox.showerror("Error", "Invalid deposit amount.")

    def withdraw(self):
        amount = self.get_amount()
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.balance_label.config(text=f"Current Balance: ${self.balance}")
            self.success_label.config(text="Withdrawal successful!", fg="green")
            self.clear_entry()
        else:
            messagebox.showerror("Error", "Invalid withdrawal amount or insufficient funds.")

    def get_amount(self):
        try:
            return float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered.")
            return 0

    def clear_entry(self):
        self.amount_entry.delete(0, tk.END)

    def create_ui(self):
        self.root = tk.Tk()
        self.root.title("ATM Machine")
        self.root.geometry("400x500")
        self.root.configure(bg="#2c3e50")

        self.frame = tk.Frame(self.root, bg="#2c3e50")
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="Enter PIN:", fg="white", bg="#2c3e50", font=("Arial", 14)).pack(pady=5)
        self.pin_entry = tk.Entry(self.frame, show="*", font=("Arial", 14))
        self.pin_entry.pack(pady=5)

        tk.Button(self.frame, text="Authenticate", command=self.authenticate, font=("Arial", 14), bg="#27ae60", fg="white", width=15).pack(pady=10)
        
        self.error_label = tk.Label(self.frame, text="", fg="red", bg="#2c3e50", font=("Arial", 12))
        self.error_label.pack(pady=5)
        
        self.root.mainloop()

    def show_main_menu(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.balance_label = tk.Label(self.frame, text=f"Current Balance: ${self.balance}", fg="white", bg="#2c3e50", font=("Arial", 14))
        self.balance_label.pack(pady=10)

        tk.Label(self.frame, text="Enter Amount:", fg="white", bg="#2c3e50", font=("Arial", 14)).pack(pady=5)
        self.amount_entry = tk.Entry(self.frame, font=("Arial", 14))
        self.amount_entry.pack(pady=5)
        
        tk.Button(self.frame, text="Deposit", command=self.deposit, font=("Arial", 14), bg="#f39c12", fg="white", width=20).pack(pady=5)
        tk.Button(self.frame, text="Withdraw", command=self.withdraw, font=("Arial", 14), bg="#c0392b", fg="white", width=20).pack(pady=5)
        tk.Button(self.frame, text="Exit", command=self.root.destroy, font=("Arial", 14), bg="#7f8c8d", fg="white", width=20).pack(pady=10)

        self.success_label = tk.Label(self.frame, text="", fg="green", bg="#2c3e50", font=("Arial", 12))
        self.success_label.pack(pady=5)

if __name__ == "__main__":
    ATM()