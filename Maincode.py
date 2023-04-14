import random
import math  

def check_move(board, turn, col, pop):
    r=int(len(board)/7)
    if col<0 or col>6:
        return False
    elif pop<0 or pop>1:
        return False
    else:
        if pop==0:
            for i in range(r-1, -1, -1):
              if board[i*7+col]==0:
               return True
               break
              if i==0:
               return False
        else:
            if board[col]==turn:
                return True
            return False

def apply_move(board, turn, col, pop):
    r=int(len(board)/7)
    new_board = board.copy()
    if pop==0:
        for i in range(0,r):
            if new_board[i*7+col]==0:
                new_board[i*7+col]=turn
                break
        return new_board
    else:
        for i in range(0, r):
            if new_board[i*7+col]==turn:
                for j in range(i, r-1):
                    new_board[j*7+col]=new_board[j*7+7+col]
                new_board[(r-1)*7+col]=0
                break
        return new_board

def check_column_victory(board, who_played):
    r=int(len(board)/7)
    for j in range (0, 7):
        count=0
        value=0
        for i in range (0, r):
            if board[i*7+j]==who_played:
                count+=1
                if count==4:
                 value=1
                 break
            else:
                count=0
        if value==1:
            return True
    if j==6:
        return False

def check_row_victory(board, who_played):
    r=int(len(board)/7)
    for i in range (0, r):
        count=0
        value=0
        for j in range (0, 7):
            if board[i*7+j]==who_played:
                count+=1
                if count==4:
                 value=1
                 break
            else:
                count=0
        if value==1:
            return True
    if i==r-1:
        return False

def check_diagonal_victory(board, who_played):
    r=int(len(board)/7)
    for j in range(0, 7):
     i=0
     count=0
     while i<r and j<7:
        if board[i*7+j]==who_played:
                count+=1
        else: count=0
        if count==4:
            return True
            break
        i+=1
        j+=1
        
    for i in range(0, r):
     j=0
     count=0
     while i<r and j<7:
        if board[i*7+j]==who_played:
                count+=1
        else: count=0
        if count==4:
            return True
            break
        i+=1
        j+=1
    
    for j in range(0, 7):
     i=0
     count=0
     while i<r and j>-1:
        if board[i*7+j]==who_played:
                count+=1
        else: count=0
        if count==4:
            return True
            break
        i+=1
        j-=1
    
    for i in range(0, r):
     j=6
     count=0
     while i<r and j>-1:
        if board[i*7+j]==who_played:
                count+=1
        else: count=0
        if count==4:
            return True
            break
        i+=1
        j-=1
    return False

def check_single_victory(board, who_played):
    r=int(len(board)/7)
    if check_column_victory(board, who_played) == True or check_row_victory(board, who_played) == True or check_diagonal_victory(board, who_played) == True:
        return True
    else: return False

def check_victory(board, who_played):
    r=int(len(board)/7)
    if check_single_victory(board, who_played)==True and check_single_victory(board, 3-who_played)==False:
        return who_played
    elif check_single_victory(board, who_played)==False and check_single_victory(board, 3-who_played)==True:
        return 3-who_played
    elif check_single_victory(board, who_played)==True and check_single_victory(board, 3-who_played)==True:
        return 3-who_played
    else: return 0

def display_board(board):
    r=int(len(board)/7)
    for i in range(r-1,-1,-1):
        l=[]
        for j in range(0,7,+1):
            l.append(board[i*7+j])
        print (l)

def check_available(board, i, j):
     if board[i*7+j]!=0: return False
     elif i==0: return True
     elif board[i*7-7+j]!=0: return True
     return False
 
def check_column_threat(board, j, opponent):
    r=int(len(board)/7)
    for i in range(0,r-3):           
      if check_available(board, i+3, j) and board[i*7+j]==opponent and board[i*7+7+j]==opponent and board[i*7+14+j]==opponent: return True
    return False

def check_row_threat(board, i, opponent):
    for k in range(0,5):
        if board[i*7+k]==opponent and board[i*7+k+1]==opponent and board[i*7+k+2]==opponent:
            if k==0: 
                if check_available(board, i, 3)==True: 
                    return 3
                    break
                else: pass
            elif k==4:
                if check_available(board, i, 3)==True:
                    return 3
                    break
            else: 
                if check_available(board, i, k-1): return k-1
                elif check_available(board, i, k+3): return k+3
    for k in range(0,4):
        if board[i*7+k]==opponent and check_available(board, i, k+1) and board[i*7+k+2]==opponent and board[i*7+k+3]==opponent:
            return k+1
        elif board[i*7+k]==opponent and board[i*7+k+1]==opponent and check_available(board, i, k+2) and board[i*7+k+3]==opponent:
            return k+2
    return -1

def check_left_row_diagonal_threat(board, j, opponent):
    r=int(len(board)/7)
    n=0
    k0=0
    l0=j
    while k0<r and l0<7:
        n+=1
        k0+=1
        l0+=1
    if n<4: return -1
    else: 
      for k in range(0, n-2):
          if k==0:
              if board[k*7+(k+j)]==opponent and board[k*7+7+(k+1+j)]==opponent and board[k*7+14+(k+2+j)]==opponent and check_available(board, k+3, k+3+j):
                  return k+3+j
          elif k==n-3: 
              if board[k*7+(k+j)]==opponent and board[k*7+7+(k+1+j)]==opponent and board[k*7+14+(k+2+j)]==opponent and check_available(board, k-1, k-1+j):
                  return k-1+j
          else: 
              if board[k*7+(k+j)]==opponent and board[k*7+7+(k+1+j)]==opponent and board[k*7+14+(k+2+j)]==opponent:
                  if check_available(board, k-1, k-1+j): return k-1+j
                  elif check_available(board, k+3, k+3+j): return k+3+j
      for k in range(0,n-3):
              if board[k*7+(k+j)]==opponent and board[k*7+7+(k+1+j)]==opponent and check_available(board, k+2, k+2+j) and board[k*7+21+(k+3+j)]==opponent:
                  return k+2+j
              elif board[k*7+(k+j)]==opponent and check_available(board, k+1, k+1+j) and board[k*7+14+(k+2+j)]==opponent and board[k*7+21+(k+3+j)]==opponent:
                  return k+1+j
    return -1

def check_left_column_diagonal_threat(board, i, opponent):
    r=int(len(board)/7)
    n=0
    k0=i
    l0=0
    while k0<r and l0<7:
        n+=1
        k0+=1
        l0+=1
    if n<4: return -1
    else: 
      for l in range(0, n-2):
          if l==0:
              if board[(i+l)*7+l]==opponent and board[(i+l+1)*7+(l+1)]==opponent and board[(i+l+2)*7+(l+2)]==opponent and check_available(board, i+l+3, l+3):
                  return l+3
          elif l==3: 
              if board[(i+l)*7+l]==opponent and board[(i+l+1)*7+(l+1)]==opponent and board[(i+l+2)*7+(l+2)]==opponent and check_available(board, i+l-1, l-1):
                  return l-1
          else: 
              if board[(i+l)*7+l]==opponent and board[(i+l+1)*7+(l+1)]==opponent and board[(i+l+2)*7+(l+2)]==opponent:
                  if check_available(board, i+l-1, l-1): return l-1
                  elif check_available(board, i+l+3, l+3): return l+3
      for l in range(0,n-3):
              if board[(i+l)*7+l]==opponent and board[(i+l+1)*7+(l+1)]==opponent and check_available(board, i+l+2, l+2) and board[(i+l+3)*7+(l+3)]==opponent:
                  return l+2
              elif board[(i+l)*7+l]==opponent and check_available(board, i+l+1, l+1) and board[(i+l+2)*7+(l+2)]==opponent and board[(i+l+3)*7+(l+3)]==opponent:
                  return l+1
    return -1

def check_right_row_diagonal_threat(board, j, opponent):
    r=int(len(board)/7)
    n=0
    k0=0
    l0=j
    while k0<r and l0>-1:
        n+=1
        k0+=1
        l0-=1
    if n<4: return -1
    else: 
      for k in range(0, n-2):
          if k==0:
              if board[k*7+(j-k)]==opponent and board[k*7+7+(j-k-1)]==opponent and board[k*7+14+(j-k-2)]==opponent and check_available(board, k+3, j-k-3):
                  return j-k-3
          elif k==n-3: 
              if board[k*7+(j-k)]==opponent and board[k*7+7+(j-k-1)]==opponent and board[k*7+14+(j-k-2)]==opponent and check_available(board, k-1, j-k+1):
                  return j-k+1
          else: 
              if board[k*7+(j-k)]==opponent and board[k*7+7+(j-k-1)]==opponent and board[k*7+14+(j-k-2)]==opponent:
                  if check_available(board, k-1, j-k+1): return j-k+1
                  elif check_available(board, k+3, j-k-3): return j-k-3
      for k in range(0,n-3):
              if board[k*7+(j-k)]==opponent and board[k*7+7+(j-k-1)]==opponent and check_available(board, k+2, j-k-2) and board[k*7+21+(j-k-3)]==opponent:
                  return j-k-2
              elif board[k*7+(j-k)]==opponent and check_available(board, k+1, j-k-1) and board[k*7+14+(j-k-2)]==opponent and board[k*7+21+(j-k-3)]==opponent:
                  return j-k-1
    return -1

def check_right_column_diagonal_threat(board, i, opponent):
    r=int(len(board)/7)
    n=0
    k0=i
    l0=6
    while k0<r and l0>-1:
        n+=1
        k0+=1
        l0-=1
    if n<4: return -1
    else: 
      for l in range(n-1, 1):
          if l==n-1:
              if board[(i+6-l)*7+l]==opponent and board[(i+6-l+1)*7+(l-1)]==opponent and board[(i+6-l+2)*7+(l-2)]==opponent and check_available(board, i+6-l+3, l-3):
                  return l-3
          elif l==2: 
              if board[(i+6-l)*7+l]==opponent and board[(i+6-l+1)*7+(l-1)]==opponent and board[(i+6-l+2)*7+(l-2)]==opponent and check_available(board, i+6-l-1, l+1):
                  return l+1
          else: 
              if board[(i+6-l)*7+l]==opponent and board[(i+6-l+1)*7+(l-1)]==opponent and board[(i+6-l+2)*7+(l-2)]==opponent:
                  if check_available(board, i+6-l-1, l+1): return l+1
                  elif check_available(board, i+6-l+3, l-3): return l-3
      for l in range(n-1,2):
              if board[(i+6-l)*7+l]==opponent and board[(i+6-l+1)*7+(l-1)]==opponent and check_available(board, i+6-l+2, l-2) and board[(i+l+3)*7+(l+3)]==opponent:
                  return l-2
              elif board[(i+6-l)*7+l]==opponent and check_available(board, i+6-l+1, l-1) and board[(i+6-l+2)*7+(l-2)]==opponent and board[(i+l+3)*7+(l+3)]==opponent:
                  return l-1
    return -1

def check_threat(board, opponent):
    r=int(len(board)/7)
    for m in range(0,7):
        if check_column_threat(board, m , opponent)==True:
            return m
    for m in range(0,r):
        if check_row_threat(board, m, opponent)!=-1:
            return check_row_threat(board, m, opponent)
    for m in range(0,r):
        if check_left_column_diagonal_threat(board, m, opponent)!=-1 : 
            return check_left_column_diagonal_threat(board, m, opponent)
        elif check_right_column_diagonal_threat(board, m, opponent)!=-1:
            return check_right_column_diagonal_threat(board, m, opponent)
    for m in range(0,7):
        if check_left_row_diagonal_threat(board, m, opponent)!=-1 : 
            return check_left_row_diagonal_threat(board, m, opponent)
        elif check_right_row_diagonal_threat(board, m, opponent)!=-1:
            return check_right_row_diagonal_threat(board, m, opponent)
    return -1    

def computer_move(board, turn, level):
    if level==1:
        check=False
        while check==False:
          col=random.randint(0, 7)
          pop=random.randint(0, 2)
          check=check_move(board, turn, col, pop)
        return col, pop
    elif level==2:
        if check_threat(board, turn)==-1:
          if check_threat(board, 3-turn)==-1:
           check=False 
           while check==False:
             col=random.randint(0, 7)
             pop=random.randint(0, 2)
             check=check_move(board, turn, col, pop)
             if check==True:                            
                if check_threat(apply_move(board, turn, col, pop), 3-turn)!=-1 or check_victory(board, 3-turn)==3-turn:
                    check=False
           return col, pop
          else:                                                                      
             return check_threat(board, 3-turn), 0            
        else: 
             return check_threat(board, turn), 0
                    
        
def menu():    
    r=0
    turn=1
    print("WELCOME MY FRIEND")
    print("THIS IS THE MENU")
    Human_Computer=2
    while r<6 or r>20: 
        r=int(input("Type in the number of rows ranging from 6 to 20: "))
        if r<=5 or r>=21: print("Invalid input - Type in the number of rows ranging from 6 to 20")
        
    while Human_Computer!=0 and Human_Computer!=1:
      Human_Computer=int(input("Type number '0' for Human or type number '1' for Computer: "))
      if Human_Computer!=0 and Human_Computer!=1: print("Invalid input - Type number '0' for another player or type number '1' for a computer")
    if Human_Computer == 1:
        Diff=10
        Role=10
        while Diff!=1 and Diff!=2:
          Diff=int(input("Type number '1' for Easy computer or Type number '2' for Medium computer: "))
          if Diff!=1 and Diff!=2: print("Invalid input - Type number '1' for easy computer or type number '2' for medium computer")
        while Role!=1 and Role!=2:
          Role=int(input("Type number '1' to go 1st or type number '2' to go 2nd: "))
          if Role!=1 and Role!=2: print("Invalid input - Type number '1' to go 1st or type number '2' to go 2nd")
        board=[]
        for i in range(0, 7*r):
            board.append(0)
        display_board(board)
        turn = 2
        while check_victory(board, turn)==0:
                  turn=3-turn 
                  if Role==turn:
                    check=False
                    while check==False:
                        print("It's your turn.")
                        col=int(input("Column - Type number '0' (furthest Left),'1', '2', '3', '4', '5' or '6' (furthest right): "))
                        pop=int(input("Type '0' to hit or type '1' to pop: "))
                        check=check_move(board, turn, col, pop)
                        if check==False: print("Invalid move - Column: Type number '0', '1', '2', '3', '4', '5' and '6' and Press number '0' to hit and number '1' to pop")
                    board=apply_move(board, turn, col, pop).copy()
                    print("This is your move: ")
                    display_board(board)
                  else: 
                    col=computer_move(board, turn, Diff)[0]
                    pop=computer_move(board, turn, Diff)[1]
                    
                    board=apply_move(board, turn, col, pop).copy()
                    print("It's computer's turn now: ")   
                    display_board(board)
                        
        else: 
                     if Role==check_victory(board, turn):
                       print("You win")
                     else: print("Computer wins")    
                     
         
    else: 
        board=[]
        for i in range(0, 7*r):
          board.append(0)
        display_board(board)
        turn=2
        while check_victory(board, turn)==0:
          turn=3-turn
          check=False
          while check==False:
            print("It's your turn.")
            col=int(input("Column - Type number '0' (furthest Left),'1', '2', '3', '4', '5' or '6' (furthest right): "))
            pop=int(input("Type '0' to hit or type '1' to pop: "))
            check=check_move(board, turn, col, pop)
            if check==False: print("Invalid move - Column: Type number '0', '1', '2', '3', '4', '5' and '6' and Press number '0' to hit and number '1' to pop")
          board=apply_move(board, turn, col, pop).copy()
          display_board(board)   

        else: print("Player", check_victory(board, turn), "wins")
            
menu()
