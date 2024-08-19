import tkinter as tk
from tkinter import ttk, messagebox
import random

def quit_confirmation():
    quit_window = tk.Tk()
    quit_window.title("Quit Confirmation")

    quit_frame = tk.Frame(quit_window)
    quit_frame.pack()

    confirmation = tk.Label(quit_frame, text="Are you sure you want to quit?")
    confirmation.grid(row=0, column=0, columnspan=2, pady=10)

    def quit_close():
        quit_window.destroy()
        main_window.destroy()

    yes_button = tk.Button(quit_frame, text="Yes", command=quit_close, width=5)
    yes_button.grid(row=1, column=0, padx=10, pady=10)

    no_button = tk.Button(quit_frame, text="No", command=quit_window.destroy, width=5)
    no_button.grid(row=1, column=1, padx=10, pady=10)

    for widget in quit_frame.winfo_children():
        widget.grid_configure(padx=3)

def receipt_window():
    receipt_window = tk.Tk()
    receipt_window.title("Receipt")

    receipt_frame = tk.Frame(receipt_window)
    receipt_frame.pack()

    receipt_number = random.randint(1000, 9999)
    receipt_display = tk.Label(receipt_frame, text=f"Receipt Number: {receipt_number}")
    receipt_display.pack(pady=10)

    return_button = tk.Button(receipt_frame, text="Back", command=receipt_window.destroy)
    return_button.pack()

def hire_window():
    hire_window = tk.Toplevel(main_window)
    hire_window.title("Hire Form")

    hire_frame = tk.Frame(hire_window)
    hire_frame.pack()

    user_info_frame = tk.LabelFrame(hire_frame, text="Hire Information", padx=80, pady=80)
    user_info_frame.grid(row=0, column=0)

    first_name_label = tk.Label(user_info_frame, text="First Name:")
    first_name_label.grid(row=0, column=0)

    last_name_label = tk.Label(user_info_frame, text="Last Name:")
    last_name_label.grid(row=1, column=0)

    first_name_entry = tk.Entry(user_info_frame)
    first_name_entry.grid(row=0, column=1)

    last_name_entry = tk.Entry(user_info_frame)
    last_name_entry.grid(row=1, column=1)

    item_label = tk.Label(user_info_frame, text="Item Chosen:")
    item_label.grid(row=2, column=0)
    item_combobox = ttk.Combobox(user_info_frame, values=["Three", "one", "Two"])
    item_combobox.grid(row=2, column=1)

    amount_label = tk.Label(user_info_frame, text="Amount of item:")
    amount_label.grid(row=3, column=0)
    amount_spinbox = tk.Spinbox(user_info_frame, from_=1, to=500)
    amount_spinbox.grid(row=3, column=1)

    receipt_button = tk.Button(user_info_frame, text="Print Receipt", command=receipt_window, padx=20, width=10)
    receipt_button.grid(row=4, column=0)

    back_button = tk.Button(user_info_frame, text="Back", command=hire_window.destroy, padx=22, width=10)
    back_button.grid(row=5, column=0)

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(pady=5)

def refund_window():
    refund_window = tk.Toplevel(main_window)
    refund_window.title("Return Form")

    refund_frame = tk.Frame(refund_window)
    refund_frame.pack()

    refund_info_frame = tk.LabelFrame(refund_frame, text="Refund Information", padx=80, pady=80)
    refund_info_frame.grid(row=0, column=0)

    first_name_label = tk.Label(refund_info_frame, text="First Name:")
    first_name_label.grid(row=0, column=0)

    first_name_entry = tk.Entry(refund_info_frame, width=20)
    first_name_entry.grid(row=0, column=1)

    receipt_label = tk.Label(refund_info_frame, text="Receipt:")
    receipt_label.grid(row=1, column=0)

    receipt_entry = tk.Entry(refund_info_frame, width=20)
    receipt_entry.grid(row=1, column=1)

    item_label = tk.Label(refund_info_frame, text="Item Chosen:")
    item_label.grid(row=2, column=0)
    item_combobox = ttk.Combobox(refund_info_frame, values=["Three", "one", "Two"], width=20)
    item_combobox.grid(row=2, column=1)

    amount_label = tk.Label(refund_info_frame, text="Amount of item:")
    amount_label.grid(row=3, column=0)
    amount_spinbox = tk.Spinbox(refund_info_frame, from_=1, to=500, width=20)
    amount_spinbox.grid(row=3, column=1)

    back_button = tk.Button(refund_info_frame, text="Back", command=refund_window.destroy, padx=22, width=10)
    back_button.grid(row=10, column=0)

    for widget in refund_info_frame.winfo_children():
        widget.grid_configure(pady=5)

def validate_order(name, item, numofitem):
    if not name.isalpha():
        messagebox.showwarning("Warning", "You must only use alphabetical characters in your name")
        return False
    if not numofitem.isdigit() or not (1 <= int(numofitem) <= 500):
        messagebox.showwarning("Warning", "The maximum amount of items that can be hired is 500")
        return False
    return True

# Main window
main_window = tk.Tk()
main_window.title("Party Hire")

main_frame = tk.Frame(main_window, padx=80, pady=80)
main_frame.pack()

welcome_label = tk.Label(main_frame, text="Welcome to Party Hire. Would you like to hire or refund an item?")
welcome_label.grid(row=0, column=0, pady=10)

hire_button = tk.Button(main_frame, text="Hire", command=hire_window, width=20)
hire_button.grid(row=1, column=0, pady=10)

refund_button = tk.Button(main_frame, text="Returns/Refund", command=refund_window, width=20)
refund_button.grid(row=2, column=0, pady=10)

quit_button = tk.Button(main_frame, text="Quit", command=quit_confirmation, width=20)
quit_button.grid(row=3, column=0, pady=10)

for widget in main_frame.winfo_children():
    widget.grid_configure(pady=5)

main_window.mainloop()
