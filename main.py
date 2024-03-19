import tkinter as tk

import module.tk.init
import module.calculation
import module.tk.func

def main():
    s, root = module.tk.init.login()
    label = tk.Label(root, text='Length: ')
    label.pack()

    length_button = tk.Button(root, text='Get Length', command=lambda: label.config(text=module.tk.func.show_chapter_length_list(s, root)))
    length_button.pack()

    root.mainloop()

if __name__ == '__main__':
    main()