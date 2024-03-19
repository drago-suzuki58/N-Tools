import tkinter as tk

import module.calculation

def show_chapter_length_list(s, root):
    chapter_list = module.calculation.get_all_chapter_length(s)
    print(chapter_list)#! debug
    listbox = tk.Listbox(root, height=600, width=500)
    listbox.pack()

    for course in chapter_list:
        listbox.insert(tk.END, f"{course[2]}     {course[1]}")