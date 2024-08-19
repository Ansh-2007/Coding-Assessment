import tkinter
from tkinter import ttk
import random
from tkinter import messagebox

# Declare global variables
global first_name_entry, last_name_entry, hire_item_combobox, hire_item_no_entry
 
def data_base():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()

    if first_name and last_name:
        receipt_number = random.randint(100, 999)
        item = hire_item_combobox.get()
        amount = hire_item_no_entry.get()
        with open("data.txt", "a") as file:
            file.write(f"{first_name} {last_name}, {receipt_number}, {item}, {amount}\n")
        first_name_entry.delete(0, tkinter.END)
        last_name_entry.delete(0, tkinter.END)
        hire_item_combobox.set("")  # Use set("") to clear the combobox
        hire_item_no_entry.delete(0, tkinter.END)
        messagebox.showinfo("Success", "Data saved successfully")
        receipt_page(first_name, last_name, item, amount, receipt_number)
    else:
        messagebox.showwarning("Warning", "Please enter both first and last name")

def receipt_page(first_name, last_name, item, amount, receipt_number):
    try:
        receipt_window = tkinter.Tk()
        receipt_window.title("Receipt")

        receipt_frame = tkinter.Frame(receipt_window)
        receipt_frame.pack()

        receipt_display = tkinter.Label(receipt_frame, text=f"Receipt Number: {receipt_number}")
        receipt_display.pack(pady=10)
        receipt_display = tkinter.Label(receipt_frame, text=f"First Name: {first_name}")
        receipt_display.pack(pady=10)
        receipt_display = tkinter.Label(receipt_frame, text=f"Last Name: {last_name}")
        receipt_display.pack(pady=10)
        receipt_display = tkinter.Label(receipt_frame, text=f"Item: {item}")
        receipt_display.pack(pady=10)
        receipt_display = tkinter.Label(receipt_frame, text=f"Amount: {amount}")
        receipt_display.pack(pady=10)
        
        return_button = tkinter.Button(receipt_frame, text="Back", command=receipt_window.destroy)
        return_button.pack()
        
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No data file found")

def hire_page():
    global first_name_entry, last_name_entry, hire_item_combobox, hire_item_no_entry
    hire_window = tkinter.Toplevel()
    hire_window.title("Julie's Party Hire")

    hire_frame = tkinter.Frame(hire_window)
    hire_frame.grid(sticky="w")

    hire_frame_label = tkinter.LabelFrame(hire_frame, text="Hire Information")
    hire_frame_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    first_name_label = tkinter.Label(hire_frame_label, text="First Name")
    first_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    first_name_entry = tkinter.Entry(hire_frame_label)
    first_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    last_name_label = tkinter.Label(hire_frame_label, text="Last Name")
    last_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    last_name_entry = tkinter.Entry(hire_frame_label)
    last_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    hire_item_label = tkinter.Label(hire_frame_label, text="Item")
    hire_item_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    hire_item_combobox = ttk.Combobox(hire_frame_label, values=["Table", "Chair", "Cutlery", "5-metre LED roll"])
    hire_item_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    hire_item_no_label = tkinter.Label(hire_frame_label, text="No. of items")
    hire_item_no_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    hire_item_no_entry = tkinter.Entry(hire_frame_label)
    hire_item_no_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    done_hire_button = tkinter.Button(hire_frame_label, text="Add To Cart", command=data_base)
    done_hire_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky= "news")
    done_hire_button.config(height=1, width=20)

    def homepage():
        question_box = tkinter.messagebox.askquestion("Exit Hire page","Are you sure you would like to return to homepage? Your details will not be saved if you return to homepage.", icon="warning")
        if question_box == "yes":
            hire_window.destroy()

    home_button = tkinter.Button(hire_frame, text="Home Page", command=homepage)
    home_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky= "news")
    home_button.config(height=0, width=20)

def return_page():
    global return_receipt_no_entry, return_first_name, return_item_combobox
    return_window = tkinter.Toplevel()
    return_window.title("Julie's Party Hire")

    return_frame = tkinter.Frame(return_window)
    return_frame.pack()

    return_frame_label = tkinter.LabelFrame(return_frame, text="Return Information")
    return_frame_label.grid(row=1, column=0, padx=10, pady=20)

    return_receipt_no = tkinter.Label(return_frame_label, text="Receipt Number")
    return_receipt_no.grid(row=0, column=0)

    return_receipt_no_entry = tkinter.Entry(return_frame_label)
    return_receipt_no_entry.grid(row=0, column=1)

    return_first_name_label = tkinter.Label(return_frame_label, text="First Name")
    return_first_name_label.grid(row=1, column=0)

    return_first_name = tkinter.Entry(return_frame_label)
    return_first_name.grid(row=1, column=1)

    return_item_label = tkinter.Label(return_frame_label, text="Item")
    return_item_label.grid(row=2, column=0)

    return_item_combobox = ttk.Combobox(return_frame_label, values=["Table", "Chair", "Cutlery", "5-metre LED roll"])
    return_item_combobox.grid(row=2, column=1, padx=10, pady=0)

    cart_button = tkinter.Button(return_frame_label, text="Remove From Cart", command=return_window.destroy)
    cart_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    cart_button.config(height=1, width=20)

    def homepage():
        question_box = tkinter.messagebox.askquestion("Exit Return page","Are you sure you would like to return to homepage? Your details will not be saved if you return to homepage.", icon="warning")
        if question_box == "yes":
            return_window.destroy()
    
    back_button = tkinter.Button(return_frame, text="Back", command=homepage)
    back_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    back_button.config(height=1, width=20)

window = tkinter.Tk()
window.title("Julie's Party Hire")
window.geometry("400x300")

hire_button = tkinter.Button(window, text="Hire", command=hire_page)
hire_button.pack(pady=10)
hire_button.config(height=1, width=20)

return_button = tkinter.Button(window, text="Return", command=return_page)
return_button.pack(pady=10)
return_button.config(height=1, width=20)

quit_button = tkinter.Button(window, text="Quit", command=quit)
quit_button.pack(pady=10)
quit_button.config(height=1, width=20)

def quit():
    question_box = tkinter.messagebox.askquestion("Exit","Are you sure you would like to quit the program?", icon="warning")
    if question_box == "yes":
        window.destroy()

window.mainloop()
