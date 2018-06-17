#! /usr/bin/python3
# -*- coding: utf-8 -*-


from random import *
from tkinter import *


def new_game(n):                                    #Initialise la grille du jeu
    matrix = []

    for i in range(n):
        matrix.append([0] * n)
    return matrix

def add_two(mat):                                   #Initalise les deux premiers nombre qui apparaissent dans la grille
    a=randint(0,len(mat)-1)
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
	
def game_state(mat):                                #Regarde si dans la grille une fois avoir jouer il y a un 2048 et affiche g&gné sinon ca continue
    for i in range(len(mat)):                       #regarde au alentour de la taille de la grille
        for j in range(len(mat[0])):
            if mat[i][j]==16384:
                return 'win'
    for i in range(len(mat)-1):
        for j in range(len(mat[0])-1):
            if mat[i][j]==mat[i+1][j] or mat[i][j+1]==mat[i][j]:
                return 'Pas fini'
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==0:
                return 'Pas fini'
    for k in range(len(mat)-1):
        if mat[len(mat)-1][k]==mat[len(mat)-1][k+1]:
            return 'Pas fini'
    for j in range(len(mat)-1):
        if mat[j][len(mat)-1]==mat[j+1][len(mat)-1]:
            return 'Pas fini'
    return 'lose'                                   #Si aucune possibiltié d'ajouts, retourne perdu

def renverser(mat):                                   #fait bouger les cadres vers la droite et le bas
    new=[]
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0])-j-1])
    return new

def transposer(mat):                                 #fait bouger les cadres vers le haut et en bas
    new=[]
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new

def couvrir(mat):                              #crée une nouvelle grille et permet de fusionner vers le haut et de faire basculer toutes les cases
    new=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    done=False
    for i in range(7):
        count=0
        for j in range(7):
            if mat[i][j]!=0:
                new[i][count]=mat[i][j]
                if j!=count:
                    done=True
                count+=1
    return (new,done)

def ajouter(mat):                                #fusionne les cellules vers le bas et fait descendre le reste
    done=False
    for i in range(7):
         for j in range(6):
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

GRID_LEN = 7                                                                                   #Pour afficher toutes les cases
GRID_PADDING = 7                                                                             #La taille de la marge entre les cases

BACKGROUND_COLOR_GAME = "#57407c"                                                              #Couleur de la marge entre les cases
BACKGROUND_COLOR_CELL_EMPTY = "#3d2963"                                                        #Couleur de fond des cases quand elle sont vide
BACKGROUND_COLOR_DICT = {   2:"#41c9b8", 4:"#00b2a1", 8:"#ed5471", 16:"#e33c71", \
                            32:"#b81c64", 64:"#9e005d", 128:"#ffb33c", 256:"#f68530", \
                            512:"#e85938", 1024:"#B03A2E", 2048:"#AF7AC5",4096:"#5DADE2", 8192:"#00b2a1", 16384:"#ed5471", 32768:"#e33c71" }                    #Couleur du fond de la case en fonction du chiffre
CELL_COLOR_DICT = { 2:"#ffffff", 4:"#ffffff", 8:"#ffffff", 16:"#ffffff", \
                    32:"#ffffff", 64:"#ffffff", 128:"#ffffff", 256:"#ffffff", \
                    512:"#ffffff", 1024:"#ffffff", 2048:"#ffffff", 4096:"#ffffff",8192:"#ffffff", 16384:"#f9f6f2", 32768:"#f9f6f2" }                            #Couleur du chiffre de la case
FONT = ("Verdana", 30, "bold")

KEY_UP_ALT =111 
KEY_DOWN_ALT =116 
KEY_LEFT_ALT =113 
KEY_RIGHT_ALT =114 

KEY_UP_ALT1 = 38
KEY_DOWN_ALT1 = 40
KEY_LEFT_ALT1 = 37
KEY_RIGHT_ALT1 = 39

KEY_UP = "'z'"                                    #Commandes pour bouger en haut etc
KEY_DOWN = "'s'"
KEY_LEFT = "'q'"
KEY_RIGHT = "'d'"

class Grille7(Frame):                                   #FRAME = Cadre
    def __init__(self):
        Frame.__init__(self)

        self.grid()                                      #Je pense pour declarer la grille
        self.master.title('2048')                        #Titre de la grille
        self.master.bind("<Key>",self.key_down)

        self.commands = {   KEY_UP: up, KEY_DOWN: down, KEY_LEFT: left, KEY_RIGHT: right,
                            KEY_UP_ALT: up, KEY_DOWN_ALT: down, KEY_LEFT_ALT: left, KEY_RIGHT_ALT: right,
							KEY_UP_ALT1:up, KEY_DOWN_ALT1:down, KEY_LEFT_ALT1:left, KEY_RIGHT_ALT1:right}

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=BACKGROUND_COLOR_GAME)
        background.grid()
        for i in range(GRID_LEN):
            grid_row = []
            for j in range(GRID_LEN):
                cell = Frame(background, bg=BACKGROUND_COLOR_CELL_EMPTY)
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=FONT, width=4, height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def gen(self):
        return randint(0, GRID_LEN - 1)

    def init_matrix(self):
        self.matrix = new_game(7)
        self.matrix=add_two(self.matrix)
        self.matrix=add_two(self.matrix)

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
        key = event.keycode
        key1 = repr(event.char)
        if key in self.commands:
            self.matrix,done = self.commands[event.keycode](self.matrix)
            if done:
                self.matrix = add_two_four(self.matrix)
                self.update_grid_cells()
                done=False
                if game_state(self.matrix)=='win':
                    self.grid_cells[4][2].configure(text="Tu",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[4][3].configure(text="as",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[4][4].configure(text="ga",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[4][5].configure(text="gné!",bg=BACKGROUND_COLOR_CELL_EMPTY)
                if game_state(self.matrix)=='lose':
                    self.grid_cells[4][2].configure(text="Tu",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[4][3].configure(text="as",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[4][4].configure(text="per",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[4][5].configure(text="du!",bg=BACKGROUND_COLOR_CELL_EMPTY)
        elif key1 in self.commands:
            self.matrix,done = self.commands[repr(event.char)](self.matrix)
            if done:
                self.matrix = add_two_four(self.matrix)
                self.update_grid_cells()
                done=False
                if game_state(self.matrix)=='win':
                    self.grid_cells[4][2].configure(text="Tu",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[4][3].configure(text="as",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[4][4].configure(text="ga",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[4][5].configure(text="gné!",bg=BACKGROUND_COLOR_CELL_EMPTY)
                if game_state(self.matrix)=='lose':
                    self.grid_cells[4][2].configure(text="Tu",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[4][3].configure(text="as",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[4][4].configure(text="per",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[4][5].configure(text="du!",bg=BACKGROUND_COLOR_CELL_EMPTY)

    def generate_next(self):
        index = (self.gen(), self.gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (self.gen(), self.gen())
        self.matrix[index[0]][index[1]] = 2

#gamegrid = GameGrid7()
