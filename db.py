import pymysql
import os

os.system("sudo /opt/lampp/./xampp start")


mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "TicTacToe"
)

#Function to check if player already exist in database
def checkPlayer(player):
    mycursor = mydb.cursor()
    query = "SELECT Username FROM Users WHERE Username = %s"
    mycursor.execute(query , (player))
    result = mycursor.fetchone()
    print(player)
    if(result == None):
        print("False")
        return False
    else:
        print("True")
        return True
    '''for x in result:
        if(x == player):
            return True
        else:
            return False'''

#Function to add new player to database with his current statistics
def addNewPlayer(player, win, lose, tie):
    player = player
    win = win
    lose = lose
    tie = tie
    mycursor = mydb.cursor()
    query = "INSERT INTO Users (Username, Wins, Loses, Ties) VALUES (%s, %s, %s, %s)"
    mycursor.execute(query, (player, win, lose, tie))
    mydb.commit()

#Function to update player data in database. Updates statistics based on username
def updatePlayer(player, results):
    help = 0
    print(player)
    values = {
        "wins" : 0,
        "loses" : 0,
        "ties" : 0
    }
    mycursor = mydb.cursor()
    query = "SELECT Wins, Loses, Ties FROM Users WHERE Username = %s"
    mycursor.execute(query , (player))
    result = mycursor.fetchone()
    for x in result:
        if(help == 0):
            values["wins"] = x
        elif(help == 1):
            values["loses"] = x
        elif(help == 2):
            values["ties"] = x
        help += 1
    if(results == "Win"):
        values["wins"] += 1
    elif(results == "Lose"):
        values["loses"] += 1
    elif(results == "Tie"):
        values["ties"] += 1
    wins = values["wins"]
    loses = values["loses"]
    ties = values["ties"]
    query = "UPDATE Users SET Wins = %s, Loses = %s, Ties = %s WHERE Username = %s"
    mycursor.execute(query , (wins, loses, ties, player))
    mydb.commit()