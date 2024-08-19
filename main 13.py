#Task for 13 aug
#look at AS to see if anythings missed
#Validity
#colour



import tkinter
from tkinter import ttk
import random
from tkinter import messagebox

# Declare global variables
global first_name_entry, last_name_entry, hire_item_combobox, hire_item_no_entry, randInt



def return_page():
    global return_receipt_no_entry

    def process_return():
        receipt_number = return_receipt_no_entry.get()
        if not receipt_number:
            messagebox.showwarning("Warning", "Please enter a receipt number")
            return
        
        updated_lines = []
        item_found = False
        try:
            with open("data.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.split(",")[1].strip() != receipt_number:
                        updated_lines.append(line)
                    else:
                        item_found = True
            if item_found:
                with open("data.txt", "w") as file:
                    file.writelines(updated_lines)
                messagebox.showinfo("Success", "Item returned successfully")
            else:
                messagebox.showwarning("Warning", "Receipt number not found")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No data file found")

    return_window = tkinter.Toplevel()
    return_window.title("Julie's Party Hire")

    return_frame = tkinter.Frame(return_window)
    return_frame.pack()

    return_frame_label = tkinter.LabelFrame(return_frame, text="Return Information")
    return_frame_label.grid(row=1, column=0, padx=10, pady=20)

    return_receipt_no_label = tkinter.Label(return_frame_label, text="Receipt Number")
    return_receipt_no_label.grid(row=0, column=0)

    return_receipt_no_entry = tkinter.Entry(return_frame_label)
    return_receipt_no_entry.grid(row=0, column=1)

    return_button = tkinter.Button(return_frame_label, text="Return Item", command=process_return)
    return_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    return_button.config(height=1, width=20)

    def homepage():
        question_box = tkinter.messagebox.askquestion("Exit Return page", "Are you sure you would like to return to homepage? Your details will not be saved if you return to homepage.", icon="warning")
        if question_box == "yes":
            return_window.destroy()

    back_button = tkinter.Button(return_frame, text="Back", command=homepage)
    back_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    back_button.config(height=1, width=20)

def display_hired_items():

    try:
        file = open("data.txt", "r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        messsagebox.showwarning("Warning", "No data file found")
        return

    display_window = tkinter.Toplevel(window)
    display_window.title("Hired Items")

    display_frame = tkinter.Frame(display_window)
    display_frame.pack(padx=20, pady=20)

    for line in lines:
        item = line.strip().split(',')
        if len(item) == 4:
            display = (f"Receipt Number: {item[1]}, Name: {item[0]}, Item: {item[2]}, Amount: {item[3]}")
            tkinter.Label(display_frame, text = display).pack()

    return_button = tkinter.Button(display_frame, text="Close", command=display_window.destroy)
    return_button.pack(pady=10)


def data_base():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()

    if first_name and last_name:
        try:
            #def function to generate receipt number
            receipt_number = random.randint(100, 999)
            item = hire_item_combobox.get()
            amount = hire_item_no_entry.get()
            with open("data.txt", "a") as file:
                file.write(f"{first_name} {last_name},{receipt_number},{item},{amount}\n")
            first_name_entry.delete(0, tkinter.END)
            last_name_entry.delete(0, tkinter.END)
            hire_item_combobox.set("") 
            hire_item_no_entry.delete(0, tkinter.END)
            messagebox.showinfo("Success", "Data saved successfully")
            receipt_page(first_name, last_name, item, amount, receipt_number)
        except ValueError:
            message.showwarning("Warning", "Please enter a valid number of items (1-500).")
    else:
        messagebox.showwarning("Warning", "Please enter both first and last name")

def receipt_page(first_name, last_name, item, amount, receipt_number):
    receipt_window = tkinter.Tk()
    receipt_window.title("Receipt Information")

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

    return_button = tkinter.Button(receipt_frame, text="Close", command=receipt_window.destroy)
    return_button.pack(pady=10)



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
    done_hire_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="news")
    done_hire_button.config(height=1, width=20)

    def homepage():
        question_box = tkinter.messagebox.askquestion("Exit Hire page", "Are you sure you would like to return to homepage? Your details will not be saved if you return to homepage.", icon="warning")
        if question_box == "yes":
            hire_window.destroy()

    home_button = tkinter.Button(hire_frame, text="Home Page", command=homepage)
    home_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="news")
    home_button.config(height=0, width=20)

window = tkinter.Tk()
window.title("Julie's Party Hire")
window.geometry("400x300")

hire_button = tkinter.Button(window, text="Hire", command=hire_page)
hire_button.pack(pady=10)
hire_button.config(height=1, width=20)

return_button = tkinter.Button(window, text="Return", command=return_page)
return_button.pack(pady=10)
return_button.config(height=1, width=20)

view_receipts = tkinter.Button(window, text="View Receipt", command=display_hired_items)
view_receipts.pack(pady=10)
view_receipts.config(height=1, width=20)

quit_button = tkinter.Button(window, text="Quit", command=quit)
quit_button.pack(pady=10)
quit_button.config(height=1, width=20)

def quit():
    question_box = tkinter.messagebox.askquestion("Exit", "Are you sure you would like to quit the program?", icon="warning")
    if question_box == "yes":
        window.destroy()

window.mainloop()
