import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tabs Example (Grid)")
root.geometry("400x300")

# Create Notebook (tab controller)
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky="nsew")  # use grid instead of pack

# Make window resize properly
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create frames for each tab
tab1 = tk.Frame(notebook, bg="lightblue")
tab2 = tk.Frame(notebook, bg="lightgreen")
tab3 = tk.Frame(notebook, bg="lightyellow")

# Add frames as tabs
notebook.add(tab1, text="Home")
notebook.add(tab2, text="Converter")
notebook.add(tab3, text="Patch Notes")

# Add content inside tabs (using grid now)
tk.Label(tab1, text="Welcome to the Home Tab", font=("Arial", 14), bg="lightblue").grid(row=0, column=0, padx=10, pady=10)
tk.Label(tab2, text="Converter Page", font=("Arial", 14), bg="lightgreen").grid(row=0, column=0, padx=10, pady=10)
tk.Label(tab3, text="Patch Notes Here", font=("Arial", 14), bg="lightyellow").grid(row=0, column=0, padx=10, pady=10)

root.mainloop()