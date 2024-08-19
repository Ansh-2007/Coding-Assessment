import tkinter  # Import tkinter for GUI elements
from tkinter import ttk  # Import ttk for enhanced widgets
from tkinter import *  # Import the entire tkinter module
import random  # Import random module to generate random receipt numbers
from tkinter import messagebox  # Import messagebox for popup alerts
from PIL import Image, ImageTk  # Import PIL for handling images

# Initialize a set to store used receipt numbers to avoid duplication
used_receipt_numbers = set()

# Declare global variables to be used across functions
global first_name_entry, last_name_entry, hire_item_combobox, hire_item_no_entry, receipt_number, img

# Function to handle item returns
def return_page():
    # Global variable for the entry box where users input receipt numbers
    global return_receipt_no_entry

    # Function to process the return of an item based on the receipt number
    def process_return():
        receipt_number = return_receipt_no_entry.get()  # Get the receipt number from the input field
        if not receipt_number:
            # Warn the user if no receipt number is entered
            messagebox.showwarning("Warning", "Please enter a receipt number")
            return
    
        # Prepare to update the file by reading all lines
        updated_lines = []
        item_found = False
        try:
            with open("data.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    # Ensure the line has the correct format
                    parts = line.split(",")
                    if len(parts) >= 2 and parts[1].strip() == receipt_number:
                        item_found = True  # Item found, so it won't be added back to the list
                    else:
                        updated_lines.append(line)
                    
            # If item was found and removed, rewrite the updated data
            if item_found:
                with open("data.txt", "w") as file:
                    file.writelines(updated_lines)
                messagebox.showinfo("Success", "Item returned successfully")
            else:
                messagebox.showwarning("Warning", "Receipt number not found")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No data file found")

    # Create a new window for returning items
    return_window = tkinter.Toplevel()
    return_window.title("Julie's Party Hire")
    return_window.config(bg="light blue")

    # Create a frame to hold the return form
    return_frame = tkinter.Frame(return_window, bg="light blue")
    return_frame.pack()

    # Add a label frame to group return information
    return_frame_label = tkinter.LabelFrame(return_frame, text="Return Information", bg="white", font=("Helvetica", 12, "bold"))
    return_frame_label.grid(row=1, column=0, padx=10, pady=20)

    # Add a label and entry box for the receipt number
    return_receipt_no_label = tkinter.Label(return_frame_label, text="Receipt Number", bg="white", font=("Helvetica", 10))
    return_receipt_no_label.grid(row=0, column=0)

    return_receipt_no_entry = tkinter.Entry(return_frame_label)
    return_receipt_no_entry.grid(row=0, column=1)

    # Add a button to process the return
    return_button = tkinter.Button(return_frame_label, text="Return Item", command=process_return, bg="light blue", fg="black", font=("Helvetica", 10))
    return_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    return_button.config(height=1, width=20)

    # Function to confirm if the user wants to return to the homepage without saving data
    def homepage():
        question_box = tkinter.messagebox.askquestion("Exit Return page", "Are you sure you would like to return to homepage? Your details will not be saved if you return to homepage.", icon="warning")
        if question_box == "yes":
            return_window.destroy()

    # Add a "Back" button to return to the homepage
    back_button = tkinter.Button(return_frame, text="Back", command=homepage, bg="light blue", fg="black", font=("Helvetica", 10))
    back_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    back_button.config(height=1, width=20)

# Function to display all hired items
def display_hired_items():
    try:
        # Read all items from the data file
        file = open("data.txt", "r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No data file found")
        return

    # Create a new window to display the hired items
    display_window = tkinter.Toplevel(window)
    display_window.title("Hired Items")
    display_window.config(bg="light blue")

    # Frame to organize the display of items
    display_frame = tkinter.Frame(display_window, bg="light blue")
    display_frame.pack(padx=20, pady=20)

    # Loop through each line in the data file and display the items
    for line in lines:
        item = line.strip().split(',')
        if len(item) == 4:
            display = (f"Receipt Number: {item[1]}, Name: {item[0]}, Item: {item[2]}, Amount: {item[3]}")
            tkinter.Label(display_frame, text=display, bg="light blue", font=("Helvetica", 10)).pack()

    # Add a button to close the display window
    return_button = tkinter.Button(display_frame, text="Close", command=display_window.destroy, bg="white", fg="black", font=("Helvetica", 10))
    return_button.pack(pady=10)

# Function to handle the database entry of hired items
def data_base():
    # Get user inputs
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    item = hire_item_combobox.get()
    amount = hire_item_no_entry.get()

    # Ensure all fields are filled in
    if not first_name or not last_name or not item or not amount:
        messagebox.showwarning("Warning", "Please complete all fields")
        return

    # Validate the amount (ensure it's a number within a valid range)
    try:
        amount = int(amount)
        if amount < 1 or amount > 500:
            raise ValueError
    except ValueError:
            messagebox.showwarning("Warning!","Please enter a valid input for amount: from 1-500")
            return

    # Ensure the first and last names are alphabetical
    if not validate_name(first_name) or not validate_name(last_name):
        return

    # Generate a unique receipt number
    def generate_receipt_number():
        while True:
            receipt_number = random.randint(1000, 9999)
            if receipt_number not in used_receipt_numbers:
                used_receipt_numbers.add(receipt_number)
                return receipt_number
        
    receipt_number = generate_receipt_number()

    # Save the data to a file
    with open("data.txt", "a") as file:
        file.write(f"{first_name} {last_name},{receipt_number},{item},{amount}\n")
    
    # Clear the input fields
    first_name_entry.delete(0, tkinter.END)
    last_name_entry.delete(0, tkinter.END)
    hire_item_combobox.set("") 
    hire_item_no_entry.delete(0, tkinter.END)
    
    # Notify the user of success
    messagebox.showinfo("Success", "Data saved successfully")
    
    # Show the receipt details on a new page
    receipt_page(first_name, last_name, item, amount, receipt_number)

# Function to validate names (only alphabetical characters allowed)
def validate_name(name):
    if not name.replace(' ', '').isalpha():
        messagebox.showwarning("Warning", "Please enter alphabetical characters only in the name(s) field ")
        return False
    return True

# Function to display a receipt with user information
def receipt_page(first_name, last_name, item, amount, receipt_number):
    # Create a new window for the receipt
    receipt_window = tkinter.Tk()
    receipt_window.title("Receipt Information")
    receipt_window.config(bg="light blue")

    # Frame to hold receipt details
    receipt_frame = tkinter.Frame(receipt_window, bg="light blue")
    receipt_frame.pack()

    # Display the receipt details in labels
    receipt_display = tkinter.Label(receipt_frame, text=f"Receipt Number: {receipt_number}", bg="light blue", font=("Helvetica", 10))
    receipt_display.pack(pady=10)
    receipt_display = tkinter.Label(receipt_frame, text=f"First Name: {first_name}", bg="light blue", font=("Helvetica", 10))
    receipt_display.pack(pady=10)
    receipt_display = tkinter.Label(receipt_frame, text=f"Last Name: {last_name}", bg="light blue", font=("Helvetica", 10))
    receipt_display.pack(pady=10)
    receipt_display = tkinter.Label(receipt_frame, text=f"Item: {item}", bg="light blue", font=("Helvetica", 10))
    receipt_display.pack(pady=10)
    receipt_display = tkinter.Label(receipt_frame, text=f"Amount: {amount}", bg="light blue", font=("Helvetica", 10))
    receipt_display.pack(pady=10)

    # Add a close button for the receipt window
    return_button = tkinter.Button(receipt_frame, text="Close", command=receipt_window.destroy, bg="white", fg="black", font=("Helvetica", 10))
    return_button.pack(pady=10)

# Function to open the main window of the application
def main_window():
    # Create the main window
    global window
    window = tkinter.Tk()
    window.title("Julie's Party Hire Store")
    window.config(bg="light blue")

    # Create the main frame to organize the layout
    main_frame = tkinter.Frame(window, bg="light blue")
    main_frame.pack()

    # Add an image to the main window (resize and format the image)
    img = Image.open("julie.png")
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    img_label = tkinter.Label(main_frame, image=img, bg="light blue")
    img_label.grid(row=0, column=0)

    # Add a label with the title of the store
    store_label = tkinter.Label(main_frame, text="Julie's Party Hire", bg="light blue", font=("Helvetica", 16, "bold"))
    store_label.grid(row=1, column=0, padx=10, pady=20)

    # Create a label frame for user details
    label_frame = tkinter.LabelFrame(main_frame, text="Enter Your Details Below", bg="white", font=("Helvetica", 12, "bold"))
    label_frame.grid(row=2, column=0, padx=10, pady=20)

    # Add entry fields for first and last names
    first_name_label = tkinter.Label(label_frame, text="First Name", bg="white", font=("Helvetica", 10))
    first_name_label.grid(row=0, column=0)
    first_name_entry = tkinter.Entry(label_frame)
    first_name_entry.grid(row=0, column=1)

    last_name_label = tkinter.Label(label_frame, text="Last Name", bg="white", font=("Helvetica", 10))
    last_name_label.grid(row=1, column=0)
    last_name_entry = tkinter.Entry(label_frame)
    last_name_entry.grid(row=1, column=1)

    # Add a combobox for selecting hire items
    hire_item_label = tkinter.Label(label_frame, text="Item", bg="white", font=("Helvetica", 10))
    hire_item_label.grid(row=2, column=0)
    hire_item_combobox = ttk.Combobox(label_frame, values=["Balloons", "Banners", "Streamers", "Tables", "Chairs"])
    hire_item_combobox.grid(row=2, column=1)

    # Add an entry field for the number of items
    hire_item_no_label = tkinter.Label(label_frame, text="No. of Items", bg="white", font=("Helvetica", 10))
    hire_item_no_label.grid(row=3, column=0)
    hire_item_no_entry = tkinter.Entry(label_frame)
    hire_item_no_entry.grid(row=3, column=1)

    # Add buttons to submit the form, view hired items, and return an item
    submit_button = tkinter.Button(label_frame, text="Submit", command=data_base, bg="light blue", fg="black", font=("Helvetica", 10))
    submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    submit_button.config(height=1, width=20)

    display_items_button = tkinter.Button(main_frame, text="View Hired Items", command=display_hired_items, bg="light blue", fg="black", font=("Helvetica", 10))
    display_items_button.grid(row=5, column=0, padx=10, pady=10)
    display_items_button.config(height=1, width=20)

    return_button = tkinter.Button(main_frame, text="Return Item", command=return_page, bg="light blue", fg="black", font=("Helvetica", 10))
    return_button.grid(row=6, column=0, padx=10, pady=10)
    return_button.config(height=1, width=20)

    # Run the tkinter main event loop
    window.mainloop()

# Start the application
main_window()
