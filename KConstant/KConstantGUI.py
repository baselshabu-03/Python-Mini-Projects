import tkinter as tk
from tkinter import messagebox, scrolledtext

def kaprekar_step(num):
    s = f"{num:04d}"
    desc_str = "".join(sorted(s, reverse=True))
    asc_str = "".join(sorted(s))
    desc = int(desc_str)
    asc = int(asc_str)
    result = desc - asc
    return desc_str, asc_str, result

def is_valid_input(s):
    if not s.isdigit() or not (1 <= len(s) <= 4):
        return False, "Enter 1 to 4 digits (e.g., 3524 or 378 for 0378)."
    padded = s.zfill(4)
    if len(set(padded)) == 1:
        return False, "Invalid: all digits are the same after padding (e.g., 1111 or 0000)."
    return True, ""

def run_kaprekar():
    user = entry.get().strip()
    valid, msg = is_valid_input(user)
    
    text_output.delete(1.0, tk.END)  # clear previous output

    if not valid:
        messagebox.showerror("Invalid Input", msg)
        return

    num = int(user.zfill(4))
    if num == 6174:
        text_output.insert(tk.END, "🔔 You've entered 6174 — it's already Kaprekar's constant.\n")
        return

    steps = 0
    text_output.insert(tk.END, "🔁 Performing Kaprekar routine:\n")
    while num != 6174 and steps < 20:
        desc_str, asc_str, num = kaprekar_step(num)
        steps += 1
        text_output.insert(tk.END, f"Step {steps}: {desc_str} - {asc_str} = {num:04d}\n")

    if num == 6174:
        text_output.insert(tk.END, f"\n✅ Reached 6174 in {steps} steps.\n")
    else:
        text_output.insert(tk.END, "\n⚠️ Stopped unexpectedly.\n")

def clear_fields():
    entry.delete(0, tk.END)
    text_output.delete(1.0, tk.END)

# Create main window
root = tk.Tk()
root.title("Kaprekar's Constant Finder")
root.geometry("500x400")

# Input section
tk.Label(root, text="Enter a number (1–4 digits):", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, font=("Arial", 12), width=15)
entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)
tk.Button(button_frame, text="Run", command=run_kaprekar, bg="#4CAF50", fg="white", width=10).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Clear", command=clear_fields, bg="#FF9800", fg="white", width=10).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Exit", command=root.destroy, bg="#F44336", fg="white", width=10).grid(row=0, column=2, padx=5)

# Output display
text_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 11), height=12)
text_output.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()