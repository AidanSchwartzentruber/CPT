'''
Created on Jun 3, 2019

@author: s292252
'''

from tkinter import *
root = Tk()
root.title("Credits")
root.geometry("1000x750")





credits_title = Label(root, text = "CREDITS")
credits_title.config(font=("Courier", 44))
credits_title.pack()

by = Label(root, text = "By: Aidan Schwartzentruber and Francesca Berkoh")
by.config(font=("Courier", 20))
by.pack()
















root.mainloop()