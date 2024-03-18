import tkinter as tk

import module.tk.init
import module.calculation

def main():
    s, root = module.tk.init.login()
    label = tk.Label(root, text='Length: ')
    label.pack()

    root.mainloop()

if __name__ == '__main__':
    main()