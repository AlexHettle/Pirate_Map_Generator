from tkinter import *
from collections import defaultdict
import random
#a dictionary that stores the locations of objects on the map and what
#type of object they are
object_dict=defaultdict(tuple)
#creates a single wave at coordinates x and y
def create_wave(x,y):
    the_canvas.create_line(x+25,y+35,x+25,y+55,x+55,y+55,smooth="true")
    the_canvas.create_line(x+25,y+35,x,y+55,x-25,y+55,smooth="true")
#creates a tree at coordinates x and y
def create_tree(x,y):
    the_canvas.create_polygon(x,y,x+15,y,x+7.5,y-20,outline="#886f2f",width=0)
    the_canvas.create_rectangle(x+5,y,x+10,y+5,outline="#886f2f",fill="black")
#creates a mountain at coordinates x and y
def create_mountain(x,y):
    the_canvas.create_polygon(x,y,x+20,y,x+10,y-20,outline="#886f2f",width=0)
    the_canvas.create_polygon(x-8,y,x+10,y,x,y-18,outline="#886f2f",width=0)
    the_canvas.create_polygon(x+10,y,x+30,y,x+20,y-13,outline="#886f2f",width=0)
#uses create_wave() to create a row of waves on the map all using the same
#y coordinate
def create_wave_line(y):
    for i in range(-100+random.randint(1,40),1200,100):create_wave(i,y)
#uses all previous wave related functions to create all waves on map
def create_ocean():
    create_wave_line(-25)
    create_wave_line(585)
    create_wave(120+random.randint(-10,10),25)
    create_wave(920+random.randint(-10,10),25)
    create_wave(120+random.randint(-10,10),525)
    create_wave(920+random.randint(-10,10),525)
    for i in range(25,535,50):
        create_wave(0+random.randint(-20,20),i)
        create_wave(1000+random.randint(30,50),i)
#places numerous circles in a region of the map determined randomly.
#Clumps numerous circles together to mimic a natural land formation
#Also randomly chooses where objects are located on the map and how many
#objects there are on the map
def create_chunk():
    boundx=random.randint(100,800)
    boundy=random.randint(100,350)
    for i in range(90):
        x=random.randint(boundx,boundx+200)
        y=random.randint(boundy,boundy+200)
        if random.randint(0,500)==50:object_dict[(x-12,y)]="tree"
        elif random.randint(0,500)==50:object_dict[(x-12,y)]="mountain"
        the_canvas.create_oval(x-25,y-25,x+25,y+25,outline="#cac090",fill="#cac090")
#Uses object_dict to place all objects to place all objects on the map in their
#previously determined locations
def place_objects():
    counter=0
    for key in object_dict:
        if counter==0:
            the_canvas.create_line(key[0]-10,key[1]-10,key[0]+10,key[1]+10,fill="red",width=4)
            the_canvas.create_line(key[0]-10,key[1]+10,key[0]+10,key[1]-10,fill="red",width=4)
            counter=1
            continue
        if object_dict[key]=="tree":create_tree(key[0],key[1])
        if object_dict[key]=="mountain":create_mountain(key[0],key[1])
#uses white circles around the canvas to make the map look more realistic
def create_tears():
    for i in range(-50,1100,random.randint(20,30)):
        the_canvas.create_oval(i,-6,i+random.randint(40,90),random.randint(0,5),fill="white",width=0)
    for i in range(-50,1100,random.randint(20,30)):
        the_canvas.create_oval(i,650,i+random.randint(40,90),650-random.randint(0,5),fill="white",width=0)
    for i in range(-50,700,random.randint(20,30)):
        the_canvas.create_oval(-20,i,random.randint(0,5),i+random.randint(40,90),fill="white",width=0)
    for i in range(-50,700,random.randint(20,30)):
        the_canvas.create_oval(1100,i,1100-random.randint(0,5),i+random.randint(40,90),fill="white",width=0)
#creates a compas in the lower-right corner of the map
def create_compass():
    the_canvas.create_oval(940,520,1060,640,fill="black",width=0)
    the_canvas.create_oval(950,530,1050,630,fill="#886f2f",width=0)
    the_canvas.create_polygon(990,570,1000,580,1000,525,fill="black")
    the_canvas.create_polygon(1010,570,1000,580,1000,530,fill="#cac090")
    the_canvas.create_polygon(1010,590,1000,580,1000,630,fill="black")
    the_canvas.create_polygon(990,590,1000,580,1000,630,fill="#cac090")
    the_canvas.create_polygon(990,590,1000,580,950,580,fill="black")
    the_canvas.create_polygon(990,570,1000,580,950,580,fill="#cac090")
    the_canvas.create_polygon(1010,570,1000,580,1050,580,fill="black")
    the_canvas.create_polygon(1010,590,1000,580,1050,580,fill="#cac090")
    the_canvas.create_text(1000, 505, text="N",font=("ms serif",20))
#clears all previousy generated map data and uses all previouslt declared
#functions to create the map
def create_map():
    the_canvas.delete("all")
    object_dict.clear()
    the_canvas.configure(bg="#b4a763")
    create_ocean()
    for i in range(random.randint(15,20)):create_chunk()
    place_objects()
    create_compass()
    create_tears()
#this chunk of code sets up the GUI for the application
window=Tk()
window.geometry("1000x600")
window.state("zoomed")
window.configure(bg="white")
title_lable=Label(text="MAP GENERATOR",font=("fixedsys",30),bg="white")
title_lable.place(x=1200,y=20)
the_canvas = Canvas(window,width=1100,height=650, highlightthickness=0)
the_canvas.configure(bg="white")
generate_button=Button(window,text="GENERATE",pady=15,padx=50,bg="grey",font=("fixedsys",25),command=create_map)
generate_button.place(x=1190,y=552)
the_canvas.pack(side=LEFT,anchor=NW)
create_map()
window.mainloop()
