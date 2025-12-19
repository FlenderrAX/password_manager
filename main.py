from tkinter import Tk, Frame, Label, Entry, Button, StringVar, Checkbutton, BooleanVar, messagebox, Scale, IntVar
from PIL import Image, ImageTk
from utils.pass_gen import gen_password
from configs.config import CONFIG

def set_password():
    if not any([uppercase_var.get(), lowercase_var.get(), numbers_var.get(), symbols_var.get()]):
        for var in [uppercase_var, lowercase_var, numbers_var, symbols_var]:
            var.set(True)

    password = gen_password(
        length=length_var.get(),
        uppercase=uppercase_var.get(),
        lowercase=lowercase_var.get(),
        numbers=numbers_var.get(),
        symbols=symbols_var.get()
    )

    pass_var.set(password)

def copy_password():
    root.clipboard_clear()
    password_label_text = pass_var.get()
    if password_label_text != CONFIG.NOT_GENERATED:
        root.clipboard_append(password_label_text)
        root.update()
        messagebox.showinfo("Success", "Password has been successfully copied!")

root = Tk()
root.title(f"{CONFIG.ROOT_TITLE} - {CONFIG.AUTHOR} ")
ico = Image.open(CONFIG.APP_ICON_PATH)
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

main_frame = Frame(root)

title = Label(
    main_frame,
    padx = 10,
    pady = 10,
    text="Password Generator",
    font="Arial 40"
)

password_frame = Frame(main_frame)

pass_var = StringVar()
pass_var.set(CONFIG.NOT_GENERATED)
password_label = Entry(
    password_frame,
    width=20,
    textvariable=pass_var,
    state="disabled",
    font="Arial 20"
)

copy_button = Button(
    password_frame,
    text="Copy",
    command=lambda: copy_password()
)

gen_button = Button(
    main_frame,
    text="Generate password",
    font="Arial 15",
    command=lambda: set_password()
)

options_frame = Frame(main_frame)

uppercase_var = BooleanVar(value=True)
lowercase_var = BooleanVar(value=True)
numbers_var = BooleanVar(value=True)
symbols_var = BooleanVar(value=True)
length_var = IntVar()

length_option = Scale(
    options_frame,
    variable = length_var,
    from_ = 8,
    to = 16,
    orient="horizontal"
)

uppercase_option = Checkbutton(
    options_frame,
    text="Uppercase",
    font="Arial 12",
    variable=uppercase_var,
    onvalue=True,
    offvalue=False,
)

lowercase_option = Checkbutton(
    options_frame,
    text="Lowercase",
    font="Arial 12",
    variable=lowercase_var,
    onvalue=True,
    offvalue=False,
)

numbers_option = Checkbutton(
    options_frame,
    text="Numbers",
    font="Arial 12",
    variable=numbers_var,
    onvalue=True,
    offvalue=False,
)

symbols_option = Checkbutton(
    options_frame,
    text="Symbols",
    font="Arial 12",
    variable=symbols_var,
    onvalue=True,
    offvalue=False,
)

main_frame.pack(fill="both", expand=True, padx=20, pady=20)
title.pack()
password_frame.pack(expand=True, padx=20, pady=20)
password_label.grid(row=0, column=0)
copy_button.grid(row=0, column=1)
gen_button.pack(padx=10, pady=10)
options_frame.pack(expand=True, padx=20, pady=20)
length_option.grid(row=0, column=0)
uppercase_option.grid(row=1, column=0)
lowercase_option.grid(row=1, column=1)
numbers_option.grid(row=2, column=0)
symbols_option.grid(row=2, column=1)

root.mainloop()