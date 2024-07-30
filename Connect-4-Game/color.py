import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]

rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G")
    for x in range(rows):
        print("   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔵" or gameBoard[x][y] == "🔴":
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", end="    |")
        print()
    print("   +----+----+----+----+----+----+----+")

def modifyArray(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner(chip):
    ### Check horizontal spaces
    for x in range(rows):
        for y in range(cols - 3):
            if gameBoard[x][y] == chip and gameBoard[x][y + 1] == chip and gameBoard[x][y + 2] == chip and gameBoard[x][y + 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    ### Check vertical spaces
    for x in range(rows - 3):
        for y in range(cols):
            if gameBoard[x][y] == chip and gameBoard[x + 1][y] == chip and gameBoard[x + 2][y] == chip and gameBoard[x + 3][y] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    ### Check upper right to bottom left diagonal spaces
    for x in range(rows - 3):
        for y in range(3, cols):
            if gameBoard[x][y] == chip and gameBoard[x + 1][y - 1] == chip and gameBoard[x + 2][y - 2] == chip and gameBoard[x + 3][y - 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    ### Check upper left to bottom right diagonal spaces
    for x in range(rows - 3):
        for y in range(cols - 3):
            if gameBoard[x][y] == chip and gameBoard[x + 1][y + 1] == chip and gameBoard[x + 2][y + 2] == chip and gameBoard[x + 3][y + 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True
    return False

def coordinateParser(inputString):
    coordinate = [None] * 2
    if inputString[0] in possibleLetters:
        coordinate[1] = possibleLetters.index(inputString[0])
    else:
        raise ValueError("Invalid column letter")
    coordinate[0] = int(inputString[1])
    if coordinate[0] < 0 or coordinate[0] >= rows:
        raise ValueError("Invalid row number")
    return coordinate

def isSpaceAvailable(intendedCoordinate):
    if gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] in ('🔴', '🔵'):
        return False
    return True

def gravityChecker(intendedCoordinate):
    ### Calculate space below
    spaceBelow = [intendedCoordinate[0] + 1, intendedCoordinate[1]]
    ### Is the coordinate at ground level or has a token below
    if spaceBelow[0] == rows or not isSpaceAvailable(spaceBelow):
        return True
    return False

def getValidSpace(column):
    for row in reversed(range(rows)):
        if gameBoard[row][column] == "":
            return [row, column]
    return None

def getUserInput():
    while True:
        try:
            spacePicked = input("\nChoose a space (e.g., A0): ").upper()
            if len(spacePicked) != 2 or spacePicked[0] not in possibleLetters or not spacePicked[1].isdigit():
                raise ValueError("Invalid input format. Please use the format 'A0', 'B1', etc.")
            coordinate = coordinateParser(spacePicked)
            return coordinate
        except ValueError as e:
            print(e)
        except Exception as e:
            print("Error occurred:", e)

leaveLoop = False
turnCounter = 0
while not leaveLoop:
    if turnCounter % 2 == 0:
        printGameBoard()
        while True:
            try:
                coordinate = getUserInput()
                column = coordinate[1]
                validSpace = getValidSpace(column)
                if validSpace and gravityChecker(validSpace):
                    modifyArray(validSpace, '🔵')
                    break
                else:
                    print("Not a valid coordinate")
            except Exception as e:
                print("Error occurred:", e)
        winner = checkForWinner('🔵')
    else:
        while True:
            try:
                column = random.randint(0, 6)
                validSpace = getValidSpace(column)
                if validSpace and gravityChecker(validSpace):
                    modifyArray(validSpace, '🔴')
                    break
            except:
                continue
        winner = checkForWinner('🔴')
    
    turnCounter += 1

    if winner:
        printGameBoard()
        break
