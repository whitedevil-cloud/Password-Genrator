import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    # Get user choices
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    # Define character sets based on user choices
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Check if at least one character set is selected
    if not characters:
        messagebox.showinfo("Error", "Please select at least one character set.")
        return

    # Generate password of specified length
    password_length = length_var.get()
    password = ''.join(random.choice(characters) for _ in range(password_length))

    # Display the generated password
    result_var.set(password)

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Variables for user choices
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
length_var = tk.IntVar(value=12)
result_var = tk.StringVar()

# Create GUI components
tk.Checkbutton(root, text="Uppercase", variable=uppercase_var).grid(row=0, column=0, sticky="w")
tk.Checkbutton(root, text="Lowercase", variable=lowercase_var).grid(row=1, column=0, sticky="w")
tk.Checkbutton(root, text="Digits", variable=digits_var).grid(row=2, column=0, sticky="w")
tk.Checkbutton(root, text="Symbols", variable=symbols_var).grid(row=3, column=0, sticky="w")

tk.Label(root, text="Password Length:").grid(row=4, column=0, pady=5)
tk.Scale(root, from_=4, to=30, orient="horizontal", variable=length_var).grid(row=4, column=1, pady=5)

tk.Button(root, text="Generate Password", command=generate_password).grid(row=5, column=0, columnspan=2, pady=10)

tk.Label(root, text="Generated Password:").grid(row=6, column=0, pady=5)
tk.Entry(root, textvariable=result_var, state="readonly", width=30).grid(row=6, column=1, pady=5)

# Run the main loop
root.mainloop()

'''
u_upper=str(input("You want uppercase char in passwd ? ")) and print("Next")
u_lower=str(input("You want Lowercase char in passwd ? ")) 
u_digiit=str(input("You want Digits char in passwd ? ")) 
u_sym=str(input("You want symbols char in passwd ? "))

if u_upper == "Y" or "N":
    print("Next")

elif u_lower == "Y" or  "N":
    print("Next")

elif u_digiit == "Y" or "N":
    print("Next")

elif u_sym == "Y" or "N":
    print("Wait...")

else:
    print("Invalid Input...")'''
