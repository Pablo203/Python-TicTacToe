import mysql.connector
import os

os.system("sudo /opt/lampp/./xampp start")


mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "TicTacToe"
)

def checkPlayer(player):
    mycursor = mydb.cursor()
    query = "SELECT Username FROM Users WHERE Username = %s"
    mycursor.execute(query , (player,))
    for x in mycursor:
        if mycursor(x) == player:
            return True
    return False

def addNewPlayer(player, win, lose, tie):
    player = player
    win = win
    lose = lose
    tie = tie
    mycursor = mydb.cursor()
    query = "INSERT INTO Users (Username, Wins, Loses, Ties) VALUES (%s, %s, %s, %s)"
    mycursor.execute(query, (player, win, lose, tie))

def updatePlayer(player, result):
    player = player
    result = result
    mycursor = mydb.cursor()
    query = "SELECT Wins, Loses, Ties FROM Users WHERE Username = %s"
    mycursor.execute(query , (player))
    for x in mycursor:
        wins = mycursor[0]
        loses = mycursor[1]
        ties = mycursor[2]
    if(result == "Win"):
        wins += 1
    elif(result == "Lose"):
        loses += 1
    elif(result == "Tie"):
        ties += 1
    query = "UPDATE Users SET Wins = %s, Loses = %s, Ties = %s WHERE Username = %s"
    mycursor.execute(query , (wins, loses, ties, player))