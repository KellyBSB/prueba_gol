# -*- coding: utf-8 -*-
"""
Created on Thu May 24 08:24:49 2018

@author: Kelly Soto
"""
from tkinter import*
#import vlc
#musica=vlc.MediaPlayer("Kalimba.mp3")
#musica.play()
tk=Tk()
tk.title("MeterGol")
canvas= Canvas(tk, width=700, height=555)
canvas.pack()
imagen1=PhotoImage(file="arco.gif")
canvas.create_image(0,0, anchor=NW, image=imagen1)
imagen2=PhotoImage(file="balon.gif")
canvas.create_image(555, 250, anchor=NW, image=imagen2)
def moverBalon(event):
    canvas.move(2,-5,0)
canvas.bind_all('<KeyPress-Left>', moverBalon)
anuncio= Label(text="Gol").place(x=500, y=0)
def moverBalon1(event):
    canvas.move(2,5,0)
canvas.bind_all('<KeyPress-Right>', moverBalon1)
#musica.stop()
tk.mainloop()

