import board
array = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
turn = 1
player1 = " "
player2 = " "
win = False

#Function to display board
def showBoard(p1, p2):
    table = board.Draw(array, p1, p2)
    table.show()

#Function starting game
def startGame():
    p1 = input("Player 1, give me your nickname: ")#'Pablo' #
    p2 = input("Player 2, give me your nicname: ")#'Kamil' #
    print()
    showBoard(p1, p2)
    print("That's " + p1 + " turn")
    return p1, p2

#Assign player nicknames to variables
result = startGame()
for i in result:
    player1 = result[0]
    player2 = result[1]

#Translates X, Y coordinates to array index
def whichField(coordX, coordY):
    coordX = int(coordX)
    coordY = int(coordY)
    if(coordX == 1):
        if(coordY == 1):
            field = 0
        elif(coordY == 2):
            field = 1
        elif(coordY == 3):
            field = 2
    elif(coordX == 2):
        if(coordY == 1):
            field = 3
        elif(coordY == 2):
            field = 4
        elif(coordY == 3):
            field = 5
    elif(coordX == 3):
        if(coordY == 1):
            field = 6
        elif(coordY == 2):
            field = 7
        elif(coordY == 3):
            field = 8
    return field

#Check board to check if anyone won
def winConditions():
    #p1 = p1
    #p2 = p2
    #Horizontal lines win
    if(array[0] == "X" and array[1] == "X" and array[2] == "X") or (array[0] == "O" and array[1] == "O" and array[2] == "O"):
        print("Game Over")
    elif(array[3] == "X" and array[4] == "X" and array[5] == "X") or (array[3] == "O" and array[4] == "O" and array[5] == "O"):
        print("Game Over")
    elif(array[6] == "X" and array[7] == "X" and array[8] == "X") or (array[6] == "O" and array[7] == "O" and array[8] == "O"):
        print("Game Over")

    #Vertical lines win
    elif(array[0] == "X" and array[3] == "X" and array[6] == "X") or (array[0] == "O" and array[3] == "O" and array[6] == "O"):
        print("Game Over")
    elif(array[1] == "X" and array[4] == "X" and array[7] == "X") or (array[1] == "O" and array[4] == "O" and array[7] == "O"):
        print("Game Over")
    elif(array[2] == "X" and array[5] == "X" and array[8] == "X") or (array[0] == "O" and array[1] == "O" and array[2] == "O"):
        print("Game Over")

    #Cross lines win
    elif(array[0] == "X" and array[4] == "X" and array[8] == "X") or (array[0] == "O" and array[4] == "O" and array[8] == "O"):
        print("Game Over")
    elif(array[2] == "X" and array[4] == "X" and array[6] == "X") or (array[2] == "O" and array[4] == "O" and array[6] == "O"):
        print("Game Over")

#Write player mark into board, show updated board, and check if anyone won
def userInput(turn, p1, p2):
    p1 = p1
    p2 = p2
    if(turn % 2 == 1):
        mark = "X"
        print()
        fieldX = input("Give row number: ")
        fieldY = input("Give column number: ")
        field = whichField(fieldX, fieldY)
        if(array[field] != " "):
            print("This field is already used")
        else:
            array[field] = mark
            turn += 1
            showBoard(player1, player2)
            winConditions()
            print("That's " + p2 + " turn")
    elif(turn % 2 == 0):
        mark = "O"
        print()
        fieldX = input("Give row number: ")
        fieldY = input("Give column number: ")
        field = whichField(fieldX, fieldY)
        if(array[field] != " "):
            print("This field is already used")
        else:
            array[field] = mark
            turn += 1
            showBoard(player1, player2)
            winConditions()
            print("That's " + p1 + " turn")
    return turn

while(win != True):
    turn = userInput(turn, player1, player2)