import tkinter as tk
from tkinter import ttk
import shared_variables
import window

root = tk.Tk()

shared_variables.value = tk.StringVar(value=shared_variables.calculation)
shared_variables.prev_result = tk.StringVar(value=shared_variables.prev_cal)

root.title("Calculator")

window.build_ui(root)

root.mainloop()
