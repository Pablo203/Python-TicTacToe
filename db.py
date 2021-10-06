import pymysql
import os

os.system("sudo /opt/lampp/./xampp start")


mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "TicTacToe"
)

def checkPlayer(player):
    mycursor = mydb.cursor()
    query = "SELECT Username FROM Users WHERE Username = %s"
    mycursor.execute(query , (player))
    result = mycursor.fetchone()
    '''for x in result:
        x = int(float(x))
        print(result[x])
        if(result[x] == player):
            return True
    return False'''
    '''
    if(result == player):
        return True
    return False'''
    for x in result:
        if(x == player):
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
    result = mycursor.fetchone()
    mydb.commit()

def updatePlayer(player, results):
    help = 0
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
            print(x)
            values["wins"] = x
        elif(help == 1):
            print(x)
            values["loses"] = x
        elif(help == 2):
            print(x)
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