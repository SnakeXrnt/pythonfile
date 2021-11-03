import tkinter as tk

class Page01(tk.Frame):

    def __init__(self, parent, App):
        self.settings = App.settings

        super().__init__(parent)
        self.configure(bg="white")
        self.pack(fill="both", expand=True)

        self.pixelButton = tk.PhotoImage(width=1, height=1)

        self.create_frame01()
        self.create_frame02()
        self.create_frame03()
        # self.create_frame04()

    def create_frame01(self):
        frame01 = tk.Frame(self, bg="black", height=(self.settings.height//3))
        frame01.pack(side="top", fill="both")

        self.textNumber = tk.Label(frame01, text="0", font=("Arial", 65, "bold"), bg="black", fg="white")
        self.textNumber.pack(side="right")


    def create_frame02(self):
        self.frame02 = tk.Frame(self, bg="orange", height=(2*self.settings.height//3))
        self.frame02.pack(side="top", fill="both", expand=True)


    def create_frame03(self):
        frame03 = tk.Frame(self.frame02, bg="grey", width=(self.settings.width), height=(2*self.settings.height//3))
        frame03.pack(fill="both")

        width_btn = self.settings.width//4 - 10
        height_btn = self.settings.height//6

        # line1 = tk.Frame(frame03, bg="white", height=(self.settings.height//6), width=(3*self.settings.width//4))
        # line1.pack(fill="x")

        line2 = tk.Frame(frame03, bg="grey", height=(self.settings.height//6), width=(3*self.settings.width//4))
        line2.pack(fill="x")

        button7 = tk.Button(line2, text='7', font=("Arial",26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn)
        button7.pack(side="left", fill="x", expand=True)

        button8 = tk.Button(line2, text='8', font=("Arial",26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn)
        button8.pack(side="left", fill="x", expand=True)

        button9 = tk.Button(line2, text='9', font=("Arial",26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn)
        button9.pack(side="left", fill="x", expand=True)

        buttonPlus = tk.Button(line2, text="+", font=("Arial", 26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn, bg="orange")
        buttonPlus.pack(side="left", fill="x", expand=True)

        line3 = tk.Frame(frame03, bg="white", height=(self.settings.height//6), width=(3*self.settings.width//4))
        line3.pack(fill="x")

        button4 = tk.Button(line3, text='4', font=("Arial",26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn)
        button4.pack(side="left", fill="x", expand=True)

        button5 = tk.Button(line3, text='5', font=("Arial",26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn)
        button5.pack(side="left", fill="x", expand=True)

        button6 = tk.Button(line3, text='6', font=("Arial",26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn)
        button6.pack(side="left", fill="x", expand=True)

        buttonMin = tk.Button(line3, text="-", font=("Arial", 26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn, bg="orange")
        buttonMin.pack(side="left", fill="x", expand=True)

        line4 = tk.Frame(frame03, bg="grey", height=(self.settings.height//6), width=(3*self.settings.width//4))
        line4.pack(fill="x")

        button1 = tk.Button(line4, text='1', font=("Arial",26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn)
        button1.pack(side="left", fill="x", expand=True)

        button2 = tk.Button(line4, text='2', font=("Arial",26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn)
        button2.pack(side="left", fill="x", expand=True)

        button3 = tk.Button(line4, text='3', font=("Arial",26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn)
        button3.pack(side="left", fill="x", expand=True)

        buttonMult = tk.Button(line4, text="x", font=("Arial", 26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn, bg="orange")
        buttonMult.pack(side="left", fill="x", expand=True)

        line5 = tk.Frame(frame03, bg="white", height=(self.settings.height//6), width=(3*self.settings.width//4))
        line5.pack(fill="x")

        # frameButton0 = tk.Frame(line5, bg="pink", height=(self.settings.height//6), width=(self.settings.width//2))
        # frameButton0.pack(side="left", fill="y")
        buttonClear = tk.Button(line5, text='c', font=("Arial",26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn)
        buttonClear.pack(side="left", fill="both", expand=True)

        button0 = tk.Button(line5, text='0', font=("Arial",26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn)
        button0.pack(side="left", fill="both", expand=True)

        buttonEqual = tk.Button(line5, text='=', font=("Arial",26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn)
        buttonEqual.pack(side="left", fill="both", expand=True)

        buttonDiv = tk.Button(line5, text=':', font=("Arial",26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn)
        buttonDiv.pack(side="left", fill="both", expand=True)

        # frameButtonComa = tk.Frame(line5, bg="pink", height=(self.settings.height//6), width=(self.settings.width//8))
        # frameButtonComa.pack(side="left", fill="x", expand=True)

        # buttonComa = tk.Button(frameButtonComa, text=',', font=("Arial",26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn)
        # buttonComa.pack(side="left", fill="both", expand=True)


    # def create_frame04(self):
    #   frame04 = tk.Frame(self.frame02, bg="purple", width=(self.settings.width//4))
    #   frame04.pack(side="left", fill="y")

    #   buttondiv = tk.Button(frame04, text='   /   ', font=("Arial",26, "bold"), bg="orange")
    #   buttondiv.pack(fill="y", expand=True)

    #   buttonmult = tk.Button(frame04, text='  x  ', font=("Arial",26, "bold"), image=self.pixelButton, compound="c", width=width_btn, height=height_btn)
    #   buttonmult.pack(fill="y", expand=True)
