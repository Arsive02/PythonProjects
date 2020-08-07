#!/usr/bin/env python
# coding: utf-8

#Creating the Board

def Board(board):
    print('-------------------------------')
    print('|    '+board[1]+'    |    '+board[2]+'    |    '+board[3]+'    |')
    print('-------------------------------')
    print('|    '+board[4]+'    |    '+board[5]+'    |    '+board[6]+'    |')
    print('-------------------------------')
    print('|    '+board[7]+'    |    '+board[8]+'    |    '+board[9]+'    |')
    print('-------------------------------')

#Getting the Username of the players

def username(user1,user2):
    player_1 = input("Player1,Enter your name : ").strip()
    print(f'\nWelcome to the game {player_1}!')
    player_2 = input("\nPlayer2,Enter your name : ").strip()
    print(f'\nWelcome to the game {player_2}!')
    return (player_1,player_2)

#Getting player1 choice

def player1_Selection(user1,user2):
    print(f'\n{user1}, Do you want "X" or "O?\n\n(press "x" or "o")\n')
    while(1):
        user_input = input().strip().lower()
        if user_input != 'x' and user_input != 'o':
            print('\nPlease select "X" or "O"')
        if user_input == 'x' or user_input == 'o':
            print(f'\n{user1}, you have selected "{user_input}"')
            break
    return user_input

#Visualing the board after getting the input from player1

def game_player1():
    print(f'\n{user1}, select a number from 1 to 9 : ')
    while(True):
        try:
            player1_position = int(input())
            if player1_position not in range(1,10):
                print('\nPlease select a number from 1 to 9')
            else:
                if selection == 'x':
                    if board[player1_position] =='X' or board[player1_position] == 'O':
                        print(f'\nSorry {user1}, this place is already occupied by -->  {board[player1_position]}')
                        print('\nKindly Select another place')
                    else:
                        board[player1_position] = 'X'
                        break
                else:
                    if board[player1_position] !='X' and board[player1_position] != 'O':
                        board[player1_position] = 'O'
                        break
                    else:
                        print(f'\nSorry {user1}, this place is already occupied by -->  {board[player1_position]}')
                        print('\nKindly Select another place')
        except:
            print('\nPlease select a number from 1 to 9')

#Visualing the board after getting the input from player2

def game_player2():
    print(f'\n{user2}, select a number from 1 to 9 : ')
    while(True):
        try:
            player2_position = int(input())
            if player2_position not in range(1,10):
                print('\nPlease select a number from 1 to 9')
            else:
                if selection == 'x':
                    if board[player2_position] =='X' or board[player2_position] == 'O':
                        print(f'\nSorry {user2}, this place is already occupied by -->  {board[player2_position]}')
                        print('\nKindly Select another place')
                    else:
                        board[player2_position] = 'O'
                        break
                else:
                    if board[player2_position] !='X' and board[player2_position] != 'O':
                        board[player2_position] = 'X'
                        break
                    else:
                        print(f'\nSorry {user2}, this place is already occupied by -->  {board[player2_position]}')
                        print('\nKindly Select another place')
        except:
            print('\nPlease select a number from 1 to 9')

#Defining the Victory Rule

def Victory():
    if board[1:4]==['X','X','X'] or board[4:7]==['X','X','X'] or board[6:10]==['X','X','X'] :
        return 'X'
    elif board[1:4]==['O','O','O'] or board[4:7]==['O','O','O'] or board[6:10]==['O','O','O'] :
        return 'O'
    elif (board[1]=='X' and board[4]=='X' and board[7]=='X') or (board[2]=='X' and board[5]=='X' and board[8]=='X') or (board[3]=='X' and board[6]=='X' and board[9]=='X'):
        return 'X'
    elif (board[1]=='O' and board[4]=='O' and board[7]=='O') or (board[2]=='O' and board[5]=='O' and board[8]=='O') or (board[3]=='O' and board[6]=='O' and board[9]=='O'):
        return 'O'
    elif (board[1]=='X' and board[5]=='X' and board[9]=='X') or (board[3]=='X' and board[5]=='X' and board[7]=='X'):
        return 'X'
    elif (board[1]=='O' and board[5]=='O' and board[9]=='O') or (board[3]=='O' and board[5]=='O' and board[7]=='O'):
        return 'O'
    else:
        if sorted(set(board[1:10])) == ['O','X']:
            Tie = "Ooops, It's a Tie!, Well played"
            return Tie
        else:
            return False

from IPython.display import clear_output

# Collecting all the functions and forming the game flow
def Game():
    while(Victory() == False):
        if selection =='x':
            game_player1()
        else:
            game_player2()

        Board(board)
        if Victory()!="Ooops, It's a Tie!, Well played":
            if selection == 'x':
                if Victory() == 'X':
                    print(f'\nCongratulations {user1}! YOU WON!')
                    break
                elif Victory() == 'O':
                    print(f'\nCongratulations {user2}! YOU WON!')
                    break
                else:
                    pass
            if selection == 'o':
                if Victory() == 'O':
                    print(f'\nCongratulations {user1}! YOU WON!')
                    break
                elif Victory() == 'X':
                    print(f'\nCongratulations {user2}! YOU WON!')
                    break
                else:
                    pass
        else:
            print(f'{Victory()}, Well played {user1},{user2}')
            break

        if selection=='o':
            game_player1()
        else:
            game_player2()

        Board(board)
        if Victory()!="Ooops, It's a Tie!, Well played":
            if selection == 'x':
                if Victory() == 'X':
                    print(f'\nCongratulations {user1}! YOU WON!')
                    break
                elif Victory() == 'O':
                    print(f'\nCongratulations {user2}! YOU WON!')
                    break
                else:
                    pass
            if selection == 'o':
                if Victory() == 'O':
                    print(f'\nCongratulations {user1}! YOU WON!')
                    break
                elif Victory() == 'X':
                    print(f'\nCongratulations {user2}! YOU WON!')
                    break
                else:
                    pass
        else:
            print(f'{Victory()}, {user1} and {user2}')
            break

#Initializing the Key to "Yes"
key='Y'

while(key=='Y'):
    #Defining the board
    board= [' ']*10

    #Visualizing the Board
    Board(board)

    #Getting the username from player1 and player2
    user1,user2=username(user1='',user2='')

    #Getting the Selection from player1
    selection =player1_Selection(user1,user2)
    Game()
    print('\n Do you wish to play again? Press (Y/N)')
    key = input().strip()
    while(1):
        if key !='Y' or key !='N':
            print('\nPlease select Y or N')
            break
    clear_output()
