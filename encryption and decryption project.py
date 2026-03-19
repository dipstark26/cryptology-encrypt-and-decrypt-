import tkinter as tk
from tkinter import ttk, messagebox

# Alphabet list
alp = list("abcdefghijklmnopqrstuvwxyz")

# --- Encryption Function ---
def encrypt(alp, key, name):
    result = []
    for char in name:
        if char == " ":
            result.append(" ")
        else:
            ind = alp.index(char)
            a = (key + ind) % 26
            result.append(alp[a])
    return "".join(result)

# --- Decryption Function ---
def decrypt(alp, key, name):
    result = []
    for char in name:
        if char == " ":
            result.append(" ")
        else:
            ind = alp.index(char)
            a = (ind - key) % 26
            result.append(alp[a])
    return "".join(result)

# --- GUI Functions ---
def process(action):
    input_text = entry.get().lower()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer")
        return
    
    if action == "encrypt":
        output = encrypt(alp, shift, input_text)
    else:
        output = decrypt(alp, shift, input_text)
    
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, output)

def copy_output():
    root.clipboard_clear()
    root.clipboard_append(result_box.get("1.0", tk.END).strip())
    messagebox.showinfo("Copied", "Output copied to clipboard!")

# --- Window Setup ---
root = tk.Tk()
root.title("Encryption & Decryption Tool")
root.geometry("500x300")

style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TLabel", font=("Segoe UI", 10))

# Input field
ttk.Label(root, text="Enter text:").pack(pady=5)
entry = ttk.Entry(root, width=50)
entry.pack(pady=5)

# Shift key
ttk.Label(root, text="Shift key:").pack(pady=5)
shift_entry = ttk.Entry(root, width=10)
shift_entry.insert(0, "3")
shift_entry.pack(pady=5)

# Buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Encrypt", command=lambda: process("encrypt")).grid(row=0, column=0, padx=10)
ttk.Button(button_frame, text="Decrypt", command=lambda: process("decrypt")).grid(row=0, column=1, padx=10)

# Result box
ttk.Label(root, text="Result:").pack(pady=5)
result_box = tk.Text(root, height=5, width=50, wrap="word", font=("Consolas", 11))
result_box.pack(pady=5)

# Copy button
ttk.Button(root, text="Copy Output", command=copy_output).pack(pady=10)

root.mainloop()
