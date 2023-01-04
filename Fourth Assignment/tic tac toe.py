import pyfiglet

def show():
    for row in gameboard:
        for cell in row:
            print(cell,end = "")
        print() #this is a \n. commands to go to the next line.

def checkgame1():
    if gameboard[0][0] == " X " and gameboard[0][1] == " X " and gameboard[0][2] == " X ":
        result = ("player 1 wins!")
    elif gameboard[1][0] == " X " and gameboard[1][1] == " X " and gameboard[1][2] == " X ":
        result = ("player 1 wins!")
    elif gameboard[2][0] == " X " and gameboard[2][1] == " X " and gameboard[2][2] == " X ":
        result = ("player 1 wins!")
    elif gameboard[0][0] == " X " and gameboard[1][0] == " X " and gameboard[2][0] == " X ":
        result = ("player 1 wins!")
    elif gameboard[0][1] == " X " and gameboard[1][1] == " X " and gameboard[2][1] == " X ":
        result = ("player 1 wins!")
    elif gameboard[0][2] == " X " and gameboard[1][2] == " X " and gameboard[2][2] == " X ":
        result = ("player 1 wins!")
    elif gameboard[0][0] == " X " and gameboard[1][1] == " X " and gameboard[2][2] == " X ":
        result = ("player 1 wins!")
    elif gameboard[0][2] == " X " and gameboard[1][1] == " X " and gameboard[2][0] == " X ":
        result = ("player 1 wins!")

def checkgame2():
    if gameboard[0][0] == " O " and gameboard[0][1] == " O " and gameboard[0][2] == " O ":
        print("player 2 wins!")
    elif gameboard[1][0] == " O " and gameboard[1][1] == " O " and gameboard[1][2] == " O ":
        print("player 2 wins!")
    elif gameboard[2][0] == " O " and gameboard[2][1] == " O " and gameboard[2][2] == " O ":
        print("player 2 wins!")
    elif gameboard[0][0] == " O " and gameboard[1][0] == " O " and gameboard[2][0] == " O ":
        print("player 2 wins!")
    elif gameboard[0][1] == " O " and gameboard[1][1] == " O " and gameboard[2][1] == " O ":
        print("player 2 wins!")
    elif gameboard[0][2] == " O " and gameboard[1][2] == " O " and gameboard[2][2] == " O ":
        print("player 2 wins!")
    elif gameboard[0][0] == " O " and gameboard[1][1] == " O " and gameboard[2][2] == " O ":
        print("player 2 wins!")
    elif gameboard[0][2] == " O " and gameboard[1][1] == " O " and gameboard[2][0] == " O ":
        print("player 2 wins!")

def nowinner():
    for i in gameboard:
        if i != " - ":
            if not (gameboard[0][0] == " O " and gameboard[0][1] == " O " and gameboard[0][2] == " O ") or (gameboard[1][0] == " O " and gameboard[1][1] == " O " and gameboard[1][2] == " O ") or (gameboard[2][0] == " O " and gameboard[2][1] == " O " and gameboard[2][2] == " O ") or (gameboard[0][0] == " O " and gameboard[1][0] == " O " and gameboard[2][0] == " O ") or (gameboard[0][1] == " O " and gameboard[1][1] == " O " and gameboard[2][1] == " O ") or (gameboard[0][2] == " O " and gameboard[1][2] == " O " and gameboard[2][2] == " O ") or (gameboard[0][0] == " O " and gameboard[1][1] == " O " and gameboard[2][2] == " O ") or (gameboard[0][2] == " O " and gameboard[1][1] == " O " and gameboard[2][0] == " O ") or (gameboard[0][0] == " X " and gameboard[0][1] == " X " and gameboard[0][2] == " X ") or (gameboard[1][0] == " X " and gameboard[1][1] == " X " and gameboard[1][2] == " X ") or (gameboard[2][0] == " X " and gameboard[2][1] == " X " and gameboard[2][2] == " X ") or (gameboard[0][0] == " X " and gameboard[1][0] == " X " and gameboard[2][0] == " X ") or (gameboard[0][1] == " X " and gameboard[1][1] == " X " and gameboard[2][1] == " X ") or (gameboard[0][2] == " X " and gameboard[1][2] == " X " and gameboard[2][2] == " X ") or (gameboard[0][0] == " X " and gameboard[1][1] == " X " and gameboard[2][2] == " X ") or (gameboard[0][2] == " X " and gameboard[1][1] == " X " and gameboard[2][0] == " X "):
                print("nobody wins!")
                


title = pyfiglet.figlet_format("Tic Tac Toe", font = "slant")
print(title)

gameboard = [[" - ", " - ", " - ",],
             [" - ", " - ", " - ",],
             [" - ", " - ", " - ",]]
show()

while True:
    print("player 1")
    while True:
        row = int(input("row: "))
        col = int(input("column: "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if gameboard[row][col] == " - ":
                gameboard[row][col] = " X "
                show()
                checkgame1()
                break
            else:
                print("select another cell: ")
        else:
            print("enter the row and column between 0 to 2")
        nowinner()

    print("player 2")
    while True:
        row = int(input("row: "))
        col = int(input("column: "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if gameboard[row][col] == " - ":
                gameboard[row][col] = " O "
                show()
                checkgame2()
                break
            else:
                print("select another cell: ")
        else:
            print("enter the row and column between 0 to 2")
        nowinner()