print('Welcome to Tic Tac Toe!')


player1 = input ("Enter name of Player 1:")
player2 = input ("Enter name of Player 2:")

import numpy as np
board = np.zeros((3,3),int)

B = board.astype(str)
print(B)

for x in range (0,5,1):
  print("It's", player1,"s","turn")
  c= int(input("Enter column:"))
  r= int(input("Enter row:"))
  B[r-1][c-1]= 'X'
  print(B)

  print("It's", player2,"s","turn")
  c= int(input("Enter column:"))
  r= int(input("Enter row:"))
  B[r-1][c-1]= 'O'
  print(B)

  if B[0][0] == 'X' and B[0][1] == 'X' and B[0][2] == 'X':
   print(player1, "wins!!!")
   break
  elif B[1][0] == 'X' and B[1][1] == 'X' and B[1][2] == 'X':
   print(player1, "wins!!!")
   break
  elif B[2][0] == 'X' and B[2][1] == 'X' and B[2][2] == 'X':
   print(player1, "wins!!!")
   break
  elif B[0][0] == 'X'and B[1][0] == 'X' and B[2][0] == 'X':
    print(player1, "wins!!!")
    break
  elif B[0][1] == 'X' and B[1][1] == 'X' and B[2][1] == 'X':
    print(player1, "wins!!!")
    break
  elif B[0][2] == 'X' and B[1][2] == 'X' and B[2][2] == 'X':
    print(player1, "wins!!!")
    break
  elif B[0][0] == 'X' and B[1][1]  == 'X' and B[2][2] == 'X':
    print(player1, "wins!!!")
    break
  elif B[2][0] == 'X' and B[1][1] == 'X' and B[0][2] == 'X':
    print(player1, "wins!!!")
    break
  elif B[0][0] == 'O' and B[0][1] == 'O' and B[0][2] == 'O':
    print(player2, "wins!!!")
    break
  elif B[1][0] == 'O' and B[1][1] == 'O' and B[1][2] == 'O':
    print(player2, "wins!!!")
    break
  elif B[2][0] == 'O' and B[2][1] == 'O' and B[2][2] == 'O':
    print(player2, "wins!!!")
    break
  elif B[0][0] == 'O' and B[1][0] == 'O' and B[2][0] == 'O':
    print(player2, "wins!!!")
    break
  elif B[0][1] == 'O' and B[1][1] == 'O' and B[2][1] == 'O':
    print(player2, "wins!!!")
    break
  elif B[0][2] == 'O' and B[1][2] == 'O' and B[2][2] == 'O':
    print(player2, "wins!!!")
    break
  elif B[0][0] == 'O' and B[1][1] == 'O' and B[2][2] == 'O':
    print(player2, "wins!!!")
    break
  elif B[2][0] == 'O' and B[1][1] == 'O' and B[0][2] == 'O':
    print(player2, "wins!!!")
    break
 # else:
    #  print("No one wins")
    #  break
