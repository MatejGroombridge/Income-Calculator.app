import tkinter as tk
initial = 2343


def add():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    result = int(initial + num1 - num2)
    result_label.config(text=("The total is $" + str(result) + ". Legend."))


# create the main window
root = tk.Tk()
root.title("Total Money")
root.resizable(False, False)

# create the widgets
num1_label = tk.Label(root, text="Profit:", font=("Calibri", 15))
num1_entry = tk.Entry(root, font=("Calibri", 15))
num2_label = tk.Label(root, text="Expenses:", font=("Calibri", 15))
num2_entry = tk.Entry(root, font=("Calibri", 15))
add_button = tk.Button(root, text="Submit", command=add, font=("Calibri", 15))
result_label = tk.Label(root, text="")

# layout the widgets
num1_label.grid(row=0, column=0, sticky="e", pady=10, padx=10)
num1_entry.grid(row=0, column=1, pady=10, padx=10)
num2_label.grid(row=1, column=0, sticky="e", pady=10, padx=10)
num2_entry.grid(row=1, column=1, pady=10, padx=10)
add_button.grid(row=2, column=0, columnspan=2,
                pady=10, padx=10)
result_label.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

# run the main loop
root.mainloop()


# How much money I had at the start of the year
# initial = 2343
# profit = input("Profit ($): ")
# expenses = input("Expenses ($): ")

# total = initial + int(profit) - int(expenses)

# print("\nYou have $" + str(total) + ". Legend.")

# input()
