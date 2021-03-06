#Imported built-in modules
import sys
import os
#Imported writed modules
import board
#Import random choose bot
import randomBot
#Import database
import db

#initialize variables
array = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
turn = [1]
player1 = " "
player2 = " "
gamemode = [0]
wins = [0, 0]
ties = [0]
fieldsTaken = [0]
gamesLeft = [1001]

#Display board
def showBoard(p1, p2):
    os.system("clear")
    table = board.Draw(array, p1, p2)
    table.show()

#Choose gamemode based on input
def gameMode():
    print("1 - Player vs Player")
    print("2 - Player vs Bot")
    print("3 - Bot vs Bot")
    x = input("Choose your gamemode: ")
    if((x == "1") or (x == "2") or (x == "3")):
        x = int(x)
        if(x == 1):
            gamemode[0] = 1
        elif(x == 2):
            gamemode[0] = 2
        elif(x == 3):
            gamemode[0] = 3
    else:
        print("Please insert a vaild gamemode!")
        gameMode()

gameMode()

#Start game between two players
def startGame():
    p1 = input("Player 1, give me your nickname: ")
    p2 = input("Player 2, give me your nicname: ")
    print()
    showBoard(p1, p2)
    print("That's " + p1 + " turn")
    return p1, p2

#Start game between player and a bot
def startPGame():
    p1 = input("Player 1, give me your nickname: ")
    p2 = "Bot"
    print()
    showBoard(p1, p2)
    print("That's " + p1 + " turn")
    return p1, p2

#Start game between two bots
def startBotGame():
    howManyGames = input("How many games you want to play?")
    gamesLeft[0] = int(howManyGames) - 1
    p1 = "Bot 1"
    p2 = "Bot 2"
    print()
    showBoard(p1, p2)
    print("That's " + p1 + " turn")
    return p1, p2


#Assign player nicknames to variables
if(gamemode[0] == 1):
    result = startGame()
    for i in result:
        player1 = result[0]
        player2 = result[1]
elif(gamemode[0] == 2):
    result = startPGame()
    for i in result:
        player1 = result[0]
        player2 = result[1]
elif(gamemode[0] == 3):
    result = startBotGame()
    for i in result:
        player1 = result[0]
        player2 = result[1]

#Reset game
def resetGame(p1, p2):
    for i in range(len(array)):
        array[i] = " "
    fieldsTaken[0] = 0
    showBoard(p1, p2)

#Show messages after someone win and take decision input
def gameOver():
    if(gamemode[0] == 1):
        answer = input("Do you wanna play again? [Yes/No]")
        if(answer == "Yes"):
           resetGame(player1, player2)
        elif(answer == "No"):
            sys.exit()
        else:
            print("Give right answer")
            gameOver()
    elif(gamemode[0] == 2):
        answer = input("Do you wanna play again? [Yes/No]")
        if(answer == "Yes"):
           resetGame(player1, player2)
        elif(answer == "No"):
            sys.exit()
        else:
            print("Give right answer")
            gameOver()
    elif(gamemode[0] == 3):
        if(turn[0] % 2 == 0):
           wins[0] += 1
        elif(turn[0] % 2 == 1):
           wins[1] += 1
        if(gamesLeft[0] > 0):
            resetGame(player1, player2)
            gamesLeft[0] -= 1
        elif(gamesLeft[0] == 0):
            print("Bot 1 wins: " + str(wins[0]))
            print("Bot 2 wins: " + str(wins[1]))
            print("Ties: " + str(ties[0]))
            sys.exit()

#Function to be called when game ends with a tie
def tie():
    ties[0] += 1
    player1InDB = db.checkPlayer(player1)
    player2InDB = db.checkPlayer(player2)
    if(player1InDB == True and player2InDB == True):
        db.updatePlayer(player1, "Tie")
        db.updatePlayer(player2, "Tie")
    elif(player1InDB == True and player2InDB == False):
            db.updatePlayer(player2, "Tie")
            db.addNewPlayer(player1, 0, 0, 1)
    elif(player1InDB == False and player2InDB == True):
        db.updatePlayer(player1, "Tie")
        db.addNewPlayer(player2, 0, 0, 1)
    elif(player1InDB == False and player2InDB == False):
            db.addNewPlayer(player2, 0, 0, 1)
            db.addNewPlayer(player1, 0, 0, 1)

    if(gamemode[0] == 1):
        print("Tie")

        answer = input("Do you wanna play again? [Yes/No]")
        if(answer == "Yes"):
           resetGame(player1, player2)
        elif(answer == "No"):
            sys.exit()
        else:
            print("Give right answer")
            gameOver()
    elif(gamemode[0] == 2):
        print("Tie")
        answer = input("Do you wanna play again? [Yes/No]")
        if(answer == "Yes"):
           resetGame(player1, player2)
        elif(answer == "No"):
            sys.exit()
        else:
            print("Give right answer")
            gameOver()
    elif(gamemode[0] == 3):
        resetGame(player1, player2)
        gamesLeft[0] -= 1

#Function to perform actions with database
def dbPlayer():
    if(turn[0] % 2 == 1):
            print(player2 + " won!")
            player1InDB = db.checkPlayer(player1)
            player2InDB = db.checkPlayer(player2)
            if(player1InDB == True and player2InDB == True):
                db.updatePlayer(player2, "Win")
                db.updatePlayer(player1, "Lose")
            elif(player1InDB == True and player2InDB == False):
                db.updatePlayer(player1, "Lose")
                db.addNewPlayer(player2, 1, 0, 0)
            elif(player1InDB == False and player2InDB == True):
                db.updatePlayer(player2, "Win")
                db.addNewPlayer(player1, 0, 1, 0)
            elif(player1InDB == False and player2InDB == False):
                db.addNewPlayer(player1, 0, 1, 0)
                db.addNewPlayer(player2, 1, 0, 0)

    elif(turn[0] % 2 == 0):
        print(player1 + " won!")
        player1InDB = db.checkPlayer(player1)
        player2InDB = db.checkPlayer(player2)
        if(player1InDB == True and player2InDB == True):
            db.updatePlayer(player1, "Win")
            db.updatePlayer(player2, "Lose")
        elif(player1InDB == True and player2InDB == False):
            db.updatePlayer(player1, "Win")
            db.addNewPlayer(player2, 0, 1, 0)
        elif(player1InDB == False and player2InDB == True):
            db.updatePlayer(player2, "Lose")
            db.addNewPlayer(player1, 1, 0, 0)
        elif(player1InDB == False and player2InDB == False):
            db.addNewPlayer(player2, 0, 1, 0)
            db.addNewPlayer(player1, 1, 0, 0)


#Check if coordinates are valid and translates X, Y coordinates to array index
def whichField(coordX, coordY):
    if(((coordX != "1") and (coordX != "2") and (coordX != "3")) or ((coordY != "1") and (coordY != "2") and (coordY != "3"))):
        print("Please give a valid coordinate")
    else:
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
    #Horizontal lines win
    if(array[0] == "X" and array[1] == "X" and array[2] == "X") or (array[0] == "O" and array[1] == "O" and array[2] == "O"):
        dbPlayer()
        gameOver()

    elif(array[3] == "X" and array[4] == "X" and array[5] == "X") or (array[3] == "O" and array[4] == "O" and array[5] == "O"):
        dbPlayer()
        gameOver()

    elif(array[6] == "X" and array[7] == "X" and array[8] == "X") or (array[6] == "O" and array[7] == "O" and array[8] == "O"):
        dbPlayer()
        gameOver()

    #Vertical lines win
    elif(array[0] == "X" and array[3] == "X" and array[6] == "X") or (array[0] == "O" and array[3] == "O" and array[6] == "O"):
        dbPlayer()
        gameOver()

    elif(array[1] == "X" and array[4] == "X" and array[7] == "X") or (array[1] == "O" and array[4] == "O" and array[7] == "O"):
        dbPlayer()
        gameOver()

    elif(array[2] == "X" and array[5] == "X" and array[8] == "X") or (array[0] == "O" and array[1] == "O" and array[2] == "O"):
        dbPlayer()
        gameOver()

    #Cross lines win
    elif(array[0] == "X" and array[4] == "X" and array[8] == "X") or (array[0] == "O" and array[4] == "O" and array[8] == "O"):
        dbPlayer()
        gameOver()

    elif(array[2] == "X" and array[4] == "X" and array[6] == "X") or (array[2] == "O" and array[4] == "O" and array[6] == "O"):
        dbPlayer()
        gameOver()

    elif(fieldsTaken[0] == 9):
        tie()


#Write player mark into board, show updated board, and check if anyone won
#Main player vs player game function

#User input fixed, playerInput fixed, 
def userInput(p1, p2):
    if(turn[0] % 2 == 1):
        mark = "X"
        print()
        fieldX = input("Give row number: ")
        fieldY = input("Give column number: ")
        field = whichField(fieldX, fieldY)
        if(type(field) == int):
            if(array[field] != " "):
                print("This field is already used")
            else:
                array[field] = mark
                turn[0] += 1
                showBoard(p1, p2)
                fieldsTaken[0] += 1
                winConditions()
                print("That's " + p2 + " turn")
        
    elif(turn[0] % 2 == 0):
        mark = "O"
        print()
        fieldX = input("Give row number: ")
        fieldY = input("Give column number: ")
        field = whichField(fieldX, fieldY)
        if(type(field) == int):
            if(array[field] != " "):
                print("This field is already used")
            else:
                array[field] = mark
                turn[0] += 1
                showBoard(player1, player2)
                fieldsTaken[0] += 1
                winConditions()
                print("That's " + p1 + " turn")

#Main player vs bot function
def playerInput(p1, p2):
    if(turn[0] % 2 == 1):
        mark = "X"
        print()
        fieldX = input("Give row number: ")
        fieldY = input("Give column number: ")
        field = whichField(fieldX, fieldY)
        if(type(field) == int):
            if(array[field] != " "):
                print("This field is already used")
            else:
                array[field] = mark
                turn[0] += 1
                showBoard(player1, player2)
                fieldsTaken[0] += 1
                winConditions()
                print("That's " + p2 + " turn")
        
    elif(turn[0] % 2 == 0):
        mark = "O"
        print()
        correct = randomBot.botInput(array, mark)
        if(correct == False):
            print("Try again")
        elif(correct == True):
            turn[0] += 1
            showBoard(player1, player2)
            fieldsTaken[0] += 1
            winConditions()
            print("That's " + p1 + " turn")

#Main Bot vs Bot function
def botInput(p1, p2):
    if(turn[0] % 2 == 1):
        mark = "X"
        print()
        correct = randomBot.botInput(array, mark)
        if(correct == False):
            print("Try again")
        elif(correct == True):
            turn[0] += 1
            showBoard(player1, player2)
            fieldsTaken[0] += 1
            winConditions()
            print("That's " + p2 + " turn")
    elif(turn[0] % 2 == 0):
        mark = "O"
        print()
        correct = randomBot.botInput(array, mark)
        if(correct == False):
            print("Try again")
        elif(correct == True):
            turn[0] += 1
            showBoard(player1, player2)
            fieldsTaken[0] += 1
            winConditions()
            print("That's " + p1 + " turn")

#Run game until someone win
#Main game loop
while(True):
    if(gamemode[0] == 1):
        userInput(player1, player2)
    elif(gamemode[0] == 2):
        playerInput(player1, player2)
    elif(gamemode[0] == 3):
        botInput(player1, player2)