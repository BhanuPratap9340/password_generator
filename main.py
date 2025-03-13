import string
import random
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        plen = int(entry_length.get())  # Get user input for password length
        if plen < 4:
            messagebox.showerror("Error", "Password length should be at least 4")
            return

        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation

        s = list(s1 + s2 + s3 + s4)
        random.shuffle(s)
        password = "".join(random.sample(s, plen))

        entry_password.config(state=tk.NORMAL)
        entry_password.delete(0, tk.END)  # Clear previous password
        entry_password.insert(0, password)  # Display new password
        entry_password.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    root.update()
    messagebox.showinfo("Success", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#2C3E50")  # Set background color

# Title Label
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white").pack(pady=10)

# Password Length Input
tk.Label(root, text="Enter Password Length:", font=("Arial", 12), bg="#2C3E50", fg="white").pack()
entry_length = tk.Entry(root, font=("Arial", 12), width=10, justify="center", bd=2, relief="solid")
entry_length.pack(pady=5)

# Generate Button
btn_generate = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), bg="#27AE60", fg="white",
                        activebackground="#1E8449", activeforeground="white", padx=10, pady=5, relief="raised",
                        command=generate_password)
btn_generate.pack(pady=10)

# Password Display
entry_password = tk.Entry(root, font=("Arial", 12), width=30, justify="center", bd=2, relief="solid", state="readonly")
entry_password.pack(pady=5)

# Copy Button
btn_copy = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12, "bold"), bg="#E74C3C", fg="white",
                    activebackground="#C0392B", activeforeground="white", padx=10, pady=5, relief="raised",
                    command=copy_to_clipboard)
btn_copy.pack(pady=10)

# Run the application
root.mainloop()