import tkinter as tk

import module.tk.init
import module.get_result
import module.tk.func

def main():
    s, root = module.tk.init.login()
    label = tk.Label(root, text='Hello, World!')
    label.pack()

    length_button = tk.Button(root, text='Get Length', command=lambda: label.config(text=module.tk.func.show_chapter_length_list(s, root)))
    length_button.pack()

    question_button = tk.Button(root, text='Get Question', command=lambda: label.config(text=module.tk.func.show_chapter_question_list(s, root)))
    question_button.pack()

    root.mainloop()

if __name__ == '__main__':
    main()