import tkinter as tk
from tkinter import messagebox
import secrets
import string
import random

 # Password Gen
def generate_password():
    
    # Must have one uppercase letter, one lowercase letter, one digit, and one punctuation character.

    try:
        length = int(entry.get())
        if length < 4:
            # Minimum length is 4 to accommodate all character type requirements
            raise ValueError("Password length must be at least 4.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer (minimum 4) for password length.")
        return
    
    # Define character sets for each requirement
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation

    # Ensure password has at least one of each required character type
    password_chars = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(punctuation)
    ]
    
    # If additional characters are needed, fill in the rest with a combined set
    if length > 4:
        all_characters = uppercase + lowercase + digits + punctuation
        password_chars.extend(secrets.choice(all_characters) for _ in range(length - 4))
    
    # Shuffle the list to avoid predictable sequences
    secure_random = random.SystemRandom()
    secure_random.shuffle(password_chars)
    
    # Join the characters into the final password string
    password = ''.join(password_chars)
    
    # Update the result label with the generated password
    result_label.config(text=password)

def copy_to_clipboard():

    # Copy the generated password to the system clipboard.
    password = result_label.cget("text")
    if password and password != "Your password will appear here":
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first before copying.")

# Create the main application window with a custom background color
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("450x300")
root.configure(bg="#2C3E50")  # Dark blue background

# Title label with a unique font and contrasting color
title_label = tk.Label(root, text="Secure Password Generator", bg="#2C3E50", fg="#ECF0F1", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

# Input frame with a raised border and a different background for visual contrast
input_frame = tk.Frame(root, bg="#34495E", bd=2, relief="raised")
input_frame.pack(pady=10, padx=20, fill="x")

# Label prompting the user to enter the desired password length
length_label = tk.Label(input_frame, text="Enter password length (min 4):", bg="#34495E", fg="#ECF0F1", font=("Helvetica", 12))
length_label.pack(pady=5)

# Entry widget for password length input
entry = tk.Entry(input_frame, width=10, font=("Helvetica", 12))
entry.pack(pady=5)
entry.insert(0, "16")  # Default length

# Button to generate the password, styled with custom colors and font
generate_button = tk.Button(root, text="Generate Password", command=generate_password,
                            bg="#1ABC9C", fg="white", font=("Helvetica", 12, "bold"),
                            relief="flat", bd=0, padx=10, pady=5)
generate_button.pack(pady=10)

# Label to display the generated password using a monospaced font for clarity
result_label = tk.Label(root, text="Your password will appear here", bg="#2C3E50", fg="#ECF0F1", font=("Courier", 14))
result_label.pack(pady=10)

# Button to copy the generated password to the clipboard, styled to match the overall design
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard,
                        bg="#E74C3C", fg="white", font=("Helvetica", 12, "bold"),
                        relief="flat", bd=0, padx=10, pady=5)
copy_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
