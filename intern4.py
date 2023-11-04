import tkinter as tk
from tkinter import ttk
from tkinter import Label
from tkinter import messagebox



# Function to save contacts to a text file
def save_contacts():
    with open('contacts.txt', 'w') as file:
        for contact in contacts:
            file.write(','.join(contact) + '\n')

# Function to load contacts from a text file
def load_contacts():
    try:
        with open('contacts.txt', 'r') as file:
            for line in file:
                contact_data = line.strip().split(',')
                contacts.append(contact_data)
    except FileNotFoundError:
        pass

def add_contact():
    c_name = txt1.get()
    c_no = txt2.get()
    c_email = txt3.get()
    c_ad = txt4.get()
    contact = [c_name, c_no, c_email, c_ad]
    contacts.append(contact)
    clear_entries()
    save_contacts()  # Save the updated contact list

def view_contacts():
    contacts_window = tk.Toplevel(root)
    contacts_window.title('Contact List')

    row_num = 0

    for contact in contacts:
        Label(contacts_window, text='Contact Name:', fg='rosybrown').grid(row=row_num, column=0)
        Label(contacts_window, text=contact[0]).grid(row=row_num, column=1)

        Label(contacts_window, text='Phone Number:', fg='rosybrown').grid(row=row_num + 1, column=0)
        Label(contacts_window, text=contact[1]).grid(row=row_num + 1, column=1)

        Label(contacts_window, text='Email:', fg='rosybrown').grid(row=row_num + 2, column=0)
        Label(contacts_window, text=contact[2]).grid(row=row_num + 2, column=1)

        Label(contacts_window, text='Address:', fg='rosybrown').grid(row=row_num + 3, column=0)
        Label(contacts_window, text=contact[3]).grid(row=row_num + 3, column=1)

        ttk.Separator(contacts_window, orient=tk.HORIZONTAL).grid(row=row_num + 4, columnspan=2, sticky='ew')
        edit_button = tk.Button(contacts_window, text='Edit', command=lambda c=contact: edit_contact(c), fg='black', bg='MistyRose')
        edit_button.grid(row=row_num + 5, column=3)
        row_num += 6

def clear_entries():
    txt1.delete(0, 'end')
    txt2.delete(0, 'end')
    txt3.delete(0, 'end')
    txt4.delete(0, 'end')

def edit_contact(contact_to_edit):
    edit_window = tk.Toplevel(root)
    edit_window.title('Edit Contact')

    edit_name = tk.Entry(edit_window)
    edit_name.insert(0, contact_to_edit[0])
    edit_number = tk.Entry(edit_window)
    edit_number.insert(0, contact_to_edit[1])
    edit_email = tk.Entry(edit_window)
    edit_email.insert(0, contact_to_edit[2])
    edit_address = tk.Entry(edit_window)
    edit_address.insert(0, contact_to_edit[3])

    def save_changes():
        contact_to_edit[0] = edit_name.get()
        contact_to_edit[1] = edit_number.get()
        contact_to_edit[2] = edit_email.get()
        contact_to_edit[3] = edit_address.get()
        edit_window.destroy()
        save_contacts()  # Save the updated contact list

    save_button = tk.Button(edit_window, text="Save", command=save_changes, fg='black', bg='MistyRose')

    edit_name.pack()
    edit_number.pack()
    edit_email.pack()
    edit_address.pack()
    save_button.pack()

def delete_contact():
    contact_name_to_delete = txt6.get()
    contact_to_delete = None

    for contact in contacts:
        if contact[0].lower() == contact_name_to_delete.lower():
            contact_to_delete = contact
            break

    if contact_to_delete:
        contacts.remove(contact_to_delete)
        save_contacts()  # Save the updated contact list
        messagebox.showinfo("Contact Deleted", "The contact has been deleted.")
    else:
        messagebox.showinfo("Contact Not Found", "The contact does not exist.")



def search_contact():
    search_term = txt_search.get().lower()
    results = []

    for contact in contacts:
        if search_term in contact[0].lower() or search_term in contact[1].lower():
            results.append(contact)

    show_search_results(results)

def show_search_results(search_results):
    results_window = tk.Toplevel(root)
    results_window.title('Search Results')

    row_num = 0

    if not search_results:
        Label(results_window, text='No matching contacts found', fg='red').grid(row=0, column=0)
    else:
        for contact in search_results:
            Label(results_window, text='Contact Name:', fg='rosybrown').grid(row=row_num, column=0)
            Label(results_window, text=contact[0]).grid(row=row_num, column=1)

            Label(results_window, text='Phone Number:', fg='rosybrown').grid(row=row_num + 1, column=0)
            Label(results_window, text=contact[1]).grid(row=row_num + 1, column=1)

            Label(results_window, text='Email:', fg='rosybrown').grid(row=row_num + 2, column=0)
            Label(results_window, text=contact[2]).grid(row=row_num + 2, column=1)

            Label(results_window, text='Address:', fg='rosybrown').grid(row=row_num + 3, column=0)
            Label(results_window, text=contact[3]).grid(row=row_num + 3, column=1)

            ttk.Separator(results_window, orient=tk.HORIZONTAL).grid(row=row_num + 4, columnspan=2, sticky='ew')
            row_num += 6
root = tk.Tk()
root.title('Contact Book')

contacts = []
load_contacts()  # Load existing contacts when the application starts

lbl1 = tk.Label(root, text='Enter Contact Name:', padx=10, pady=10, fg='black', bg='MistyRose')
lbl2 = tk.Label(root, text='Enter Phone Number:', padx=10, pady=10, fg='black', bg='Lavender')
lbl3 = tk.Label(root, text='Enter E-mail:', padx=10, pady=10, fg='black', bg='MistyRose')
lbl4 = tk.Label(root, text='Enter Address:', padx=10, pady=10, fg='black', bg='Lavender')
lbl5 = tk.Label(root, text='Enter Contact name to search:', padx=10, pady=10, fg='black', bg='MistyRose')
lbl6 = tk.Label(root, text='Enter Contact name to be deleted:', padx=10, pady=10, fg='black', bg='Lavender')
frame = tk.Frame(root, borderwidth=10, relief='groove')
frame.grid(row=0, column=2, rowspan=10)

txt1 = tk.Entry(root)
txt2 = tk.Entry(root)
txt3 = tk.Entry(root)
txt4 = tk.Entry(root)
txt6= tk.Entry(root)

lbl1.grid(row=0, column=0, padx=10, pady=10)
lbl2.grid(row=1, column=0, padx=10, pady=10)
lbl3.grid(row=2, column=0, padx=10, pady=10)
lbl4.grid(row=3, column=0, padx=10, pady=10)
lbl5.grid(row=4, column=0, padx=10, pady=10)
lbl6.grid(row=5, column=0, padx=10, pady=10)


txt1.grid(row=0, column=1, padx=10, pady=10)
txt2.grid(row=1, column=1, padx=10, pady=10)
txt3.grid(row=2, column=1, padx=10, pady=10)
txt4.grid(row=3, column=1, padx=10, pady=10)
txt6.grid(row=5, column=1, padx=10, pady=10)

btn1 = tk.Button(root, text='Save', command=add_contact, fg='black', bg='Lavender')
btn2 = tk.Button(root, text='View Contact List', command=view_contacts, fg='black', bg='Lavender')

btn1.grid(row=6, column=0)
btn2.grid(row=6, column=1)

txt_search = tk.Entry(root)
btn_search = tk.Button(root, text='Search  a Contact', command=search_contact, fg='black', bg='MistyRose')
#delete = tk.Button(root, text='Delete a Contact', command=delete_contact, fg='black', bg='MistyRose')
btn_delete = tk.Button(root, text='Delete a Contact', command=delete_contact, fg='black', bg='MistyRose')




txt_search.grid(row=4, column=1, padx=10, pady=10)
btn_search.grid(row=7, column=0,padx=10,pady=10)
btn_delete.grid(row=7, column=1,padx=10,pady=10)


root.mainloop()

