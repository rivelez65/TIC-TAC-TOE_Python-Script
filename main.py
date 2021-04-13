# SETUP GAME 3x3 MATRIX
row_1 = ["___", "___", "___"]
row_2 = ["___", "___", "___"]
row_3 = ["___", "___", "___"]

# NEST ROW LISTS
matrix = [row_1, row_2, row_3]

# COLUMN DICTIONARY WILL RETURN AN INDEX NUMBER FOR THE GIVEN LETTER
columns = {
    'A': 0,
    'B': 1,
    'C': 2,
}

# BLANK VARIABLES
position = ''
occupied_positions = []

# INTRODUCTION
# PRINT GAME OBJECTIVE AND INSTRUCTIONS:
print(f'Welcome to python script TIC TAC TOE\n\n'
      f'OBJECTIVE: Whoever manages to align 3 " X " or " O " in the 3X3 gird is declared the winner.\n\n'
      f'INSTRUCTIONS: You will be placing an " X " or an " O " by typing the coordinates for the given \nrows:(1,2,3)'
      f' then the Given columns:(A,B,C)  \nfor example:("1A" for top left corner)\n'
      f'Lets Begin!!!\n')
# DISPLAY BLANK GAME
print(f'      A      B      C\n1  {row_1}\n2  {row_2}\n3  {row_3}\n')


# PLAYER 1 INPUT
def player1_turn():
    global occupied_positions, position
    # ASK PLAYER_1 TO GIVE COORDINATES
    position = input('Player 1 place your " X " (type your coordinates): ').upper()
    if position in occupied_positions:
        print('\n*****That position is already occupied, please pick another\n')
        player1_turn()
    else:
        try:
            # REPLACE SPECIFIC POSITION WITH 'X'
            row = int(position[0]) - 1
            column = columns[position[1]]
            matrix[row][column] = ' X '
            # DISPLAY UPDATE
            print(f'      A      B      C\n1  {row_1}\n2  {row_2}\n3  {row_3}\n')
            # UPDATE OCCUPIED POSITIONS
            occupied_positions.append(position)
        except IndexError:
            print("That position does not exist, pick '1' or '2' or '3' for row and 'A' or 'B' or 'C' for column")
            player1_turn()
        except KeyError:
            print("That position does not exist, pick '1' or '2' or '3' for row and 'A' or 'B' or 'C' for column")
            player1_turn()
        except ValueError:
            print("That position does not exist, pick '1' or '2' or '3' for row and 'A' or 'B' or 'C' for column")
            player1_turn()


def player2_turn():
    global occupied_positions, position
    # ASK PLAYER_2 TO GIVE COORDINATES
    position = input('Player 2 place your " O " (type your coordinates): ').upper()
    if position in occupied_positions:
        print('\n*****That position is already occupied, please pick another\n')
        player2_turn()
    else:
        try:
            # REPLACE SPECIFIC POSITION WITH 'X'
            row = int(position[0]) - 1
            column = columns[position[1]]
            matrix[row][column] = ' O '
            # DISPLAY UPDATE
            print(f'      A      B      C\n1  {row_1}\n2  {row_2}\n3  {row_3}\n')
            # UPDATE OCCUPIED POSITIONS
            occupied_positions.append(position)
        except IndexError:
            print("That position does not exist, pick '1' or '2' or '3' for row and 'A' or 'B' or 'C' for column")
            player2_turn()
        except KeyError:
            print("That position does not exist, pick '1' or '2' or '3' for row and 'A' or 'B' or 'C' for column")
            player2_turn()
        except ValueError:
            print("That position does not exist, pick '1' or '2' or '3' for row and 'A' or 'B' or 'C' for column")
            player2_turn()


# GAME LOGIC STRUCTURE
game_on = True
while game_on:

    player1_turn()

    # CHECK IF THERE ARE 3 'X' ALIGNED AND END GAME IF TRUE
    if row_1[0] == " X " and row_1[1] == " X " and row_1[2] == " X " \
            or row_2[0] == " X " and row_2[1] == " X " and row_2[2] == " X " \
            or row_3[0] == " X " and row_3[1] == " X " and row_3[2] == " X " \
            or row_1[0] == " X " and row_2[0] == " X " and row_3[0] == " X " \
            or row_1[1] == " X " and row_2[1] == " X " and row_3[1] == " X " \
            or row_1[2] == " X " and row_2[2] == " X " and row_3[2] == " X " \
            or row_1[0] == " X " and row_2[1] == " X " and row_3[2] == " X " \
            or row_1[2] == " X " and row_2[1] == " X " and row_3[0] == " X ":
        print("\n\n ****** PLAYER 1 WINS !!!!!!!!****** \n\n")
        game_on = False

    player2_turn()

    # CHECK IF THERE ARE 3 'O' ALIGNED AND END GAME IF TRUE
    if row_1[0] == " O " and row_1[1] == " O " and row_1[2] == " O " \
            or row_2[0] == " O " and row_2[1] == " O " and row_2[2] == " O " \
            or row_3[0] == " O " and row_3[1] == " O " and row_3[2] == " O " \
            or row_1[0] == " O " and row_2[0] == " O " and row_3[0] == " O " \
            or row_1[1] == " O " and row_2[1] == " O " and row_3[1] == " O " \
            or row_1[2] == " O " and row_2[2] == " O " and row_3[2] == " O " \
            or row_1[0] == " O " and row_2[1] == " O " and row_3[2] == " O " \
            or row_1[2] == " O " and row_2[1] == " O " and row_3[0] == " O ":
        print("\n\n ****** PLAYER 2 WINS!!!!!****** \n\n")
        game_on = False