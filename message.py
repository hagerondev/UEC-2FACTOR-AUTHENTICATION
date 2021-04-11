import tkinter as tk
from tkinter import messagebox

title = "Auto Auth hg"

def warning(txt):
	root = tk.Tk()
	root.withdraw()
	tk.messagebox.showwarning(title,txt)

def info(txt):
	root = tk.Tk()
	root.withdraw()
	tk.messagebox.showinfo(title,txt)
