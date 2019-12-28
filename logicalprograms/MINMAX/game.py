#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 2:17:24 2019

@author: Moneshs
"""
#importing functions from the different file
from utility import print_board,check_current_state,getbestmove,play_move\
#assigning the players role
players=['X','O']
#Started playing
play_again='Y'
while play_again=='Y' or play_again=='y':
    #creating a empty array for storing inputs
    game_state=[[' ',' ',' '],
                [' ',' ',' '],
                [' ',' ',' ']]
    current_state="Not Done"
    print_board(game_state)
    #choose human or Ai starts
    player_choice=input("choose X for human or O for Ai:")
    Winner=None  

    #using condition statements according to input of Player choice's
    if player_choice=='X' or player_choice=='x':
        current_player_idx=0
    else:
        current_player_idx=1

    #using looping statments till current_state is Done 
    while current_state=="Not Done":
        #using condition statments for placing the move for human and Ai
        if current_player_idx==0:
            block_choice=int(input("enter the move:"))
            #calling a function to play a move
            play_move(game_state,players[current_player_idx],block_choice)
        else:
            #calling a function to get a best move for AI
            block_choice=getbestmove(game_state,players[current_player_idx])
            #calling a function to play a move
            play_move(game_state,players[current_player_idx],block_choice)

        #calling a function to print the board
        print_board(game_state)
        #calling a function to check the board
        winner,current_state=check_current_state(game_state)
        #using condition statement for checking the winner of the game
        if winner is not None:
            print(str(winner)+"won")
        else:
            current_player_idx=(current_player_idx+1)%2
        #checking the current_state is draw or not
        if current_state is "draw":
            print("Draw")