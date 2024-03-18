import tkinter as tk

import module.calculation
import module.login_logout

def login():
    root = tk.Tk()
    root.title('N-Tools')
    root.geometry("800x600")

    login_text = tk.StringVar()
    login_text.set('Logging in now...',)

    login_label = tk.Label(root, textvariable=login_text, font=('', 20))
    login_label.pack()

    root.update()
    s = module.login_logout.to_requests()

    login_text.set('Login Success!')

    return s, root