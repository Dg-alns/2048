import os
from tkinter import *
import random


# Fonction pour l'utilisation du clavier
def press(event,):
  if event.keysym == "Up":
    os.system("clear")
    print(load_board(movement("Up",board)))
  elif event.keysym == "Down":
    os.system("clear")
    print(load_board(movement("Down",board)))
  elif event.keysym == "Right":
    os.system("clear")
    print(load_board(movement("Right",board)))
  elif event.keysym == "Left":
    os.system("clear")
    print(load_board(movement("Left",board)))


fen= Tk()


# Fonction pour crée le plateau
def create_board() -> list[list[str]]:
  board = [[" " for _ in range(4)] for _ in range(4)]
  return board


# Fonction pour afficher le plateau
def load_board(board: list[list[str]]):
  for x in range (0,4):
      for y in range (0,4):
        if board[x][y]=="2048":
          print("Vous avez gagné !")
          exit()
      
  generate_nb(board)
  rows = len(board)
  cols = len(board[0])


  col_widths = [max(len(str(board[row][col])) for row in range(rows)) for col in range(cols)]

  top_border = "\t" + "+".join("-" * (width + 2) for width in col_widths)
  print(top_border)

  for row in range(rows):
      row_content = "\t|"
      for col in range(cols):
          cell_value = str(board[row][col]).center(col_widths[col])
          row_content += "{} | ".format(cell_value)
      print(row_content)

      separator = "\t" + "+".join("-" * (width + 2) for width in col_widths)
      print(separator)
  return ""


# Fonction pour générer un nombre aléatoire
def generate_nb(board: list[list[str]]):
  empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == " "]

  if not empty_cells:
    print("Fin du jeu. Aucun mouvement valide possible.")
    exit()

  
  rand_index = random.randint(0, len(empty_cells) - 1)
  i, j = empty_cells[rand_index]
  board[i][j] = str(random.randint(1, 10) == 1 and 4 or 2) # Génère 2 ou 4 aléatoirement



# Fonction pour déplacer les nombres dans le tableau et fusionner les tuiles 
def movement(mov, board): 
  if mov == "Left":
      for x in range(4):
          for y in range(1, 4):
              if board[x][y] != " ":
                
                  # Déplacez les tuiles
                  k = y
                  while k - 1 >= 0 and board[x][k - 1] == " ":
                      board[x][k - 1] = board[x][k]
                      board[x][k] = " "
                      k -= 1

                # Fusionnez les tuiles
                  temp_board=board
                  if k > 0 and board[x][k] == board[x][k - 1]:
                      combined_value = int(temp_board[x][k - 1]) * 2
                      temp_board[x][k - 1] = str(combined_value)
                      temp_board[x][k] = " "
                  board=temp_board

  elif mov == "Right":
      for x in range(4):
          for y in range(2, -1, -1):
              if board[x][y] != " ":
                  k = y
                  while k + 1 <= 3 and board[x][k + 1] == " ":
                      board[x][k + 1] = board[x][k]
                      board[x][k] = " "
                      k += 1

                
                  temp_board=board
                  if k < 3 and board[x][k] == board[x][k + 1]:
                      combined_value = int(temp_board[x][k + 1]) * 2
                      temp_board[x][k + 1] = str(combined_value)
                      temp_board[x][k] = " "
                  board=temp_board
                
  elif mov == "Up":
      for y in range(4):
          for x in range(1, 4):
              if board[x][y] != " ":
                  k = x
                  while k - 1 >= 0 and board[k - 1][y] == " ":
                      board[k - 1][y] = board[k][y]
                      board[k][y] = " "
                      k -= 1

                
                  temp_board=board
                  if k > 0 and board[k][y] == board[k - 1][y]:
                      combined_value = int(temp_board[k - 1][y]) * 2
                      temp_board[k - 1][y] = str(combined_value)
                      temp_board[k][y] = " "

  elif mov == "Down":
      for y in range(4):
          for x in range(2, -1, -1):
              if board[x][y] != " ":
                  k = x
                  while k + 1 <= 3 and board[k + 1][y] == " ":
                      board[k + 1][y] = board[k][y]
                      board[k][y] = " "
                      k += 1

                
                  temp_board=board
                  if k < 3 and board[k][y] == board[k + 1][y]:
                      combined_value = int(temp_board[k + 1][y]) * 2
                      temp_board[k + 1][y] = str(combined_value)
                      temp_board[k][y] = " "
                  board=temp_board
  return board


def game():
  global board
  board = create_board()
  generate_nb(board)
  print(load_board(board))

game()

fen.bind_all('<KeyPress>', press)
fen.mainloop()
