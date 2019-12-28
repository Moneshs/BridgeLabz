#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:17:24 2019

@author: Moneshs
"""
from math import inf as infinity

#creating a empty board 
game_state=[[' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']]
#defining a function for playing a move
def play_move(state,player,block_num):
    #using condition statements where the move can be placed or not
    if state[int((block_num-1)/3)][(block_num-1)%3] is ' ':
        state[int((block_num-1)/3)][(block_num-1)%3]=player
    #else place the move again where the board is empty
    else:
        block_num=int(input("its not empty,choose different move:"))
        play_move(state,player,block_num)

#defining a function for coping a gameboard for each time plays
def copy_game_state(state):
    #creating a empty array to store
    new_state=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    for i in range(3):
        for j in range(3):
            new_state[i][j]=state[i][j]
    return new_state

#defining a function to check the current state of board
def check_current_state(game_state):
    draw_flag=0
    for i in range(3):
        for j in range(3):
            if game_state[i][j]is ' ':
                draw_flag=1
    if draw_flag is 0:
        return None ,"draw"

    # Checking horizontals of a board
    if (game_state[0][0] == game_state[0][1] and game_state[0][1] == game_state[0][2] and game_state[0][0] is not ' '):
        return game_state[0][0], "Done"
    if (game_state[1][0] == game_state[1][1] and game_state[1][1] == game_state[1][2] and game_state[1][0] is not ' '):
        return game_state[1][0], "Done"
    if (game_state[2][0] == game_state[2][1] and game_state[2][1] == game_state[2][2] and game_state[2][0] is not ' '):
        return game_state[2][0], "Done"
    
    # Checking verticals of a board
    if (game_state[0][0] == game_state[1][0] and game_state[1][0] == game_state[2][0] and game_state[0][0] is not ' '):
        return game_state[0][0], "Done"
    if (game_state[0][1] == game_state[1][1] and game_state[1][1] == game_state[2][1] and game_state[0][1] is not ' '):
        return game_state[0][1], "Done"
    if (game_state[0][2] == game_state[1][2] and game_state[1][2] == game_state[2][2] and game_state[0][2] is not ' '):
        return game_state[0][2], "Done"
    
    # Checking  diagonals of a board
    if (game_state[0][0] == game_state[1][1] and game_state[1][1] == game_state[2][2] and game_state[0][0] is not ' '):
        return game_state[1][1], "Done"
    if (game_state[2][0] == game_state[1][1] and game_state[1][1] == game_state[0][2] and game_state[2][0] is not ' '):
        return game_state[1][1], "Done"
    
    #returning if non of the cases true
    return None, "Not Done"

#Printing the board 3X3
def print_board(game_state):
    print('-----------------')
    print('|'+str(game_state[0][0])+'||'+str(game_state[0][1])+'||'+str(game_state[0][2])+'|')
    print('-----------------')
    print('|'+str(game_state[1][0])+'||'+str(game_state[1][1])+'||'+str(game_state[1][2])+'|')
    print('-----------------')
    print('|'+str(game_state[2][0])+'||'+str(game_state[2][1])+'||'+str(game_state[2][2])+'|')
    print('-----------------')

#defining a function for getbesrmove in the board
def getbestmove(state,player):
    #Minmax Algorithm
    #calling a function to check_current_state board
    winner_loser,done=check_current_state(state)
    #using condition statement and returns AI or human won
    if done=="Done" and winner_loser=='O':
        return 1
    elif done=="Done" and winner_loser=='X':
        return -1
    elif done=="Draw":
        return 0
    
    #initializing a two empty list
    moves=[]
    empty_cells=[]
    #using looping condtion to check the state for where the move is unplaced
    for i in range(3):
        for j in range(3):
            #checking where the board has empty spaces
            if state[i][j] is ' ':
                #appending the empty places into the list
                empty_cells.append(i*3+(j+1))
    
    #using looping conditions and storing empty_places moves in to dictionary
    for empty_cell in empty_cells:
        #creating a empty dictionary
        move={}
        move['index']=empty_cell
        #calling a copy_game_state function
        new_state=copy_game_state(state)
        #calling a fucntion to play a move
        play_move(new_state,player,empty_cell)
    
    #human turn
    if player=='X':
        #making more depth tree for human
        result=getbestmove(new_state,'X')
        move['score']=result
    elif player=='O':
        #making more depth tree for Ai
        result=getbestmove(new_state,'O')
        move['score']=result
    #appending the move into list
    moves.append(move)

    #finding a best move
    best_move=None
    if player=='O':
        best=-infinity
        for move in moves:
            if move['score']>best:
                best=move['score']
                best_move=move['index']
    else:
        for move in moves:
            if move['score']<best:
                best=move['score']
                best_move=move['index']

    return best_move
