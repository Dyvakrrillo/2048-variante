#! /usr/bin/python3
# -*- coding: utf-8 -*-
#


from random import *
from tkinter import *


def new_game(n):                                           #Initialise la grille du jeu avec des 0 
    matrix = []

    for i in range(n):
        matrix.append([0] * n)
    return matrix


def add_two(mat):
    a=randint(0,len(mat)-1)                                #Initialise la grille avec un nombre aleatoire 
    b=randint(0,len(mat)-1)
    while(mat[a][b]!=0):
        a=randint(0,len(mat)-1)
        b=randint(0,len(mat)-1)
    mat[a][b]=2
    return mat

def add_two_four(mat):
    choix = choice([2,4])
    a=randint(0,len(mat)-1)
    b=randint(0,len(mat)-1)
    while(mat[a][b]!=0):
        a=randint(0,len(mat)-1)
        b=randint(0,len(mat)-1)
    if choix == 2:
        mat[a][b]=2
    else:
        mat[a][b]=4
    return mat

	
def game_state(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==2048:                           #Regarde si dans la grille il y a un 2048 et retourne "win"                
                return 'win'
    for i in range(len(mat)-1): 
        for j in range(len(mat[0])-1):                    #Regarde si on peut encore additionner des nombres 
            if mat[i][j]==mat[i+1][j] or mat[i][j+1]==mat[i][j]:
                return 'Pas fini'
    for i in range(len(mat)): 
        for j in range(len(mat[0])):   
            if mat[i][j]==0:                              #Regarde si il y a encore une place de libre 
                return 'Pas fini'
    for k in range(len(mat)-1):
        if mat[len(mat)-1][k]==mat[len(mat)-1][k+1]:      #Regarde si on peut encore additionner des nombres 
            return 'Pas fini'
    for j in range(len(mat)-1): 
        if mat[j][len(mat)-1]==mat[j+1][len(mat)-1]:      #Regarde si on peut encore additionner des nombres 
            return 'Pas fini'
    return 'lose'


def renverser(mat):                                         #Fait bouger les cadres vers la droite et le bas 
    new=[]
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0])-j-1])
    return new


def transposer(mat):                                       #Fait bouger les cadres vers le haut et en bas 
    new=[]
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new


def couvrir(mat):
    new=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]         #Fusionne cellule 
    done=False
    for i in range(4):
        count=0
        for j in range(4):
            if mat[i][j]!=0:
                new[i][count]=mat[i][j]
                if j!=count:
                    done=True
                count+=1
    return (new,done)


def ajouter(mat):                                           #Fusionne cellule 
    done=False
    for i in range(4):
         for j in range(3):
             if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                 mat[i][j]*=2
                 mat[i][j+1]=0
                 done=True
    return (mat,done)


def up(game):
    print("up")
    game=transposer(game)
    game,done=couvrir(game)
    temp=ajouter(game)
    game=temp[0]
    done=done or temp[1]
    game=couvrir(game)[0]
    game=transposer(game)
    return (game,done)


def down(game):
    print("down")
    game=renverser(transposer(game))
    game,done=couvrir(game)
    temp=ajouter(game)
    game=temp[0]
    done=done or temp[1]
    game=couvrir(game)[0]
    game=transposer(renverser(game))
    return (game,done)


def left(game):
    print("left")
    game,done=couvrir(game)
    temp=ajouter(game)
    game=temp[0]
    done=done or temp[1]
    game=couvrir(game)[0]
    return (game,done)


def right(game):
    print("right")
    game=renverser(game)
    game,done=couvrir(game)
    temp=ajouter(game)
    game=temp[0]
    done=done or temp[1]
    game=couvrir(game)[0]
    game=renverser(game)
    return (game,done)

GRID_LEN = 4                                                                              #Pour afficher toutes les cases
GRID_PADDING = 7                                                                          #La taille de la marge entre les cases

BACKGROUND_COLOR_GAME = "#57407c"                                                         #Couleur de la marge entre les cases
BACKGROUND_COLOR_CELL_EMPTY = "#3d2963"
																						  #Couleur de fond des cases quand elle sont vide
BACKGROUND_COLOR_DICT = {   2:"#41c9b8", 4:"#00b2a1", 8:"#ed5471", 16:"#e33c71", \
                            32:"#b81c64", 64:"#9e005d", 128:"#ffb33c", 256:"#f68530", \
                            512:"#e85938", 1024:"#B03A2E", 2048:"#AF7AC5",4096:"#5DADE2", 8192:"#00b2a1", 16384:"#ed5471", 32768:"#e33c71" } 	 #Couleur du fond de la case en fonction du chiffre
							
CELL_COLOR_DICT = { 2:"#ffffff", 4:"#ffffff", 8:"#ffffff", 16:"#ffffff", \
                    32:"#ffffff", 64:"#ffffff", 128:"#ffffff", 256:"#ffffff", \
                    512:"#ffffff", 1024:"#ffffff", 2048:"#ffffff", 4096:"#ffffff",8192:"#ffffff", 16384:"#f9f6f2", 32768:"#f9f6f2" }                       #Couleur du chiffre de la case
					
FONT = ("Verdana", 30, "bold")                                                            #Si on change le chiffre sa change la taille de la grille afficher, le bold permet de mettre les chiffres en gras 

KEY_UP_ALT = 111
KEY_DOWN_ALT = 116    
KEY_LEFT_ALT = 113    
KEY_RIGHT_ALT = 114   

KEY_UP_ALT1 = 38
KEY_DOWN_ALT1 = 40
KEY_LEFT_ALT1 = 37
KEY_RIGHT_ALT1 = 39

KEY_UP = "'z'"                                                                            #Commandes pour bouger en haut etc
KEY_DOWN = "'s'"
KEY_LEFT = "'q'"
KEY_RIGHT = "'d'"


class Grille4(Frame):                                                                    #FRAME = Cadre
 
    def __init__(self):
        Frame.__init__(self)
        self.grid()                                                                       #Declarer le cadre 
        self.master.title('2048')                                                         #Titre de la grille
        self.master.bind("<Key>", self.key_down)                                          #Lance la fonction key_down  key est l'attribut


        self.commands = {   KEY_UP: up, KEY_DOWN: down, KEY_LEFT: left, KEY_RIGHT: right,
                            KEY_UP_ALT: up, KEY_DOWN_ALT: down, KEY_LEFT_ALT: left, KEY_RIGHT_ALT: right,
							KEY_UP_ALT1:up, KEY_DOWN_ALT1:down, KEY_LEFT_ALT1:left, KEY_RIGHT_ALT1:right}  	#Assigne les commandes avec les bonne fonction 

        self.grid_cells = []                                                              #Declare la grille 
        self.init_grid()                                                                  #Declere la fonction qui init la grille avec les bonnes taille etc 
        self.init_matrix()                                                                #Initialisation de la matrice 
        self.update_grid_cells()                                                          #Permet de modifier la grille en fonction des nombres qui sont a l'interieur 

        self.mainloop()                                                                   #Permet de bloquer la fenetre et donc d'attendre les instructions que on lui fournira ,j elle met egalement a jour l'interface graphique 


    def init_grid(self):
        background = Frame(self, bg=BACKGROUND_COLOR_GAME)                                #Initialise la grille de depart avec la couleur de fond et la taille , on a enlever la size 
        background.grid()                                                                 #Appelle background sur la grille 
        for i in range(GRID_LEN):
            grid_row = []                                                                 #Declare grille sous forme de liste, ici se seront des lignes que l'on ajoute a la grande liste grid_cells 
            for j in range(GRID_LEN):
                cell = Frame(background, bg=BACKGROUND_COLOR_CELL_EMPTY)                  #Couleur de fond des cases 
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)          #Appelle cell sur la grille
                t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=FONT, width=4, height=2)     #Taille des cellule, centrages des chiffres 
                t.grid()                                                                                                          #Apelle de t sur la grille
                grid_row.append(t)                                                        #On ajoute les cases a la grille au fur et a mesure 
            self.grid_cells.append(grid_row)                                              #On ajoute la ligne  
    

    def init_matrix(self):                    
        self.matrix = new_game(4)                   #appel la fonction qui créer la matrice
        self.matrix=add_two(self.matrix)            #ajoute une 1er case en appellant la fonction ass_two sur la matrix 
        self.matrix=add_two(self.matrix)            #ajoute une 2er case en appellant la fonction ass_two sur la matrix 


    def update_grid_cells(self):
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number), bg=BACKGROUND_COLOR_DICT[new_number], fg=CELL_COLOR_DICT[new_number])
        self.update_idletasks()


    def key_down(self, event):
        key = event.keycode                                                              #Pour les 4 fleches directionnels
        key1 = repr(event.char)                                                          #Pour les touches  z q s d              #print(key), print(self.commands)
        if key in self.commands:
            self.matrix,done = self.commands[event.keycode](self.matrix)
            if done:                                                                     #verifie les bonnes condition si la matrice a bouger 
                self.matrix = add_two_four(self.matrix)
                self.update_grid_cells()
                done=False
                if game_state(self.matrix)=='win':
                    self.grid_cells[1][1].configure(text="Ga",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Gné!",bg=BACKGROUND_COLOR_CELL_EMPTY)
                if game_state(self.matrix)=='lose':
                    self.grid_cells[1][1].configure(text="Pe",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="rdu!",bg=BACKGROUND_COLOR_CELL_EMPTY)
        elif key1 in self.commands:
            self.matrix,done = self.commands[repr(event.char)](self.matrix)
            if done:
                self.matrix = add_two_four(self.matrix)
                self.update_grid_cells()
                done=False
                if game_state(self.matrix)=='win':
                    self.grid_cells[1][1].configure(text="Ga",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="gné!",bg=BACKGROUND_COLOR_CELL_EMPTY)
                if game_state(self.matrix)=='lose':
                    self.grid_cells[1][1].configure(text="Pe",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="rdu!",bg=BACKGROUND_COLOR_CELL_EMPTY)

#gamegrid = GameGrid()
