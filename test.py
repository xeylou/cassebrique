from tkinter import *
import tkinter as tk

flag=0
all_briques=[]

def move():
    global coord, direction, flag
    coord[0], coord[1] = coord[0] +direction[0], coord[1] + direction[1]
    if coord[0] >780 or coord[0] <10:
        direction[0] = direction[0]*-1
    if coord[1] >580 or coord[1] <10:
        direction[1] = direction[1]*-1
    coll=c.find_overlapping(c.coords(balle)[0],c.coords(balle)[1],c.coords(balle)[2],c.coords(balle)[3])
    if len(coll)> 1:
        print(coll)
        if coll[1]==2:
            direction[1]=direction[1]*-1
            coord[0], coord[1], coord[2], coord[3] = coord[0] +direction[0], coord[1] + direction[1], coord[2] + direction[0], coord[3] + direction[1]
        if coll[1]>2:
            c.delete(coll[1])
            if direction[0]>0 and direction[1]>0 or direction[0]<0 and direction[1]<0: #vers haut gauche ou bas droite
                direction[0]=direction[0]*-1
            elif direction[0]>0 and direction[1]<0 or direction[0]<0 and direction[1]>0: #vers haut droite ou bas gauche
                direction[1]=direction[1]*-1
    c.coords(balle, coord[0], coord[1], coord[0] + 15, coord[1] + 15)
    if flag >0:
        c.after(25,move)



def briques():
    parcours=[7.5, 10]
    color=['red','blue']
    Coul=0
    global flag, all_briques
    for i in range(1,11):
        for j in range(1,11):
            if parcours[0]==7.5:
                flag=0
                Coul=0
            elif parcours[0]==45:
                flag=1
                Coul=1
            brique = c.create_rectangle(parcours[0], parcours[1], parcours[0]+75, parcours[1]+25, fill=color[Coul], outline='white')
            all_briques.append(brique)
            parcours[0]+=75
            if Coul==0:
                Coul=1
            else:
                Coul=0
        if flag==0:
            parcours[0]=45
            flag=1
        else:
            parcours[0]=7.5
            flag=0
        parcours[1]+=25
    flag=0

def droite(event):
    if coordP[2]+15 < 800:
        c.move(paddle,15,0)
        coordP[0], coordP[2] = coordP[0]+15, coordP[2]+15
    else:
        pass
def gauche(event):
    if coordP[0]-15 > 0:
        c.move(paddle,-15,0)
        coordP[0], coordP[2] = coordP[0]-15, coordP[2]-15
    else:
        pass
        

def start_it():
    global flag
    if flag ==0:
        flag =1
        move()

fen1 = tk.Tk()
fen1.title('Casse-brique')

c = tk.Canvas(fen1, bg='black', height=600, width=800)
c.pack()

coord=[300,500,315,515]
direction=[10,5]
coordP=[300,550,450,560]
balle = c.create_oval(coord[0],coord[1],coord[2],coord[3],fill='red', outline='white')
paddle = c.create_rectangle(coordP[0],coordP[1],coordP[2],coordP[3],fill='orange', outline='white')

briques()    

tk.Button(fen1,text='Quitter', width = 8, command=fen1.destroy).pack(side=tk.BOTTOM)
tk.Button(fen1, text='Demarrer', width = 8, command=start_it).pack()

c.bind_all('<Right>', droite)
c.bind_all('<Left>' , gauche)

fen1.mainloop()


# import matploblib.pyplot as matpl

# def graphique():
#    matpl.bar(valeurs_x, valeurs_y)
#   par exemples clés et valeurs d'un dico
