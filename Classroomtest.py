import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox

# Global dictionary to store user data
user_data = {}

def update_user_data():
    """Update the global user_data dictionary with current hiring status."""
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    key = f"{first_name} {last_name}"

    if first_name and last_name:
        if key not in user_data:
            user_data[key] = {
                'hired': False, 
                'receipt_number': None, 
                'item': None, 
                'item_amount': None
            }

def hire_page():
    """Displays the hire page where users can input their details and item information."""
    hire_window = tk.Toplevel()
    hire_window.title("Julie's Party Hire - Hire")

    hire_frame = tk.Frame(hire_window)
    hire_frame.grid(sticky="w", padx=10, pady=10)

    hire_frame_label = tk.LabelFrame(hire_frame, text="Hire Information")
    hire_frame_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    first_name_label = tk.Label(hire_frame_label, text="First Name")
    first_name_label.grid(row=0, column=0)

    last_name_label = tk.Label(hire_frame_label, text="Last Name")
    last_name_label.grid(row=1, column=0)

    global first_name_entry
    global last_name_entry
    first_name_entry = tk.Entry(hire_frame_label)
    first_name_entry.grid(row=0, column=1)

    last_name_entry = tk.Entry(hire_frame_label)
    last_name_entry.grid(row=1, column=1)

    hire_item_label = tk.Label(hire_frame_label, text="Item")
    hire_item_label.grid(row=2, column=0)

    hire_item_combobox = ttk.Combobox(hire_frame_label, values=["Table", "Chair", "Cutlery", "5-metre LED roll"], state="readonly")
    hire_item_combobox.grid(row=2, column=1, padx=10, pady=0)

    hire_item_no_label = tk.Label(hire_frame_label, text="No. of items")
    hire_item_no_label.grid(row=3, column=0)

    hire_item_no_spinbox = tk.Spinbox(hire_frame_label, from_=1, to=100)
    hire_item_no_spinbox.grid(row=3, column=1)

    def handle_hiring():
        """Store hiring information and print receipt."""
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        key = f"{first_name} {last_name}"

        if first_name and last_name:
            if key in user_data:
                item = hire_item_combobox.get()
                item_amount = hire_item_no_spinbox.get()
                if item and item_amount:
                    receipt_number = random.randint(1000, 9999)
                    user_data[key] = {
                        'hired': True,
                        'receipt_number': receipt_number,
                        'item': item,
                        'item_amount': item_amount
                    }
                    # Print receipt
                    receipt_page()
                    hire_window.destroy()
                else:
                    messagebox.showerror("Error", "Please select an item and specify the amount.")
            else:
                messagebox.showerror("Error", "User details not found.")

    handle_button = tk.Button(hire_frame_label, text="Add To Cart & Print Receipt", command=handle_hiring)
    handle_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    handle_button.config(height=1, width=20)

    def homepage():
        question_box = tk.messagebox.askquestion("Exit Hire page", "Are you sure you would like to return to homepage? Your details will not be saved if you return to homepage.", icon="warning")
        if question_box == "yes":
            hire_window.destroy()

    home_button = tk.Button(hire_frame, text="Home Page", command=homepage)
    home_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")
    home_button.config(height=0, width=20)

def receipt_page():
    """Displays the receipt page with the hire details."""
    receipt_window = tk.Toplevel()
    receipt_window.title("Receipt")

    receipt_frame = tk.Frame(receipt_window)
    receipt_frame.pack(padx=10, pady=10)

    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    key = f"{first_name} {last_name}"

    if key in user_data and user_data[key]['hired']:
        receipt_number = user_data[key]['receipt_number']
        item = user_data[key]['item']
        item_amount = user_data[key]['item_amount']
    else:
        receipt_number = random.randint(1000, 9999)
        item = "None"
        item_amount = "0"

    receipt_display = tk.Label(receipt_frame, text=f"Receipt Number: {receipt_number}\nName: {first_name} {last_name}\nItem: {item}\nAmount: {item_amount}")
    receipt_display.pack(pady=10)

    return_button = tk.Button(receipt_frame, text="Back", command=receipt_window.destroy)
    return_button.pack()

def return_page():
    """Displays the return page where users can return previously hired items."""
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    key = f"{first_name} {last_name}"

    if key not in user_data or not user_data[key]['hired']:
        messagebox.showerror("Error", "You have not hired any items. Cannot proceed with return.")
        return

    return_window = tk.Toplevel()
    return_window.title("Julie's Party Hire - Return")

    return_frame = tk.Frame(return_window)
    return_frame.pack(padx=10, pady=10)

    return_frame_label = tk.LabelFrame(return_frame, text="Return Information")
    return_frame_label.grid(row=1, column=0, padx=10, pady=20)

    return_receipt_no_label = tk.Label(return_frame_label, text="Receipt Number")
    return_receipt_no_label.grid(row=0, column=0)

    return_receipt_no_entry = tk.Entry(return_frame_label)
    return_receipt_no_entry.grid(row=0, column=1)
    return_receipt_no_entry.insert(0, user_data[key]['receipt_number'])
    return_receipt_no_entry.config(state="readonly")

    return_item_label = tk.Label(return_frame_label, text="Item")
    return_item_label.grid(row=1, column=0)

    return_item_combobox = ttk.Combobox(return_frame_label, values=["Table", "Chair", "Cutlery", "5-metre LED roll"], state="readonly")
    return_item_combobox.grid(row=1, column=1, padx=10, pady=0)
    return_item_combobox.set(user_data[key]['item'])

    return_item_no_label = tk.Label(return_frame_label, text="No. of items")
    return_item_no_label.grid(row=2, column=0)

    return_item_no_spinbox = tk.Spinbox(return_frame_label, from_=1, to=100)
    return_item_no_spinbox.grid(row=2, column=1)
    return_item_no_spinbox.delete(0, "end")
    return_item_no_spinbox.insert(0, user_data[key]['item_amount'])

    def remove_from_cart():
        """Remove item from the cart and update user data."""
        messagebox.showinfo("Item Removed", "Item has been removed from the cart.")
        user_data[key]['hired'] = False
        user_data[key]['receipt_number'] = None
        user_data[key]['item'] = None
        user_data[key]['item_amount'] = None
        return_window.destroy()

    cart_button = tk.Button(return_frame_label, text="Remove From Cart", command=remove_from_cart)
    cart_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    cart_button.config(height=1, width=20)

    def homepage():
        question_box = tk.messagebox.askquestion("Exit Return page", "Are you sure you would like to return to homepage? Your details will not be saved if you return to homepage.", icon="warning")
        if question_box == "yes":
            return_window.destroy()

    home_button = tk.Button(return_frame, text="Home Page", command=homepage)
    home_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")
    home_button.config(height=0, width=20)

def main_menu():
    """Displays the main menu with options to hire, return, or quit."""
    main_window = tk.Tk()
    main_window.title("Julie's Party Hire")

    def hire():
        main_window.destroy()
        hire_page()

    def return_items():
        main_window.destroy()
        return_page()

    def quit_app():
        main_window.destroy()

    menu_frame = tk.Frame(main_window)
    menu_frame.pack(padx=10, pady=10)

    hire_button = tk.Button(menu_frame, text="Hire", command=hire)
    hire_button.grid(row=0, column=0, padx=10, pady=10)
    hire_button.config(height=1, width=20)

    return_button = tk.Button(menu_frame, text="Return", command=return_items)
    return_button.grid(row=1, column=0, padx=10, pady=10)
    return_button.config(height=1, width=20)

    quit_button = tk.Button(menu_frame, text="Quit", command=quit_app)
    quit_button.grid(row=2, column=0, padx=10, pady=10)
    quit_button.config(height=1, width=20)

    main_window.mainloop()

# Start the application
main_menu()
