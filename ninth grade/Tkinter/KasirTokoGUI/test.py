
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as msg
from time import strftime
import os
import sys
import tkinter.ttk as ttk
#from ttkthemes import ThemedStyle
from tkinter import Tk, Label, StringVar, ttk, Entry, Button, LabelFrame, Menu, Frame

from json import *
from datetime import *
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

Label(window, text='kodebarang: \t \t').grid(row=1,column=0)
kodebarangvar = StringVar()
kodebarangentry = Entry(window,width=50,textvariable=kepadavar)
kodebarangentry.grid(row=1,column=1)