##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!
# House outline code
#   house
square1 = drawpad.create_rectangle(0,400,200,600, fill='red')
#   roof
line1 = drawpad.create_line(0,400,100,350)
line2 = drawpad.create_line(200,400,100,350)
# Windows and door
#   windows
square2 = drawpad.create_rectangle(30,440,70,480, fill='white')
square3 = drawpad.create_rectangle(30,520,70,560, fill='white')
square4 = drawpad.create_rectangle(130,440,170,480, fill='white')
square5 = drawpad.create_rectangle(130,520,170,560, fill='white')
#   door
square6 = drawpad.create_rectangle(90,550,115,600, fill='white')
# Door handle plus chimney
#   handle
oval1 = drawpad.create_oval(93,575,96,580)
#   chimney
line3 = drawpad.create_line(140,370,140,330)
line4 = drawpad.create_line(140,330,180,330)
line5 = drawpad.create_line(180,330,180,390)




root.mainloop()
