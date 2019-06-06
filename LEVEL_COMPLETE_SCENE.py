'''
Created on Jun 4, 2019

@author: s292252
'''

from tkinter import *
root = Tk()
root.title("Level Complete")
root.geometry("1000x750")









time_elapsed_display = Label(root, text = "Time elapsed: ")# + timer value
time_elapsed_display.grid(row=1, column=1)

level_display = Label(root, text = "Current level: ")# + level  value
level_display.grid(row=1, column=2)

streak_display = Label(root, text = "Streak: " + str(0))
streak_display.grid(row=1, column=3)

blank_space = Label(root, text = "     ")
blank_space.config(font=("Courier", 144)) 
blank_space.grid(row=2, column=4)

congratulations = Label(root, text = "LEVEL COMPLETE!")
congratulations.config(font=("Courier", 44)) 
congratulations.grid(row=3, column=4)

next_level = Button(root, text = "NEXT LEVEL")
next_level.config(height=2, width=12)
next_level.config(font=("Courier", 20))
next_level.grid(row=4, column=4)
# this wil start the next level

retrun2main = Button(root, text = "QUIT")
retrun2main.config(height=2, width=12)
retrun2main.config(font=("Courier", 20))
retrun2main.grid(row=5, column=4)
# this will run main()




root.mainloop()