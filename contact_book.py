import tkinter as tk
from tkinter import messagebox

contacts = {}


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


def add_contact():
    name = name_entry.get()
    phone_number = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name:
        contacts[name] = {
            "phone_number": phone_number,
            "email": email,
            "address": address,
        }
        update_contact_list()
        clear_fields()  # Clear the input fields after adding the contact
    else:
        messagebox.showerror("Error", "Name is required")


def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name in contacts:
        contact_listbox.insert(tk.END, name)


def display_contact(event):
    selected_contact = contact_listbox.get(contact_listbox.curselection())
    if selected_contact in contacts:
        contact_info = contacts[selected_contact]
        details_label.config(
            text=f"Phone Number: {contact_info['phone_number']}\nEmail: {contact_info['email']}\nAddress: {contact_info['address']}"
        )
    else:
        details_label.config(text="")


def delete_contact():
    selected_contact = contact_listbox.get(contact_listbox.curselection())
    if selected_contact in contacts:
        del contacts[selected_contact]
        update_contact_list()
        details_label.config(text="")
    else:
        messagebox.showerror("Error", "Please select a contact to delete")


root = tk.Tk()
root.title("Contact Book")

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone Number:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

contact_listbox = tk.Listbox(root)
contact_listbox.pack()
contact_listbox.bind("<<ListboxSelect>>", display_contact)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

details_label = tk.Label(root, text="")
details_label.pack()

root.mainloop()
