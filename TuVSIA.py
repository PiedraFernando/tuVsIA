from tkinter import *
import random
import time
import threading
import copy

#recursos
colorFondo = "#2C1642"
frontColor = "#759C7E"
tipoDeLetra = "Minecraft"

#Clases
class player:
    caracter = ""
    x=0
    y=0
    def __init__(self,x,y,caracter):    
        self.caracter = caracter
        self.x=x
        self.y=y

#mapa
def getMapa(): #Crea el mapa
    mapa = [["█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█","█"]]
    for i in range(13):
        dato=[]
        dato.append("█")
        for j in range(28):
            aux = random.random()
            if(aux>0.7):
                dato.append("█")
            else:
                dato.append(" ")
        dato.append("█")
        mapa.append(dato)
    mapa.append(["█","█","█","█","█","█","█","█","█","█","█","█","█","█","█"," ","█","█","█","█","█","█","█","█","█","█","█","█","█","█"])
    mapa[player1.x][player1.y]=player1.caracter
    mapa[playerRecursivo.x][playerRecursivo.y]=playerRecursivo.caracter
    mapa[playerManjatan.x][playerManjatan.y]=playerManjatan.caracter
    return mapa  
def updateMapa(mapa): #convierte el array de mapa a string para imprimir
    mapaString=""
    for i in range(15):
        for j in range(30):
            mapaString+=mapa[i][j]
        mapaString+="\n"
    return mapaString

#movimientos
def up(player):  #mueve el player arriva
    if(mapa[player.x-1][player.y]!=" "):
        return
    else:
        mapa[player.x][player.y] = " "
        mapa[player.x-1][player.y] = player.caracter
        player.x-=1
    mapaString.set(updateMapa(mapa))
def down(player): #mueve el player abajo
    if(mapa[player.x+1][player.y]!=" "):
        return
    else:
        mapa[player.x][player.y] = " "
        mapa[player.x+1][player.y] = player.caracter
        player.x+=1
    mapaString.set(updateMapa(mapa))
def left(player): #mueve el player izquierda
    if(mapa[player.x][player.y-1]!=" "):
        return
    else:
        mapa[player.x][player.y] = " "
        mapa[player.x][player.y-1] = player.caracter
        player.y-=1
    mapaString.set(updateMapa(mapa))
def right(player): #mueve el player derecha
    if(mapa[player.x][player.y+1]!=" "):
        return
    else:
        mapa[player.x][player.y] = " "
        mapa[player.x][player.y+1] = player.caracter
        player.y+=1
    mapaString.set(updateMapa(mapa))

#Interfaz
def loadElements(): #genera toda la interfaz
    ventana = Tk()
    ventana.resizable(0,0)
    ventana.title("Laberintos")
    ventana.geometry("600x800")
    ventana.config(bg=colorFondo)

    #bottones Movimiento
    botonArriba = Button(ventana,text="↑",font=(tipoDeLetra,22),command=lambda: up(player1))
    botonArriba.place(x=280,y=600)
    botonArriba.config(width = "2",height="1")
    botonAbajo = Button(ventana,text="↓",font=(tipoDeLetra,22),command=lambda: down(player1))
    botonAbajo.place(x=280,y=700)
    botonAbajo.config(width = "2",height="1")
    botonIzquierda = Button(ventana,text="←",font=(tipoDeLetra,22),command=lambda: left(player1))
    botonIzquierda.place(x=230,y=650)
    botonIzquierda.config(width = "2",height="1")
    botonDerecha = Button(ventana,text="→",font=(tipoDeLetra,22),command=lambda: right(player1))
    botonDerecha.place(x=330,y=650)
    botonDerecha.config(width = "2",height="1")

    #mapa
    mapa = getMapa()
    mapaString = StringVar()
    mapaString.set(updateMapa(mapa))
    labelMapa = Label(ventana,fg=frontColor,textvariable=mapaString,bg=colorFondo,font=("Lucida Console",18))
    labelMapa.place(x=80,y=90)

    #labels
    labelTitulo = Label(ventana,fg=frontColor,text="Laberintos\n Tu VS IA",bg=colorFondo,font=(tipoDeLetra,18))
    labelTitulo.pack()
    labelMovimientos = Label(ventana,fg=frontColor,text="Movimientos:",bg=colorFondo,font=(tipoDeLetra,18))
    labelMovimientos.place(x=235,y=570)
    return ventana, mapa, mapaString

#AlgotitmosIA
def isNew(pos1,pos2):
    if(mapaVisita[pos1][pos2]==" "):
        mapaVisita[pos1][pos2] = "1"
        return True
    else:
        return False
def IARecursiva():
    if((playerRecursivo.x!=14 or playerRecursivo.y!=15) and  mapa[14][15]==" "):
        time.sleep(dificultad)
        if(mapa[playerRecursivo.x+1][playerRecursivo.y]==" " and isNew(playerRecursivo.x+1,playerRecursivo.y)):#verifica abajo
            down(playerRecursivo)
            IARecursiva()
            if(playerRecursivo.x==14 and playerRecursivo.y==15):
                return
            else:
                up(playerRecursivo)
        if(mapa[playerRecursivo.x][playerRecursivo.y+1]==" " and isNew(playerRecursivo.x,playerRecursivo.y+1)):#verifica derecha
            right(playerRecursivo)
            IARecursiva()
            if(playerRecursivo.x==14 and playerRecursivo.y==15):
                return
            else:
                left(playerRecursivo)
        if(mapa[playerRecursivo.x][playerRecursivo.y-1]==" " and isNew(playerRecursivo.x,playerRecursivo.y-1)):#verifica izquierda
            left(playerRecursivo)
            IARecursiva()
            if(playerRecursivo.x==14 and playerRecursivo.y==15):
                return
            else:
                right(playerRecursivo)
        if(mapa[playerRecursivo.x-1][playerRecursivo.y]==" " and isNew(playerRecursivo.x-1,playerRecursivo.y)):#verifica arriva
            up(playerRecursivo)
            IARecursiva()
            if(playerRecursivo.x==14 and playerRecursivo.y==15):
                return
            else:
                down(playerRecursivo)
def manhattan():
    follow = []
    while((playerManjatan.x!=14 or playerManjatan.y!=15) and mapa[14][15]==" "):
        time.sleep(dificultad)
        costo=1000000
        opc=0
        if(mapaVisitaManhattan[playerManjatan.x+1][playerManjatan.y]!=" " and mapaVisitaManhattan[playerManjatan.x][playerManjatan.y+1]!=" " and mapaVisitaManhattan[playerManjatan.x-1][playerManjatan.y]!=" " and mapaVisitaManhattan[playerManjatan.x][playerManjatan.y-1]!=" "):
            opc = follow.pop()
            if(opc==1):
                up(playerManjatan)
            elif(opc==2):
                left(playerManjatan)
            elif(opc==3):
                down(playerManjatan)
            else: 
                right(playerManjatan)
        else:
            if(mapaVisitaManhattan[playerManjatan.x+1][playerManjatan.y]==" "): #opcion hacia abajo
                costoVertical=0
                for i in range(1,(13-playerManjatan.x)):
                    if(mapaVisitaManhattan[playerManjatan.x+i][playerManjatan.y] == " "):
                        costoVertical+=1
                    else:
                        costoVertical+=100
                costoHorisontal=0
                for i in range(1,(15-playerManjatan.y)):
                    if(mapaVisitaManhattan[playerManjatan.x][playerManjatan.y+i] == " "):
                        costoHorisontal+=1
                    else:
                        costoHorisontal+=100
                if (costoHorisontal+costoVertical < costo):
                    costo = costoHorisontal+costoVertical
                    opc=1
            if(mapaVisitaManhattan[playerManjatan.x][playerManjatan.y+1]==" "): #opcion hacia derecha
                costoVertical=0
                for i in range(1,(13-playerManjatan.x)):
                    if(mapaVisitaManhattan[playerManjatan.x+i][playerManjatan.y] == " "):
                        costoVertical+=1
                    else:
                        costoVertical+=100
                costoHorisontal=0
                for i in range(1,(15-playerManjatan.y)):
                    if(mapaVisitaManhattan[playerManjatan.x][playerManjatan.y+i] == " "):
                        costoHorisontal+=1
                    else:
                        costoHorisontal+=100
                if (costoHorisontal+costoVertical < costo):
                    costo = costoHorisontal+costoVertical
                    opc=2
            if(mapaVisitaManhattan[playerManjatan.x-1][playerManjatan.y]==" "):
                costoVertical=0
                for i in range(1,(13-playerManjatan.x)):
                    if(mapaVisitaManhattan[playerManjatan.x+i][playerManjatan.y] == " "):
                        costoVertical+=1
                    else:
                        costoVertical+=100
                costoHorisontal=0
                for i in range(1,(15-playerManjatan.y)):
                    if(mapaVisitaManhattan[playerManjatan.x][playerManjatan.y+i] == " "):
                        costoHorisontal+=1
                    else:
                        costoHorisontal+=100
                if (costoHorisontal+costoVertical < costo):
                    costo = costoHorisontal+costoVertical
                    opc=3
            if(mapaVisitaManhattan[playerManjatan.x][playerManjatan.y-1]==" "):
                costoVertical=0
                for i in range(1,(13-playerManjatan.x)):
                    if(mapaVisitaManhattan[playerManjatan.x+i][playerManjatan.y] == " "):
                        costoVertical+=1
                    else:
                        costoVertical+=100
                costoHorisontal=0
                for i in range(1,(15-playerManjatan.y)):
                    if(mapaVisitaManhattan[playerManjatan.x][playerManjatan.y+i] == " "):
                        costoHorisontal+=1
                    else:
                        costoHorisontal+=100
                if (costoHorisontal+costoVertical < costo):
                    costo = costoHorisontal+costoVertical
                    opc=4
            if(opc==1):
                mapaVisitaManhattan[playerManjatan.x+1][playerManjatan.y]="1"
                down(playerManjatan)
                follow.append(1)
            elif(opc==2):
                mapaVisitaManhattan[playerManjatan.x][playerManjatan.y+1]="1"
                right(playerManjatan)
                follow.append(2)
            elif(opc==3):
                mapaVisitaManhattan[playerManjatan.x-1][playerManjatan.y]="1"
                up(playerManjatan)
                follow.append(3)
            else:
                mapaVisitaManhattan[playerManjatan.x][playerManjatan.y-1]="1"    
                left(playerManjatan)
                follow.append(4)

dificultad = 0.5
playerRecursivo = player(1,10,"░")
playerManjatan = player(1,1,"▓")
player1 = player(1,28,"#")
ventana,mapa,mapaString = loadElements()
mapaVisita = copy.deepcopy(mapa)
mapaVisitaManhattan = copy.deepcopy(mapa)
#hilos
hiloRecursivo = threading.Thread(name="hiloRecursivo",target=IARecursiva)
hiloRecursivo.start()
hiloManhattan = threading.Thread(name="hiloManhattan",target=manhattan)
hiloManhattan.start()
ventana.mainloop()