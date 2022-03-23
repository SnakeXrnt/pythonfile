
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("390x844")
window.configure(bg = "#2F2F2F")


Login_canvas = Canvas(
    window,
    bg = "#2F2F2F",
    height = 844,
    width = 390,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    20.0,
    34.0,
    anchor="nw",
    text="Hi , \nPlease Login to\nContinue",
    fill="#FFEAEA",
    font=("RobotoRoman CondensedBlack", 37 * -1)
)

canvas.create_text(
    20.0,
    207.0,
    anchor="nw",
    text="Username : ",
    fill="#FFEAEA",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    20.0,
    311.0,
    anchor="nw",
    text="Password : ",
    fill="#FFEAEA",
    font=("Roboto", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    184.0,
    258.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#A1A1A1",
    highlightthickness=0
)
entry_1.place(
    x=32.0,
    y=235.0,
    width=304.0,
    height=44.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    184.0,
    362.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#A1A1A1",
    highlightthickness=0
)
entry_2.place(
    x=32.0,
    y=339.0,
    width=304.0,
    height=44.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=130.0,
    y=422.0,
    width=130.0,
    height=34.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    195.0,
    669.0,
    image=image_image_1
) 

def 
window.resizable(False, False)
window.mainloop()
