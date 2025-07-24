import tkinter as tk
from tkinter import ttk
from calc_function import division, seven, eight, nine, times, four, five, six, minus, one, two, three, plus, dot, zero, equal, AllClear, left_par, right_par, percent
import shared_variables

buttons = [
    ['/','7','8','9'],
    ['x','4','5','6'],
    ['-','1','2','3'],
    ['+','.','0','='],
    ['AC','(',')','%']
]

buttons_name = ['division','seven','eight','nine','times','four','five','six','minus','one','two','three','plus','dot','zero','equal','AllClear','left_par','right_par','percent']

def build_ui(root):
    frm = ttk.Frame(root, padding=10)
    frm_prev = ttk.Frame(root, padding=2)
    frm2 = ttk.Frame(root, padding=10)

    frm.grid()  
    frm_prev.grid()
    frm2.grid()

    prev_label = tk.Label(frm_prev, textvariable=shared_variables.prev_result, justify="right", ).grid(column=0, row=0 ,sticky="e")
    show = tk.Label(frm, textvariable=shared_variables.value, justify="right", background="#D3D3D3", width="25", border=2, borderwidth=1).grid(column=0, row=0, sticky="w")

    index = 0

    for row_index, row in enumerate(buttons, start=1):
        for col_index, text in enumerate(row):
            tk.Button(frm2, text=text, command=eval(buttons_name[index]), width=5).grid(column=col_index+1, row=row_index+1, padx=row_index-1, pady=row_index-1)
            index += 1



