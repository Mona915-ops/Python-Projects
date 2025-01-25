import json
import os
from tkinter import *
from tkinter import messagebox

file_name = "contacts.json"

# Load contacts from file
def load_data():
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                messagebox.showwarning("Warning", "File is empty or corrupted. Initializing new contacts list.")
                return {}
    return {}

# Save contacts to file
def save_contacts():
    with open(file_name, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()

    if not name or not phone or not email:
        messagebox.showerror("Error", "All fields are required!")
        return

    if name in contacts:
        messagebox.showerror("Error", "Contact already exists!")
    else:
        contacts[name] = {"phone": phone, "email": email}
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        update_contact_list()

# View contacts
def update_contact_list():
    contact_list.delete(0, END)
    for name in contacts:
        contact_list.insert(END, name)

# Display contact details
def view_contact(event):
    try:
        selected_name = contact_list.get(contact_list.curselection())
        details = contacts[selected_name]
        entry_name.delete(0, END)
        entry_name.insert(0, selected_name)
        entry_phone.delete(0, END)
        entry_phone.insert(0, details["phone"])
        entry_email.delete(0, END)
        entry_email.insert(0, details["email"])
    except IndexError:
        pass

# Edit a contact
def edit_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()

    if not name or not phone or not email:
        messagebox.showerror("Error", "All fields are required!")
        return

    if name in contacts:
        contacts[name] = {"phone": phone, "email": email}
        messagebox.showinfo("Success", "Contact updated successfully!")
        clear_entries()
        update_contact_list()
    else:
        messagebox.showerror("Error", "No contact found with that name!")

# Delete a contact
def delete_contact():
    name = entry_name.get().strip()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        clear_entries()
        update_contact_list()
    else:
        messagebox.showerror("Error", "No contact found with that name!")

# Clear entry fields
def clear_entries():
    entry_name.delete(0, END)
    entry_phone.delete(0, END)
    entry_email.delete(0, END)

# Exit the application
def exit_app():
    save_contacts()
    root.destroy()

# Initialize main application
contacts = load_data()
root = Tk()
root.configure(bg="#0B0C10")  # Deep Space Black
root.title("Contact Management System")

# GUI Elements
frame = Frame(root, bg="#1C1E26")  # Cosmic Gray
frame.pack(pady=10)

Label(frame, text="Name:", bg="#1C1E26", fg="#FFD700", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)  # Star Yellow
entry_name = Entry(frame, width=30, bg="#2B2D42", fg="#E5E5E5", insertbackground="#FFD700")  # Meteor White
entry_name.grid(row=0, column=1, padx=5, pady=5)

Label(frame, text="Phone:", bg="#1C1E26", fg="#FFD700", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
entry_phone = Entry(frame, width=30, bg="#2B2D42", fg="#E5E5E5", insertbackground="#FFD700")
entry_phone.grid(row=1, column=1, padx=5, pady=5)

Label(frame, text="Email:", bg="#1C1E26", fg="#FFD700", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5)
entry_email = Entry(frame, width=30, bg="#2B2D42", fg="#E5E5E5", insertbackground="#FFD700")
entry_email.grid(row=2, column=1, padx=5, pady=5)

btn_frame = Frame(root, bg="#0B0C10")
btn_frame.pack(pady=10)

Button(btn_frame, text="Add Contact", command=add_contact, width=15, bg="#7F00FF", fg="#FFFFFF", activebackground="#6A0572", activeforeground="#FFFFFF").grid(row=0, column=0, padx=5)
Button(btn_frame, text="Edit Contact", command=edit_contact, width=15, bg="#7F00FF", fg="#FFFFFF", activebackground="#6A0572", activeforeground="#FFFFFF").grid(row=0, column=1, padx=5)
Button(btn_frame, text="Delete Contact", command=delete_contact, width=15, bg="#7F00FF", fg="#FFFFFF", activebackground="#6A0572", activeforeground="#FFFFFF").grid(row=0, column=2, padx=5)
Button(btn_frame, text="Clear", command=clear_entries, width=15, bg="#7F00FF", fg="#FFFFFF", activebackground="#6A0572", activeforeground="#FFFFFF").grid(row=0, column=3, padx=5)

list_frame = Frame(root, bg="#0B0C10")
list_frame.pack(pady=10)

Label(list_frame, text="Contacts:", bg="#0B0C10", fg="#FFD700", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
contact_list = Listbox(list_frame, width=50, height=10, bg="#2B2D42", fg="#E5E5E5", selectbackground="#7F00FF", selectforeground="#FFD700")
contact_list.grid(row=1, column=0, padx=5, pady=5)
contact_list.bind("<<ListboxSelect>>", view_contact)

Button(root, text="Exit", command=exit_app, width=15, bg="#7F00FF", fg="#FFFFFF", activebackground="#6A0572", activeforeground="#FFFFFF").pack(pady=10)

# Populate contact list on startup
update_contact_list()

root.mainloop()
