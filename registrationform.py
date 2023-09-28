import tkinter as tk
from tkinter import messagebox

def register():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if not username or not password or not confirm_password:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    # Perform registration logic here
    # For simplicity, we'll just display the entered information
    messagebox.showinfo("Registration Successful", f"Username: {username}\nPassword: {password}")

root = tk.Tk()
root.title("Registration form")

# Create labels and entries for the registration form
label_username = tk.Label(root, text="Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

label_confirm_password = tk.Label(root, text="Confirm Password:")
label_confirm_password.pack()
entry_confirm_password = tk.Entry(root, show="*")
entry_confirm_password.pack()

# Create a button to trigger the registration process
register_button = tk.Button(root, text="Register", command=register)
register_button.pack()

root.mainloop()
