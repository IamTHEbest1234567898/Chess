import random

# Piece worths
Queen = 9
Rook = 5
Bishop = 3
Knight = 3
Pawn = 1

# Chess pieces
#--- Black ---
blackKingPiece = "♔"
blackQueenPiece = "♕"
blackRookPiece = "♖"
blackBishopPiece = "♗"
blackKnightPiece = "♘"
blackPawnPiece = "♙"

blackList = [blackKingPiece, blackQueenPiece, blackRookPiece, blackBishopPiece, blackKnightPiece, blackPawnPiece]

#--- White ___
whiteKingPiece = "♚"
whiteQueenPiece = "♛"
whiteRookPiece = "♜"
whiteBishopPiece = "♝"
whiteKnightPiece = "♞"
whitePawnPiece = "♟"

whiteList = [whiteKingPiece, whiteQueenPiece, whiteRookPiece, whiteBishopPiece, whiteKnightPiece, whitePawnPiece]


board = ["　", "　", "　", "　", "　", "　", "　", "　",
         "　", "　", "　", "　", "　", "　", "　", "　",
         "　", "　", "　", "　", "　", "　", "　", "　",
         "　", "　", "　", "　", "　", "　", "　", "　",
         "　", "　", "　", "　", "　", "　", "　", "　",
         "　", "　", "　", "　", "　", "　", "　", "　",
         "　", "　", "　", "　", "　", "　", "　", "　",
         "　", "　", "　", "　", "　", "　", "　", "　"]

FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
#FEN = "2r3k1/Q7/5p1p/7B/pp2pB1N/3R2P1/3K3p/7R w - - 0 1"
#FEN = "4k3/qqqqqqqq/8/8/8/8/8/4K3 w - - 0 1"

enPassantLast = "-"
blackCaptureList = ["Black: "]
whiteCaptureList = ["White: "]
whiteCaptureCounter = 0
blackThreats = []
whiteThreats = []
gameGoing = True

def FENToBoard(FEN, board):
    boardCounter = 0
    FEN_List = []
    FEN_ListCounter = 0

    for letter in FEN:
        FEN_List.append(letter)

    for i in FEN_List:
        while boardCounter < 64:
            print(FEN_List[FEN_ListCounter])
            # Black
            if (FEN_List[FEN_ListCounter] == "r"):
               board[boardCounter] = blackRookPiece
            elif (FEN_List[FEN_ListCounter] == "n"):
               board[boardCounter] = blackKnightPiece
            elif (FEN_List[FEN_ListCounter] == "b"):
               board[boardCounter] = blackBishopPiece
            elif (FEN_List[FEN_ListCounter] == "q"):
               board[boardCounter] = blackQueenPiece
            elif (FEN_List[FEN_ListCounter] == "k"):
               board[boardCounter] = blackKingPiece
            elif (FEN_List[FEN_ListCounter] == "p"):
               board[boardCounter] = blackPawnPiece

            # White
            elif (FEN_List[FEN_ListCounter] == "R"):
               board[boardCounter] = whiteRookPiece
            elif (FEN_List[FEN_ListCounter] == "N"):
               board[boardCounter] = whiteKnightPiece
            elif (FEN_List[FEN_ListCounter] == "B"):
               board[boardCounter] = whiteBishopPiece
            elif (FEN_List[FEN_ListCounter] == "Q"):
               board[boardCounter] = whiteQueenPiece
            elif (FEN_List[FEN_ListCounter] == "K"):
               board[boardCounter] = whiteKingPiece
            elif (FEN_List[FEN_ListCounter] == "P"):
               board[boardCounter] = whitePawnPiece

            # Else
            elif (FEN_List[FEN_ListCounter].isnumeric()):
                count = int(FEN_List[FEN_ListCounter]) - 1
                while (count > 0):
                    board[boardCounter] = "　"
                    boardCounter = boardCounter + 1
                    count = count - 1

            if (FEN_List[FEN_ListCounter] != '/'):
                boardCounter = boardCounter + 1
            FEN_ListCounter = FEN_ListCounter + 1

def fullMoveClock(FEN):
    FEN_List = FEN.split(' ')
    return int(FEN_List[5])

def halfMoveClock(FEN):
    FEN_List = FEN.split(' ')
    return int(FEN_List[4])

def enPassant(FEN):
    FEN_List = FEN.split(' ')
    return FEN_List[3]

def castlingRights(FEN):
    FEN_List = FEN.split(' ')
    return FEN_List[2]

def currentMove(FEN):
    FEN_List = FEN.split(' ')
    return FEN_List[1]

def boardToFEN(FEN, board, capture, enPassantLast):
    boardCounter = 0

    currentMoveColour = currentMove(FEN)

    fullMoveClockLocal = fullMoveClock(FEN) + 1
    if (currentMoveColour == "b"):
        fullMoveClockLocal = fullMoveClockLocal + 1
        currentMoveColour = "w"

    if (currentMoveColour == "w"):
        currentMoveColour = "b"

    halfMoveClockLocal = halfMoveClock(FEN)
    if (capture == 0):
        halfMoveClockLocal = halfMoveClockLocal + 1

    castlingRightsLocal = castlingRights(FEN)

    currentBoardPos = ""
    numCounter = 1

    while boardCounter < 64:
        if (board[boardCounter] == "　"):
            if (boardCounter != 63):
                if (board[boardCounter + 1] != "　" or boardCounter == 7 or boardCounter == 15 or boardCounter == 23 or boardCounter == 31 or boardCounter == 39 or boardCounter == 47 or boardCounter == 55):
                    currentBoardPos = currentBoardPos + str(numCounter)
                    numCounter = 1
                else:
                    numCounter = numCounter + 1

        # Black
        elif (board[boardCounter] == "♖"):
            currentBoardPos = currentBoardPos + "r"
        elif (board[boardCounter] == "♘"):
            currentBoardPos = currentBoardPos + "n"
        elif (board[boardCounter] == "♗"):
            currentBoardPos = currentBoardPos + "b"
        elif (board[boardCounter] == "♕"):
            currentBoardPos = currentBoardPos + "q"
        elif (board[boardCounter] == "♔"):
            currentBoardPos = currentBoardPos + "k"
        elif (board[boardCounter] == "♙"):
            currentBoardPos = currentBoardPos + "p"

        # White
        elif (board[boardCounter] == "♜"):
            currentBoardPos = currentBoardPos + "R"
        elif (board[boardCounter] == "♞"):
            currentBoardPos = currentBoardPos + "N"
        elif (board[boardCounter] == "♝"):
            currentBoardPos = currentBoardPos + "B"
        elif (board[boardCounter] == "♛"):
            currentBoardPos = currentBoardPos + "Q"
        elif (board[boardCounter] == "♚"):
            currentBoardPos = currentBoardPos + "K"
        elif (board[boardCounter] == "♟"):
            currentBoardPos = currentBoardPos + "P"

        if (boardCounter == 7 or boardCounter == 15 or boardCounter == 23 or boardCounter == 31 or boardCounter == 39 or boardCounter == 47 or boardCounter == 55):
            currentBoardPos = currentBoardPos + "/"

        boardCounter = boardCounter + 1

    tempFEN = currentBoardPos + " " + currentMoveColour + " " + castlingRightsLocal + " " + enPassantLast + " " + str(halfMoveClockLocal) + " " + str(fullMoveClockLocal)
    print(tempFEN)
    return tempFEN

def displayBoard(board, whiteCaptureList, blackCaptureList, whiteCaptureCounter):
    print("8|" + board[0] + "|" + board[1] + "|" + board[2] + "|" + board[3] + "|" + board[4] + "|" + board[5] + "|" + board[6] + "|" + board[7] + "|")
    print("7|" + board[8] + "|" + board[9] + "|" + board[10] + "|" + board[11] + "|" + board[12] + "|" + board[13] + "|" + board[14] + "|" + board[15] + "|")
    print("6|" + board[16] + "|" + board[17] + "|" + board[18] + "|" + board[19] + "|" + board[20] + "|" + board[21] + "|" + board[22] + "|" + board[23] + "|")
    print("5|" + board[24] + "|" + board[25] + "|" + board[26] + "|" + board[27] + "|" + board[28] + "|" + board[29] + "|" + board[30] + "|" + board[31] + "|")
    print("4|" + board[32] + "|" + board[33] + "|" + board[34] + "|" + board[35] + "|" + board[36] + "|" + board[37] + "|" + board[38] + "|" + board[39] + "|")
    print("3|" + board[40] + "|" + board[41] + "|" + board[42] + "|" + board[43] + "|" + board[44] + "|" + board[45] + "|" + board[46] + "|" + board[47] + "|")
    print("2|" + board[48] + "|" + board[49] + "|" + board[50] + "|" + board[51] + "|" + board[52] + "|" + board[53] + "|" + board[54] + "|" + board[55] + "|")
    print("1|" + board[56] + "|" + board[57] + "|" + board[58] + "|" + board[59] + "|" + board[60] + "|" + board[61] + "|" + board[62] + "|" + board[63] + "|")
    print("0   A　B　C　D　E　F　G　H")
    count = 0
    whiteCapturesStr = ""
    blackCapturesStr = ""
    if (whiteCaptureCounter > 0):
        whiteCaptureCounterLocal = "+" + str(whiteCaptureCounter)
    else:
        whiteCaptureCounterLocal = str(whiteCaptureCounter)
    for i in whiteCaptureList:
        whiteCapturesStr = whiteCapturesStr + whiteCaptureList[count]
        count = count + 1
    whiteCapturesStr = whiteCapturesStr + " " + whiteCaptureCounterLocal
    print(whiteCapturesStr)
    count = 0
    for i in blackCaptureList:
        blackCapturesStr = blackCapturesStr + blackCaptureList[count]
        count = count + 1
    print(blackCapturesStr)

def whiteThreats(board, whiteList):
    PieceMoves = []
    legalMoves = []
    illegalMoves = []
    boardCounter = 0
    for i in board:
        if (board[boardCounter] == "♚"):
            legalMoves.append(-9)
            legalMoves.append(-8)
            legalMoves.append(-7)
            legalMoves.append(-1)
            legalMoves.append(9)
            legalMoves.append(8)
            legalMoves.append(7)
            legalMoves.append(1)
            if (boardCounter < 55):
                legalMoves.pop(4)
                legalMoves.pop(4)
                legalMoves.pop(4)
            elif (boardCounter < 8):
                legalMoves.pop(0)
                legalMoves.pop(0)
                legalMoves.pop(0)

            count = 0
            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63 or boardCounter + legalMoves[count] < 0):
                    illegalMoves.append(legalMoves[count])
                else:
                    if (board[boardCounter + legalMoves[count]] in whiteList):
                        illegalMoves.append(legalMoves[count])
                count = count + 1

            legalMoves = [x for x in legalMoves if x not in illegalMoves]

            tempMoves = [boardCounter]
            count = 0
            for i in legalMoves:
                tempMoves.append(legalMoves[count])
                count = count + 1

            PieceMoves.append(tempMoves)

        if (board[boardCounter] == "♛"):
            # diagonal

            illegalMoves = []
            legalMoves = []

            legalMoves.append(-63)
            legalMoves.append(-54)
            legalMoves.append(-45)
            legalMoves.append(-36)
            legalMoves.append(-27)
            legalMoves.append(-18)
            legalMoves.append(-9)
            legalMoves.append(9)
            legalMoves.append(18)
            legalMoves.append(27)
            legalMoves.append(36)
            legalMoves.append(45)
            legalMoves.append(54)
            legalMoves.append(63)

            legalMoves.append(-49)
            legalMoves.append(-42)
            legalMoves.append(-35)
            legalMoves.append(-28)
            legalMoves.append(-21)
            legalMoves.append(-14)
            legalMoves.append(-7)
            legalMoves.append(7)
            legalMoves.append(14)
            legalMoves.append(21)
            legalMoves.append(28)
            legalMoves.append(35)
            legalMoves.append(42)
            legalMoves.append(49)
            # straight
            legalMoves.append(-7)
            legalMoves.append(-6)
            legalMoves.append(-5)
            legalMoves.append(-4)
            legalMoves.append(-3)
            legalMoves.append(-2)
            legalMoves.append(-1)
            legalMoves.append(1)
            legalMoves.append(2)
            legalMoves.append(3)
            legalMoves.append(4)
            legalMoves.append(5)
            legalMoves.append(6)
            legalMoves.append(7)

            legalMoves.append(-56)
            legalMoves.append(-48)
            legalMoves.append(-40)
            legalMoves.append(-32)
            legalMoves.append(-24)
            legalMoves.append(-16)
            legalMoves.append(-8)
            legalMoves.append(8)
            legalMoves.append(16)
            legalMoves.append(24)
            legalMoves.append(32)
            legalMoves.append(40)
            legalMoves.append(48)
            legalMoves.append(56)

            count = 0
            diagonalLeftUp = [-63, -54, -45, -36, -27, -18, -9]
            diagonalRightDown = [9, 18, 27, 36, 45, 54, 63]
            diagonalRightUp = [-49, -42, -35, -28, -21, -14, -7]
            diagonalLeftDown = [7, 14, 21, 28, 35, 42, 49]

            straightLeft = [-7, -6, -5, -4, -3, -2, -1]
            straightRight = [1, 2, 3, 4, 5, 6, 7]
            straightDown = [8, 16, 24, 32, 40, 48, 56]
            straightUp = [-8, -16, -24, -32, -40, -48, -56]

            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63):
                    if (legalMoves[count] in illegalMoves):
                        illegalMoves.append(legalMoves[count])
                elif (board[boardCounter + legalMoves[count]] in whiteList):
                    currentIllegalMove = legalMoves[count]
                    illegalMoves.append(legalMoves[count])
                    # Left Up
                    if (currentIllegalMove in diagonalLeftUp):
                        if (currentIllegalMove == -54):
                            diagonalLeftUp = [-63]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -45):
                            diagonalLeftUp = [-63, -54]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -36):
                            diagonalLeftUp = [-63, -54, -45]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -27):
                            diagonalLeftUp = [-63, -54, -45, -36]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -18):
                            diagonalLeftUp = [-63, -54, -45, -36, -27]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -9):
                            diagonalLeftUp = [-63, -54, -45, -36, -27, -18]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                    # Right Up
                    if (currentIllegalMove in diagonalRightUp):
                        if (currentIllegalMove == -42):
                            diagonalRightUp = [-49]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -35):
                            diagonalRightUp = [-49, -42]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -28):
                            diagonalRightUp = [-49, -42, -35]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -21):
                            diagonalRightUp = [-49, -42, -35, -28]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -14):
                            diagonalRightUp = [-49, -42, -35, -28, -21]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -7):
                            diagonalRightUp = [-49, -42, -35, -28, -21, -14]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                    # Left Down
                    if (currentIllegalMove in diagonalLeftDown):
                        if (currentIllegalMove == 7):
                            diagonalLeftDown = [14, 21, 28, 35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 14):
                            diagonalLeftDown = [21, 28, 35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 21):
                            diagonalLeftDown = [28, 35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 28):
                            diagonalLeftDown = [35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 35):
                            diagonalLeftDown = [42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 42):
                            diagonalLeftDown = [49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                    # Right Down
                    if (currentIllegalMove in diagonalRightDown):
                        if (currentIllegalMove == 9):
                            diagonalRightDown = [18, 27, 36, 45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 18):
                            diagonalRightDown = [27, 36, 45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 27):
                            diagonalRightDown = [36, 45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 36):
                            diagonalRightDown = [45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 45):
                            diagonalRightDown = [54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 54):
                            diagonalRightDown = [63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                    # Left
                    if (currentIllegalMove in straightLeft):
                        if (currentIllegalMove == -7):
                            straightLeft = [-6, -5, -4, -3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -6):
                            straightLeft = [-5, -4, -3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -5):
                            straightLeft = [-4, -3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -4):
                            straightLeft = [-3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -3):
                            straightLeft = [-2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -2):
                            straightLeft = [-1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                    # Right
                    if (currentIllegalMove in straightRight):
                        if (currentIllegalMove == 1):
                            straightRight = [2, 3, 4, 5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 2):
                            straightRight = [3, 4, 5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 3):
                            straightRight = [4, 5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 4):
                            straightRight = [5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 5):
                            straightRight = [6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 6):
                            straightRight = [7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                    # Down
                    if (currentIllegalMove in straightDown):
                        if (currentIllegalMove == 8):
                            straightDown = [16, 24, 32, 40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 16):
                            straightDown = [24, 32, 40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 24):
                            straightDown = [32, 40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 32):
                            straightDown = [40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 40):
                            straightDown = [48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 48):
                            straightDown = [56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                    # Up
                    if (currentIllegalMove in straightUp):
                        if (currentIllegalMove == -8):
                            straightUp = [-16, -24, -32, -40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -16):
                            straightUp = [-24, -32, -40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -24):
                            straightUp = [-32, -40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -32):
                            straightUp = [-40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -40):
                            straightUp = [-48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -48):
                            straightUp = [-56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                count = count + 1

            count = 0
            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63 or boardCounter + legalMoves[count] < 0):
                    illegalMoves.append(legalMoves[count])
                else:
                    if (board[boardCounter + legalMoves[count]] in whiteList):
                        illegalMoves.append(legalMoves[count])
                count = count + 1

            legalMoves = [x for x in legalMoves if x not in illegalMoves]

            tempMoves = [boardCounter]
            count = 0
            for i in legalMoves:
                tempMoves.append(legalMoves[count])
                count = count + 1

            PieceMoves.append(tempMoves)

        if (board[boardCounter] == "♜"):

            illegalMoves = []
            legalMoves = []

            legalMoves.append(-7)
            legalMoves.append(-6)
            legalMoves.append(-5)
            legalMoves.append(-4)
            legalMoves.append(-3)
            legalMoves.append(-2)
            legalMoves.append(-1)
            legalMoves.append(1)
            legalMoves.append(2)
            legalMoves.append(3)
            legalMoves.append(4)
            legalMoves.append(5)
            legalMoves.append(6)
            legalMoves.append(7)

            legalMoves.append(-56)
            legalMoves.append(-48)
            legalMoves.append(-40)
            legalMoves.append(-32)
            legalMoves.append(-24)
            legalMoves.append(-16)
            legalMoves.append(-8)
            legalMoves.append(8)
            legalMoves.append(16)
            legalMoves.append(24)
            legalMoves.append(32)
            legalMoves.append(40)
            legalMoves.append(48)
            legalMoves.append(56)

            count = 0
            straightLeft = [-7, -6, -5, -4, -3, -2, -1]
            straightRight = [1, 2, 3, 4, 5, 6, 7]
            straightDown = [8, 16, 24, 32, 40, 48, 56]
            straightUp = [-8, -16, -24, -32, -40, -48, -56]

            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63):
                    if (legalMoves[count] in illegalMoves):
                        illegalMoves.append(legalMoves[count])
                elif (board[boardCounter + legalMoves[count]] in whiteList):
                    currentIllegalMove = legalMoves[count]
                    illegalMoves.append(legalMoves[count])
                    # Left
                    if (currentIllegalMove in straightLeft):
                        if (currentIllegalMove == -7):
                            straightLeft = [-6, -5, -4, -3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -6):
                            straightLeft = [-5, -4, -3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -5):
                            straightLeft = [-4, -3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -4):
                            straightLeft = [-3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -3):
                            straightLeft = [-2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -2):
                            straightLeft = [-1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                    # Right
                    if (currentIllegalMove in straightRight):
                        if (currentIllegalMove == 1):
                            straightRight = [2, 3, 4, 5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 2):
                            straightRight = [3, 4, 5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 3):
                            straightRight = [4, 5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 4):
                            straightRight = [5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 5):
                            straightRight = [6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 6):
                            straightRight = [7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                    # Down
                    if (currentIllegalMove in straightDown):
                        if (currentIllegalMove == 8):
                            straightDown = [16, 24, 32, 40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 16):
                            straightDown = [24, 32, 40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 24):
                            straightDown = [32, 40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 32):
                            straightDown = [40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 40):
                            straightDown = [48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 48):
                            straightDown = [56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                    # Up
                    if (currentIllegalMove in straightUp):
                        if (currentIllegalMove == -8):
                            straightUp = [-16, -24, -32, -40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -16):
                            straightUp = [-24, -32, -40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -24):
                            straightUp = [-32, -40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -32):
                            straightUp = [-40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -40):
                            straightUp = [-48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -48):
                            straightUp = [-56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                count = count + 1

            count = 0
            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63 or boardCounter + legalMoves[count] < 0):
                    illegalMoves.append(legalMoves[count])
                else:
                    if (board[boardCounter + legalMoves[count]] in whiteList):
                        illegalMoves.append(legalMoves[count])
                count = count + 1

            legalMoves = [x for x in legalMoves if x not in illegalMoves]

            tempMoves = [boardCounter]
            count = 0
            for i in legalMoves:
                tempMoves.append(legalMoves[count])
                count = count + 1

            PieceMoves.append(tempMoves)

        if (board[boardCounter] == "♝"):

            illegalMoves = []
            legalMoves = []

            legalMoves.append(-63)
            legalMoves.append(-54)
            legalMoves.append(-45)
            legalMoves.append(-36)
            legalMoves.append(-27)
            legalMoves.append(-18)
            legalMoves.append(-9)
            legalMoves.append(9)
            legalMoves.append(18)
            legalMoves.append(27)
            legalMoves.append(36)
            legalMoves.append(45)
            legalMoves.append(54)
            legalMoves.append(63)

            legalMoves.append(-49)
            legalMoves.append(-42)
            legalMoves.append(-35)
            legalMoves.append(-28)
            legalMoves.append(-21)
            legalMoves.append(-14)
            legalMoves.append(-7)
            legalMoves.append(7)
            legalMoves.append(14)
            legalMoves.append(21)
            legalMoves.append(28)
            legalMoves.append(35)
            legalMoves.append(42)
            legalMoves.append(49)

            count = 0
            diagonalLeftUp = [-63, -54, -45, -36, -27, -18, -9]
            diagonalRightDown = [9, 18, 27, 36, 45, 54, 63]
            diagonalRightUp = [-49, -42, -35, -28, -21, -14, -7]
            diagonalLeftDown = [7, 14, 21, 28, 35, 42, 49]

            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63 or boardCounter + legalMoves[count] < 0):
                    if (legalMoves[count] in illegalMoves):
                        illegalMoves.append(legalMoves[count])
                elif (board[boardCounter + legalMoves[count]] in whiteList):
                    currentIllegalMove = legalMoves[count]
                    illegalMoves.append(legalMoves[count])
                    # Left Up
                    if (currentIllegalMove in diagonalLeftUp):
                        if (currentIllegalMove == -54):
                            diagonalLeftUp = [-63]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -45):
                            diagonalLeftUp = [-63, -54]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -36):
                            diagonalLeftUp = [-63, -54, -45]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -27):
                            diagonalLeftUp = [-63, -54, -45, -36]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -18):
                            diagonalLeftUp = [-63, -54, -45, -36, -27]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -9):
                            diagonalLeftUp = [-63, -54, -45, -36, -27, -18]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                    # Right Up
                    if (currentIllegalMove in diagonalRightUp):
                        if (currentIllegalMove == -42):
                            diagonalRightUp = [-49]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -35):
                            diagonalRightUp = [-49, -42]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -28):
                            diagonalRightUp = [-49, -42, -35]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -21):
                            diagonalRightUp = [-49, -42, -35, -28]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -14):
                            diagonalRightUp = [-49, -42, -35, -28, -21]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -7):
                            diagonalRightUp = [-49, -42, -35, -28, -21, -14]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                    # Left Down
                    if (currentIllegalMove in diagonalLeftDown):
                        if (currentIllegalMove == 7):
                            diagonalLeftDown = [14, 21, 28, 35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 14):
                            diagonalLeftDown = [21, 28, 35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 21):
                            diagonalLeftDown = [28, 35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 28):
                            diagonalLeftDown = [35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 35):
                            diagonalLeftDown = [42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 42):
                            diagonalLeftDown = [49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                    # Right Down
                    if (currentIllegalMove in diagonalRightDown):
                        if (currentIllegalMove == 9):
                            diagonalRightDown = [18, 27, 36, 45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 18):
                            diagonalRightDown = [27, 36, 45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 27):
                            diagonalRightDown = [36, 45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 36):
                            diagonalRightDown = [45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 45):
                            diagonalRightDown = [54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 54):
                            diagonalRightDown = [63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                count = count + 1

            count = 0
            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63 or boardCounter + legalMoves[count] < 0):
                    illegalMoves.append(legalMoves[count])
                else:
                    if (board[boardCounter + legalMoves[count]] in whiteList):
                        illegalMoves.append(legalMoves[count])
                count = count + 1

            legalMoves = [x for x in legalMoves if x not in illegalMoves]

            tempMoves = [boardCounter]
            count = 0
            for i in legalMoves:
                tempMoves.append(legalMoves[count])
                count = count + 1

            PieceMoves.append(tempMoves)

        if (board[boardCounter] == "♞"):

            illegalMoves = []
            legalMoves = []

            legalMoves.append(-6)
            legalMoves.append(6)
            legalMoves.append(-10)
            legalMoves.append(10)
            legalMoves.append(-15)
            legalMoves.append(15)
            legalMoves.append(-17)
            legalMoves.append(17)

            count = 0
            knightMoves = [-6, 10, 6, -10, -15, -17, 15, 17]

            rightSide = [6, 7, 14, 15, 22, 23, 31, 30, 39, 38, 47, 46, 55, 54, 62, 63]
            leftSide = [0, 1, 8, 9, 16, 17, 24, 25, 32, 33, 40, 41, 48, 49, 56, 57]

            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63):
                    if (legalMoves[count] in illegalMoves):
                        continue
                    else:
                        illegalMoves.append(legalMoves[count])
                if (boardCounter in rightSide):
                    illegalMoves.append(10)
                    illegalMoves.append(-6)
                if (boardCounter in leftSide):
                    illegalMoves.append(-10)
                    illegalMoves.append(6)
                if (boardCounter <= 15):
                    illegalMoves.append(-15)
                    illegalMoves.append(-17)
                if (boardCounter >= 48):
                    illegalMoves.append(15)
                    illegalMoves.append(17)
            for i in knightMoves:
                if (knightMoves[count] in whiteList):
                    illegalMoves.append(legalMoves[count])
                    count = count + 1

            count = 0
            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63 or boardCounter + legalMoves[count] < 0):
                    illegalMoves.append(legalMoves[count])
                else:
                    if (board[boardCounter + legalMoves[count]] in whiteList):
                        illegalMoves.append(legalMoves[count])
                count = count + 1

            legalMoves = [x for x in legalMoves if x not in illegalMoves]

            tempMoves = [boardCounter]
            count = 0
            for i in legalMoves:
                tempMoves.append(legalMoves[count])
                count = count + 1

            PieceMoves.append(tempMoves)

        if (board[boardCounter] == "♟"):

            legalMoves = []
            illegalMoves = []

            if (boardCounter >= 48 and boardCounter <= 55):
                if (board[boardCounter - 8] not in blackList or board[boardCounter - 8] not in whiteList):
                    legalMoves.append(-8)
                    if (board[boardCounter - 16] not in blackList or board[boardCounter - 16] not in whiteList):
                        legalMoves.append(-16)
                if (board[boardCounter - 16] not in blackList or board[boardCounter - 16] not in whiteList):
                    legalMoves.append(-16)

            else:
                if (board[boardCounter - 8] not in blackList or board[boardCounter - 8] not in whiteList):
                    legalMoves.append(-8)

            if (board[boardCounter - 7] in blackList):
                legalMoves.append(7)

            if (board[boardCounter - 9] in blackList):
                legalMoves.append(9)

            # En passant
            if (enPassant(FEN) != "-"):
                enPassantPosition = enPassant(FEN)
                if (enPassantPosition == "a5"):
                    if (boardCounter == 33):
                        legalMoves.append(-7)
                elif (enPassantPosition == "b5"):
                    if (boardCounter == 32):
                        legalMoves.append(-9)
                    if (boardCounter == 34):
                        legalMoves.append(-7)
                elif (enPassantPosition == "c5"):
                    if (boardCounter == 33):
                        legalMoves.append(-9)
                    if (boardCounter == 35):
                        legalMoves.append(-7)
                elif (enPassantPosition == "d5"):
                    if (boardCounter == 34):
                        legalMoves.append(-9)
                    if (boardCounter == 36):
                        legalMoves.append(-7)
                elif (enPassantPosition == "e5"):
                    if (boardCounter == 35):
                        legalMoves.append(-8)
                    if (boardCounter == 37):
                        legalMoves.append(-7)
                elif (enPassantPosition == "f5"):
                    if (boardCounter == 36):
                        legalMoves.append(-9)
                    if (boardCounter == 38):
                        legalMoves.append(-7)
                elif (enPassantPosition == "g5"):
                    if (boardCounter == 37):
                        legalMoves.append(-9)
                    if (boardCounter == 39):
                        legalMoves.append(-7)
                elif (enPassantPosition == "h5"):
                    if (boardCounter == 39):
                        legalMoves.append(-9)

            count = 0
            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63 or boardCounter + legalMoves[count] < 0):
                    illegalMoves.append(legalMoves[count])
                else:
                    if (board[boardCounter + legalMoves[count]] in blackList):
                        illegalMoves.append(legalMoves[count])
                count = count + 1

            legalMoves = [x for x in legalMoves if x not in illegalMoves]

            tempMoves = [boardCounter]
            count = 0
            for i in legalMoves:
                tempMoves.append(legalMoves[count])
                count = count + 1

            PieceMoves.append(tempMoves)

        boardCounter = boardCounter + 1

    return PieceMoves


def blackThreats(board, blackList, blackThreats, FEN):
    PieceMoves = []
    illegalMoves = []
    boardCounter = 0

    coloumA = [0, 8, 16, 24, 32, 40, 48, 56]
    coloumB = [1, 9, 17, 25, 33, 41, 49, 57]
    coloumC = [2, 10, 18, 26, 34, 42, 50, 58]
    coloumD = [3, 11, 19, 27, 35, 43, 51, 59]
    coloumE = [4, 12, 20, 28, 36, 44, 52, 60]
    coloumF = [5, 13, 21, 29, 37, 45, 53, 61]
    coloumG = [6, 14, 22, 30, 38, 46, 54, 62]
    coloumH = [7, 15, 23, 31, 39, 47, 55, 63]

    row1 = [0, 1, 2, 3, 4, 5, 6, 7]
    row2 = [8, 9, 10, 11, 12, 13, 14, 15]
    row3 = [16, 17, 18, 19, 20, 21, 22, 23]
    row4 = [24, 25, 26, 27, 28, 29, 30, 31]
    row5 = [32, 33, 34, 35, 36, 37, 38, 39]
    row6 = [40, 41, 42, 43, 44, 45, 46, 47]
    row7 = [48, 49, 50, 51, 52, 53, 54, 55]
    row8 = [56, 57, 58, 59, 60, 61, 62, 63]

    for i in board:
        if (board[boardCounter] == "♔"):
            legalMoves = [1, -1 -9, -8, -7, 9, 8, 7]
            if (boardCounter < 55):
                legalMoves = [1, -1. -9, -8, -7,]
            elif (boardCounter < 8):
                legalMoves = [1, -1, 9, 8, 7]

            if (boardCounter in coloumH):
                illegalMoves.append(1)
            if (boardCounter in coloumA):
                illegalMoves.append(-1)

            #Castling
            FEN_List = FEN.split(' ')
            rights = FEN_List[2]
            castle = []
            for letter in rights:
                castle.append(letter)

            if ("k" in castle):
                if (board[5] == "　" and board[6] == "　"):
                    legalMoves.append(2)

            if ("q" in castle):
                if (board[1] == "　" and board[2] == "　" and board[3] == "　"):
                    legalMoves.append(-2)


            count = 0
            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63 or boardCounter + legalMoves[count] < 0):
                    illegalMoves.append(legalMoves[count])
                else:
                    if (board[boardCounter + legalMoves[count]] in blackList):
                        illegalMoves.append(legalMoves[count])
                count = count + 1

            legalMoves = [x for x in legalMoves if x not in illegalMoves]

            tempMoves = [boardCounter]
            count = 0
            for i in legalMoves:
                tempMoves.append(legalMoves[count])
                count = count + 1

            PieceMoves.append(tempMoves)

        if (board[boardCounter] == "♕"):
            # diagonal

            illegalMoves = []
            legalMoves = [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 16, 24, 32, 40, 48, 56, -8, -16, -24, -32,
                          -40, -48, -56, -63, -54, -45, -36, -27, -18, -9, 9, 18, 27, 36, 45, 54, 63, -49, -42, -35,
                          -28, -21, -14, -7, 7, 14, 21, 28, 35, 42, 49]

            count = 0
            diagonalLeftUp = [-63, -54, -45, -36, -27, -18, -9]
            diagonalRightDown = [9, 18, 27, 36, 45, 54, 63]
            diagonalRightUp = [-49, -42, -35, -28, -21, -14, -7]
            diagonalLeftDown = [7, 14, 21, 28, 35, 42, 49]

            straightLeft = [-7, -6, -5, -4, -3, -2, -1]
            straightRight = [1, 2, 3, 4, 5, 6, 7]
            straightDown = [8, 16, 24, 32, 40, 48, 56]
            straightUp = [-8, -16, -24, -32, -40, -48, -56]

            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63):
                    if (legalMoves[count] in illegalMoves):
                        illegalMoves.append(legalMoves[count])
                elif (board[boardCounter + legalMoves[count]] in blackList):
                    currentIllegalMove = legalMoves[count]
                    illegalMoves.append(legalMoves[count])
                    # Side cases
                    if (boardCounter in coloumA):
                        templist = [-7, -6, -5, -4, -3, -2, -1,
                                    -63, -54, -45, -36, -27, -18, -9,
                                    7, 14, 21, 28, 35, 42, 49]
                        illegalMoves.extend(templist)
                    elif (boardCounter in coloumB):
                        templist = [-7, -6, -5, -4, -3, -2,
                                    -63, -54, -45, -36, -27, -18,
                                    14, 21, 28, 35, 42, 49,
                                    7,
                                    63,
                                    -49]
                        illegalMoves.extend(templist)
                    elif (boardCounter in coloumC):
                        templist = [-7, -6, -5, -4, -3,
                                    -63, -54, -45, -36, -27,
                                    21, 28, 35, 42, 49,
                                    7, 6,
                                    63, 54,
                                    -49, -42]
                        illegalMoves.extend(templist)
                    elif (boardCounter in coloumD):
                        templist = [-7, -6, -5, -4,
                                    -63, -54, -45, -36,
                                    28, 35, 42, 49,
                                    7, 6, 5,
                                    63, 54, 45,
                                    -49, -42, -35]
                        illegalMoves.extend(templist)
                    elif (boardCounter in coloumE):
                        templist = [-7, -6, -5,
                                    -63, -54, -45,
                                    35, 42, 49,
                                    7, 6, 5, 4,
                                    63, 54, 45, 36,
                                    -49, -42, -35, -28]
                        illegalMoves.extend(templist)
                    elif (boardCounter in coloumF):
                        templist = [-7, -6,
                                    -63, -54,
                                    42, 49,
                                    7, 6, 5, 4, 3,
                                    63, 54, 45, 36, 27,
                                    -49, -42, -35, -28, -21]
                        illegalMoves.extend(templist)
                    elif (boardCounter in coloumG):
                        templist = [-7,
                                    -63,
                                    42,
                                    7, 6, 5, 4, 3, 2,
                                    63, 54, 45, 36, 27, 18,
                                    -49, -42, -35, -28, -21, -14]
                        illegalMoves.extend(templist)
                    elif (boardCounter in coloumH):
                        templist = [7, 6, 5, 4, 3, 2, 1,
                                    63, 54, 45, 36, 27, 18, 9,
                                    -49, -42, -35, -28, -21, -14, -7]
                        illegalMoves.extend(templist)

                    # Left Up
                    if (currentIllegalMove in diagonalLeftUp):
                        if (currentIllegalMove == -54):
                            diagonalLeftUp = [-63]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -45):
                            diagonalLeftUp = [-63, -54]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -36):
                            diagonalLeftUp = [-63, -54, -45]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -27):
                            diagonalLeftUp = [-63, -54, -45, -36]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -18):
                            diagonalLeftUp = [-63, -54, -45, -36, -27]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -9):
                            diagonalLeftUp = [-63, -54, -45, -36, -27, -18]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                    # Right Up
                    if (currentIllegalMove in diagonalRightUp):
                        if (currentIllegalMove == -42):
                            diagonalRightUp = [-49]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -35):
                            diagonalRightUp = [-49, -42]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -28):
                            diagonalRightUp = [-49, -42, -35]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -21):
                            diagonalRightUp = [-49, -42, -35, -28]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -14):
                            diagonalRightUp = [-49, -42, -35, -28, -21]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -7):
                            diagonalRightUp = [-49, -42, -35, -28, -21, -14]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                    # Left Down
                    if (currentIllegalMove in diagonalLeftDown):
                        if (currentIllegalMove == 7):
                            diagonalLeftDown = [14, 21, 28, 35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 14):
                            diagonalLeftDown = [21, 28, 35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 21):
                            diagonalLeftDown = [28, 35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 28):
                            diagonalLeftDown = [35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 35):
                            diagonalLeftDown = [42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 42):
                            diagonalLeftDown = [49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                    # Right Down
                    if (currentIllegalMove in diagonalRightDown):
                        if (currentIllegalMove == 9):
                            diagonalRightDown = [18, 27, 36, 45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 18):
                            diagonalRightDown = [27, 36, 45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 27):
                            diagonalRightDown = [36, 45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 36):
                            diagonalRightDown = [45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 45):
                            diagonalRightDown = [54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 54):
                            diagonalRightDown = [63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                    # Left
                    if (currentIllegalMove in straightLeft):
                        if (currentIllegalMove == -7):
                            straightLeft = [-6, -5, -4, -3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -6):
                            straightLeft = [-5, -4, -3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -5):
                            straightLeft = [-4, -3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -4):
                            straightLeft = [-3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -3):
                            straightLeft = [-2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -2):
                            straightLeft = [-1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                    # Right
                    if (currentIllegalMove in straightRight):
                        if (currentIllegalMove == 1):
                            straightRight = [2, 3, 4, 5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 2):
                            straightRight = [3, 4, 5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 3):
                            straightRight = [4, 5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 4):
                            straightRight = [5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 5):
                            straightRight = [6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 6):
                            straightRight = [7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                    # Down
                    if (currentIllegalMove in straightDown):
                        if (currentIllegalMove == 8):
                            straightDown = [16, 24, 32, 40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 16):
                            straightDown = [24, 32, 40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 24):
                            straightDown = [32, 40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 32):
                            straightDown = [40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 40):
                            straightDown = [48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 48):
                            straightDown = [56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                    # Up
                    if (currentIllegalMove in straightUp):
                        if (currentIllegalMove == -8):
                            straightUp = [-16, -24, -32, -40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -16):
                            straightUp = [-24, -32, -40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -24):
                            straightUp = [-32, -40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -32):
                            straightUp = [-40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -40):
                            straightUp = [-48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -48):
                            straightUp = [-56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                elif (board[boardCounter + legalMoves[count]] in whiteList):
                    currentIllegalMove = legalMoves[count]

                    # Left Up
                    if (currentIllegalMove in diagonalLeftUp):
                        if (currentIllegalMove == -54):
                            diagonalLeftUp = [-63]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -45):
                            diagonalLeftUp = [-63, -54]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -36):
                            diagonalLeftUp = [-63, -54, -45]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -27):
                            diagonalLeftUp = [-63, -54, -45, -36]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -18):
                            diagonalLeftUp = [-63, -54, -45, -36, -27]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -9):
                            diagonalLeftUp = [-63, -54, -45, -36, -27, -18]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                    # Right Up
                    if (currentIllegalMove in diagonalRightUp):
                        if (currentIllegalMove == -42):
                            diagonalRightUp = [-49]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -35):
                            diagonalRightUp = [-49, -42]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -28):
                            diagonalRightUp = [-49, -42, -35]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -21):
                            diagonalRightUp = [-49, -42, -35, -28]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -14):
                            diagonalRightUp = [-49, -42, -35, -28, -21]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -7):
                            diagonalRightUp = [-49, -42, -35, -28, -21, -14]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                    # Left Down
                    if (currentIllegalMove in diagonalLeftDown):
                        if (currentIllegalMove == 7):
                            diagonalLeftDown = [14, 21, 28, 35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 14):
                            diagonalLeftDown = [21, 28, 35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 21):
                            diagonalLeftDown = [28, 35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 28):
                            diagonalLeftDown = [35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 35):
                            diagonalLeftDown = [42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 42):
                            diagonalLeftDown = [49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                    # Right Down
                    if (currentIllegalMove in diagonalRightDown):
                        if (currentIllegalMove == 9):
                            diagonalRightDown = [18, 27, 36, 45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 18):
                            diagonalRightDown = [27, 36, 45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 27):
                            diagonalRightDown = [36, 45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 36):
                            diagonalRightDown = [45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 45):
                            diagonalRightDown = [54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 54):
                            diagonalRightDown = [63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                    # Left
                    if (currentIllegalMove in straightLeft):
                        if (currentIllegalMove == -7):
                            straightLeft = [-6, -5, -4, -3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -6):
                            straightLeft = [-5, -4, -3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -5):
                            straightLeft = [-4, -3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -4):
                            straightLeft = [-3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -3):
                            straightLeft = [-2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -2):
                            straightLeft = [-1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                    # Right
                    if (currentIllegalMove in straightRight):
                        if (currentIllegalMove == 1):
                            straightRight = [2, 3, 4, 5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 2):
                            straightRight = [3, 4, 5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 3):
                            straightRight = [4, 5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 4):
                            straightRight = [5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 5):
                            straightRight = [6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 6):
                            straightRight = [7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                    # Down
                    if (currentIllegalMove in straightDown):
                        if (currentIllegalMove == 8):
                            straightDown = [16, 24, 32, 40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 16):
                            straightDown = [24, 32, 40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 24):
                            straightDown = [32, 40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 32):
                            straightDown = [40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 40):
                            straightDown = [48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 48):
                            straightDown = [56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                    # Up
                    if (currentIllegalMove in straightUp):
                        if (currentIllegalMove == -8):
                            straightUp = [-16, -24, -32, -40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -16):
                            straightUp = [-24, -32, -40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -24):
                            straightUp = [-32, -40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -32):
                            straightUp = [-40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -40):
                            straightUp = [-48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -48):
                            straightUp = [-56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                count = count + 1

            count = 0
            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63 or boardCounter + legalMoves[count] < 0):
                    illegalMoves.append(legalMoves[count])
                else:
                    if (board[boardCounter + legalMoves[count]] in blackList):
                        illegalMoves.append(legalMoves[count])
                count = count + 1

            legalMoves = [x for x in legalMoves if x not in illegalMoves]

            tempMoves = [boardCounter]
            count = 0
            for i in legalMoves:
                tempMoves.append(legalMoves[count])
                count = count + 1

            PieceMoves.append(tempMoves)

        if (board[boardCounter] == "♖"):

            illegalMoves = []
            legalMoves = []

            legalMoves.append(-7)
            legalMoves.append(-6)
            legalMoves.append(-5)
            legalMoves.append(-4)
            legalMoves.append(-3)
            legalMoves.append(-2)
            legalMoves.append(-1)
            legalMoves.append(1)
            legalMoves.append(2)
            legalMoves.append(3)
            legalMoves.append(4)
            legalMoves.append(5)
            legalMoves.append(6)
            legalMoves.append(7)

            legalMoves.append(-56)
            legalMoves.append(-48)
            legalMoves.append(-40)
            legalMoves.append(-32)
            legalMoves.append(-24)
            legalMoves.append(-16)
            legalMoves.append(-8)
            legalMoves.append(8)
            legalMoves.append(16)
            legalMoves.append(24)
            legalMoves.append(32)
            legalMoves.append(40)
            legalMoves.append(48)
            legalMoves.append(56)

            count = 0
            straightLeft = [-7, -6, -5, -4, -3, -2, -1]
            straightRight = [1, 2, 3, 4, 5, 6, 7]
            straightDown = [8, 16, 24, 32, 40, 48, 56]
            straightUp = [-8, -16, -24, -32, -40, -48, -56]

            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63):
                    if (legalMoves[count] in illegalMoves):
                        illegalMoves.append(legalMoves[count])
                elif (board[boardCounter + legalMoves[count]] in blackList):
                    currentIllegalMove = legalMoves[count]
                    illegalMoves.append(legalMoves[count])
                    # Left
                    if (currentIllegalMove in straightLeft):
                        if (currentIllegalMove == -7):
                            straightLeft = [-6, -5, -4, -3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -6):
                            straightLeft = [-5, -4, -3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -5):
                            straightLeft = [-4, -3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -4):
                            straightLeft = [-3, -2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -3):
                            straightLeft = [-2, -1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -2):
                            straightLeft = [-1]

                            count2 = 0
                            for i in straightLeft:
                                illegalMoves.append(straightLeft[count2])
                                count2 = count2 + 1

                    # Right
                    if (currentIllegalMove in straightRight):
                        if (currentIllegalMove == 1):
                            straightRight = [2, 3, 4, 5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 2):
                            straightRight = [3, 4, 5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 3):
                            straightRight = [4, 5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 4):
                            straightRight = [5, 6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 5):
                            straightRight = [6, 7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 6):
                            straightRight = [7]

                            count2 = 0
                            for i in straightRight:
                                illegalMoves.append(straightRight[count2])
                                count2 = count2 + 1

                    # Down
                    if (currentIllegalMove in straightDown):
                        if (currentIllegalMove == 8):
                            straightDown = [16, 24, 32, 40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 16):
                            straightDown = [24, 32, 40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 24):
                            straightDown = [32, 40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 32):
                            straightDown = [40, 48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 40):
                            straightDown = [48, 56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 48):
                            straightDown = [56]

                            count2 = 0
                            for i in straightDown:
                                illegalMoves.append(straightDown[count2])
                                count2 = count2 + 1

                    # Up
                    if (currentIllegalMove in straightUp):
                        if (currentIllegalMove == -8):
                            straightUp = [-16, -24, -32, -40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -16):
                            straightUp = [-24, -32, -40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -24):
                            straightUp = [-32, -40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -32):
                            straightUp = [-40, -48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -40):
                            straightUp = [-48, -56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -48):
                            straightUp = [-56]

                            count2 = 0
                            for i in straightUp:
                                illegalMoves.append(straightUp[count2])
                                count2 = count2 + 1

                count = count + 1

            count = 0
            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63 or boardCounter + legalMoves[count] < 0):
                    illegalMoves.append(legalMoves[count])
                else:
                    if (board[boardCounter + legalMoves[count]] in blackList):
                        illegalMoves.append(legalMoves[count])
                count = count + 1

            legalMoves = [x for x in legalMoves if x not in illegalMoves]

            tempMoves = [boardCounter]
            count = 0
            for i in legalMoves:
                tempMoves.append(legalMoves[count])
                count = count + 1

            PieceMoves.append(tempMoves)

        if (board[boardCounter] == "♗"):

            illegalMoves = []
            legalMoves = [-63, -54, -45, -36, -27, -18, -9, 9, 18, 27, 36, 45, 54, 63, -49, -42, -35, -28, -21, -14, -7,
                          7, 14, 21, 28, 35, 42, 49]

            count = 0
            diagonalLeftUp = [-63, -54, -45, -36, -27, -18, -9]
            diagonalRightDown = [9, 18, 27, 36, 45, 54, 63]
            diagonalRightUp = [-49, -42, -35, -28, -21, -14, -7]
            diagonalLeftDown = [7, 14, 21, 28, 35, 42, 49]

            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63 or boardCounter + legalMoves[count] < 0):
                    if (legalMoves[count] in illegalMoves):
                        illegalMoves.append(legalMoves[count])
                elif (board[boardCounter + legalMoves[count]] in blackList):
                    currentIllegalMove = legalMoves[count]
                    illegalMoves.append(legalMoves[count])
                    # Side cases
                    if (boardCounter in coloumA):
                        templist = [-63, -54, -45, -36, -27, -18, -9,
                                    7, 14, 21, 28, 35, 42, 49]
                        illegalMoves.extend(templist)
                    elif (boardCounter in coloumB):
                        templist = [-63, -54, -45, -36, -27, -18,
                                    14, 21, 28, 35, 42, 49,
                                    63,
                                    -49]
                        illegalMoves.extend(templist)
                    elif (boardCounter in coloumC):
                        templist = [-63, -54, -45, -36, -27,
                                    21, 28, 35, 42, 49,
                                    63, 54,
                                    -49, -42]
                        illegalMoves.extend(templist)
                    elif (boardCounter in coloumD):
                        templist = [-63, -54, -45, -36,
                                    28, 35, 42, 49,
                                    63, 54, 45,
                                    -49, -42, -35]
                        illegalMoves.extend(templist)
                    elif (boardCounter in coloumE):
                        templist = [-63, -54, -45,
                                    35, 42, 49,
                                    63, 54, 45, 36,
                                    -49, -42, -35, -28]
                        illegalMoves.extend(templist)
                    elif (boardCounter in coloumF):
                        templist = [-63, -54,
                                    42, 49,
                                    63, 54, 45, 36, 27,
                                    -49, -42, -35, -28, -21]
                        illegalMoves.extend(templist)
                    elif (boardCounter in coloumG):
                        templist = [-63,
                                    42,
                                    63, 54, 45, 36, 27, 18,
                                    -49, -42, -35, -28, -21, -14]
                        illegalMoves.extend(templist)
                    elif (boardCounter in coloumH):
                        templist = [63, 54, 45, 36, 27, 18, 9,
                                    -49, -42, -35, -28, -21, -14, -7]
                        illegalMoves.extend(templist)

                    # Left Up
                    if (currentIllegalMove in diagonalLeftUp):
                        if (currentIllegalMove == -54):
                            diagonalLeftUp = [-63]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -45):
                            diagonalLeftUp = [-63, -54]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -36):
                            diagonalLeftUp = [-63, -54, -45]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -27):
                            diagonalLeftUp = [-63, -54, -45, -36]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -18):
                            diagonalLeftUp = [-63, -54, -45, -36, -27]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -9):
                            diagonalLeftUp = [-63, -54, -45, -36, -27, -18]

                            count2 = 0
                            for i in diagonalLeftUp:
                                illegalMoves.append(diagonalLeftUp[count2])
                                count2 = count2 + 1

                    # Right Up
                    if (currentIllegalMove in diagonalRightUp):
                        if (currentIllegalMove == -42):
                            diagonalRightUp = [-49]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -35):
                            diagonalRightUp = [-49, -42]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -28):
                            diagonalRightUp = [-49, -42, -35]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -21):
                            diagonalRightUp = [-49, -42, -35, -28]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -14):
                            diagonalRightUp = [-49, -42, -35, -28, -21]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == -7):
                            diagonalRightUp = [-49, -42, -35, -28, -21, -14]

                            count2 = 0
                            for i in diagonalRightUp:
                                illegalMoves.append(diagonalRightUp[count2])
                                count2 = count2 + 1

                    # Left Down
                    if (currentIllegalMove in diagonalLeftDown):
                        if (currentIllegalMove == 7):
                            diagonalLeftDown = [14, 21, 28, 35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 14):
                            diagonalLeftDown = [21, 28, 35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 21):
                            diagonalLeftDown = [28, 35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 28):
                            diagonalLeftDown = [35, 42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 35):
                            diagonalLeftDown = [42, 49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 42):
                            diagonalLeftDown = [49]

                            count2 = 0
                            for i in diagonalLeftDown:
                                illegalMoves.append(diagonalLeftDown[count2])
                                count2 = count2 + 1

                    # Right Down
                    if (currentIllegalMove in diagonalRightDown):
                        if (currentIllegalMove == 9):
                            diagonalRightDown = [18, 27, 36, 45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 18):
                            diagonalRightDown = [27, 36, 45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 27):
                            diagonalRightDown = [36, 45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 36):
                            diagonalRightDown = [45, 54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 45):
                            diagonalRightDown = [54, 63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                        elif (currentIllegalMove == 54):
                            diagonalRightDown = [63]

                            count2 = 0
                            for i in diagonalRightDown:
                                illegalMoves.append(diagonalRightDown[count2])
                                count2 = count2 + 1

                count = count + 1

            count = 0
            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63 or boardCounter + legalMoves[count] < 0):
                    illegalMoves.append(legalMoves[count])
                else:
                    if (board[boardCounter + legalMoves[count]] in blackList):
                        illegalMoves.append(legalMoves[count])
                count = count + 1

            legalMoves = [x for x in legalMoves if x not in illegalMoves]

            tempMoves = [boardCounter]
            count = 0
            for i in legalMoves:
                tempMoves.append(legalMoves[count])
                count = count + 1

            PieceMoves.append(tempMoves)

        if (board[boardCounter] == "♘"):

            illegalMoves = []
            legalMoves = []

            legalMoves.append(-6)
            legalMoves.append(6)
            legalMoves.append(-10)
            legalMoves.append(10)
            legalMoves.append(-15)
            legalMoves.append(15)
            legalMoves.append(-17)
            legalMoves.append(17)

            count = 0
            knightMoves = [-6, 10, 6, -10, -15, -17, 15, 17]

            rightSide = [6, 7, 14, 15, 22, 23, 31, 30, 39, 38, 47, 46, 55, 54, 62, 63]
            leftSide = [0, 1, 8, 9, 16, 17, 24, 25, 32, 33, 40, 41, 48, 49, 56, 57]

            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63):
                    if (legalMoves[count] in illegalMoves):
                        continue
                    else:
                        illegalMoves.append(legalMoves[count])
                if (boardCounter in rightSide):
                    illegalMoves.append(10)
                    illegalMoves.append(-6)
                if (boardCounter in leftSide):
                    illegalMoves.append(-10)
                    illegalMoves.append(6)
                if (boardCounter <= 15):
                    illegalMoves.append(-15)
                    illegalMoves.append(-17)
                if (boardCounter >= 48):
                    illegalMoves.append(15)
                    illegalMoves.append(17)
            for i in knightMoves:
                if (knightMoves[count] in blackList):
                    illegalMoves.append(legalMoves[count])
                    count = count + 1

            count = 0
            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63 or boardCounter + legalMoves[count] < 0):
                    illegalMoves.append(legalMoves[count])
                else:
                    if (board[boardCounter + legalMoves[count]] in blackList):
                        illegalMoves.append(legalMoves[count])
                count = count + 1

            legalMoves = [x for x in legalMoves if x not in illegalMoves]

            tempMoves = [boardCounter]
            count = 0
            for i in legalMoves:
                tempMoves.append(legalMoves[count])
                count = count + 1

            PieceMoves.append(tempMoves)

        if (board[boardCounter] == "♙"):

            legalMoves = []
            illegalMoves = []

            if (boardCounter in row2):
                if (boardCounter + 8 <= 63):
                    if (board[boardCounter + 8] not in blackList and board[boardCounter + 8] not in whiteList):
                        legalMoves.append(8)
                        if (boardCounter + 16 <= 63):
                            if (board[boardCounter + 16] not in blackList and board[boardCounter + 16] not in whiteList):
                                legalMoves.append(16)

            else:
                if (boardCounter + 8 <= 63):
                    if (board[boardCounter + 8] not in blackList and board[boardCounter + 8] not in whiteList):
                        legalMoves.append(8)

            if (boardCounter + 7 <= 63):
                if (board[boardCounter + 7] in whiteList):
                    legalMoves.append(7)

            if (boardCounter + 9 <= 63):
                if (board[boardCounter + 9] in whiteList):
                    legalMoves.append(9)

            # En passant
            if (enPassant(FEN) != "-"):
                enPassantPosition = enPassant(FEN)
                if (enPassantPosition == "a3"):
                    if (boardCounter == 33):
                        legalMoves.append(7)
                elif (enPassantPosition == "b3"):
                    if (boardCounter == 32):
                        legalMoves.append(9)
                    if (boardCounter == 34):
                        legalMoves.append(7)
                elif (enPassantPosition == "c3"):
                    if (boardCounter == 33):
                        legalMoves.append(9)
                    if (boardCounter == 35):
                        legalMoves.append(7)
                elif (enPassantPosition == "d3"):
                    if (boardCounter == 34):
                        legalMoves.append(9)
                    if (boardCounter == 36):
                        legalMoves.append(7)
                elif (enPassantPosition == "e3"):
                    if (boardCounter == 35):
                        legalMoves.append(8)
                    if (boardCounter == 37):
                        legalMoves.append(7)
                elif (enPassantPosition == "f3"):
                    if (boardCounter == 36):
                        legalMoves.append(9)
                    if (boardCounter == 38):
                        legalMoves.append(7)
                elif (enPassantPosition == "g3"):
                    if (boardCounter == 37):
                        legalMoves.append(9)
                    if (boardCounter == 39):
                        legalMoves.append(7)
                elif (enPassantPosition == "h3"):
                    if (boardCounter == 39):
                        legalMoves.append(9)

            count = 0
            for i in legalMoves:
                if (boardCounter + legalMoves[count] > 63 or boardCounter + legalMoves[count] < 0):
                    illegalMoves.append(legalMoves[count])
                else:
                    if (board[boardCounter + legalMoves[count]] in blackList):
                        illegalMoves.append(legalMoves[count])
                count = count + 1

            legalMoves = [x for x in legalMoves if x not in illegalMoves]

            tempMoves = [boardCounter]
            count = 0
            for i in legalMoves:
                tempMoves.append(legalMoves[count])
                count = count + 1

            PieceMoves.append(tempMoves)

        boardCounter = boardCounter + 1

    return PieceMoves


def whiteLegalMoves(board, whiteList, blackList, intialBoardPos, finalBoardPos, enPassantLast, FEN):
    canCastle = castlingRights(FEN)
    findPiece = board[intialBoardPos]
    legalMoves = []
    illegalMoves = []
    if (findPiece == "♚"):
        legalMoves.append(-9)
        legalMoves.append(-8)
        legalMoves.append(-7)
        legalMoves.append(-1)
        legalMoves.append(9)
        legalMoves.append(8)
        legalMoves.append(7)
        legalMoves.append(1)
        if (intialBoardPos < 55):
            legalMoves.pop(4)
            legalMoves.pop(4)
            legalMoves.pop(4)
        elif (intialBoardPos < 8):
            legalMoves.pop(0)
            legalMoves.pop(0)
            legalMoves.pop(0)

        count = 0
        for i in legalMoves:
            if (intialBoardPos + legalMoves[count] > 63 or intialBoardPos + legalMoves[count] < 0):
                illegalMoves.append(legalMoves[count])
            else:
                if (board[intialBoardPos + legalMoves[count]] in whiteList):
                    illegalMoves.append(legalMoves[count])
            count = count + 1

        legalMoves = [x for x in legalMoves if x not in illegalMoves]

    elif (findPiece == "♛"):
        # diagonal

        illegalMoves = []
        legalMoves = [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 16, 24, 32, 40, 48, 56, -8, -16, -24, -32,
                      -40, -48, -56, -63, -54, -45, -36, -27, -18, -9, 9, 18, 27, 36, 45, 54, 63, -49, -42, -35, -28,
                      -21, -14, -7, 7, 14, 21, 28, 35, 42, 49]

        count = 0
        diagonalLeftUp = [-63, -54, -45, -36, -27, -18, -9]
        diagonalRightDown = [9, 18, 27, 36, 45, 54, 63]
        diagonalRightUp = [-49, -42, -35, -28, -21, -14, -7]
        diagonalLeftDown = [7, 14, 21, 28, 35, 42, 49]

        straightLeft = [-7, -6, -5, -4, -3, -2, -1]
        straightRight = [1, 2, 3, 4, 5, 6, 7]
        straightDown = [8, 16, 24, 32, 40, 48, 56]
        straightUp = [-8, -16, -24, -32, -40, -48, -56]

        for i in legalMoves:
            if (intialBoardPos + legalMoves[count] > 63):
                if (legalMoves[count] in illegalMoves):
                    illegalMoves.append(legalMoves[count])
            elif (board[intialBoardPos + legalMoves[count]] in whiteList):
                currentIllegalMove = legalMoves[count]
                illegalMoves.append(legalMoves[count])
                # Left Up
                if (currentIllegalMove in diagonalLeftUp):
                    if (currentIllegalMove == -54):
                        diagonalLeftUp = [-63]

                        count2 = 0
                        for i in diagonalLeftUp:
                            illegalMoves.append(diagonalLeftUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -45):
                        diagonalLeftUp = [-63, -54]

                        count2 = 0
                        for i in diagonalLeftUp:
                            illegalMoves.append(diagonalLeftUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -36):
                        diagonalLeftUp = [-63, -54, -45]

                        count2 = 0
                        for i in diagonalLeftUp:
                            illegalMoves.append(diagonalLeftUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -27):
                        diagonalLeftUp = [-63, -54, -45, -36]

                        count2 = 0
                        for i in diagonalLeftUp:
                            illegalMoves.append(diagonalLeftUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -18):
                        diagonalLeftUp = [-63, -54, -45, -36, -27]

                        count2 = 0
                        for i in diagonalLeftUp:
                            illegalMoves.append(diagonalLeftUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -9):
                        diagonalLeftUp = [-63, -54, -45, -36, -27, -18]

                        count2 = 0
                        for i in diagonalLeftUp:
                            illegalMoves.append(diagonalLeftUp[count2])
                            count2 = count2 + 1

                # Right Up
                if (currentIllegalMove in diagonalRightUp):
                    if (currentIllegalMove == -42):
                        diagonalRightUp = [-49]

                        count2 = 0
                        for i in diagonalRightUp:
                            illegalMoves.append(diagonalRightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -35):
                        diagonalRightUp = [-49, -42]

                        count2 = 0
                        for i in diagonalRightUp:
                            illegalMoves.append(diagonalRightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -28):
                        diagonalRightUp = [-49, -42, -35]

                        count2 = 0
                        for i in diagonalRightUp:
                            illegalMoves.append(diagonalRightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -21):
                        diagonalRightUp = [-49, -42, -35, -28]

                        count2 = 0
                        for i in diagonalRightUp:
                            illegalMoves.append(diagonalRightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -14):
                        diagonalRightUp = [-49, -42, -35, -28, -21]

                        count2 = 0
                        for i in diagonalRightUp:
                            illegalMoves.append(diagonalRightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -7):
                        diagonalRightUp = [-49, -42, -35, -28, -21, -14]

                        count2 = 0
                        for i in diagonalRightUp:
                            illegalMoves.append(diagonalRightUp[count2])
                            count2 = count2 + 1

                # Left Down
                if (currentIllegalMove in diagonalLeftDown):
                    if (currentIllegalMove == 7):
                        diagonalLeftDown = [14, 21, 28, 35, 42, 49]

                        count2 = 0
                        for i in diagonalLeftDown:
                            illegalMoves.append(diagonalLeftDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 14):
                        diagonalLeftDown = [21, 28, 35, 42, 49]

                        count2 = 0
                        for i in diagonalLeftDown:
                            illegalMoves.append(diagonalLeftDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 21):
                        diagonalLeftDown = [28, 35, 42, 49]

                        count2 = 0
                        for i in diagonalLeftDown:
                            illegalMoves.append(diagonalLeftDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 28):
                        diagonalLeftDown = [35, 42, 49]

                        count2 = 0
                        for i in diagonalLeftDown:
                            illegalMoves.append(diagonalLeftDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 35):
                        diagonalLeftDown = [42, 49]

                        count2 = 0
                        for i in diagonalLeftDown:
                            illegalMoves.append(diagonalLeftDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 42):
                        diagonalLeftDown = [49]

                        count2 = 0
                        for i in diagonalLeftDown:
                            illegalMoves.append(diagonalLeftDown[count2])
                            count2 = count2 + 1

                # Right Down
                if (currentIllegalMove in diagonalRightDown):
                    if (currentIllegalMove == 9):
                        diagonalRightDown = [18, 27, 36, 45, 54, 63]

                        count2 = 0
                        for i in diagonalRightDown:
                            illegalMoves.append(diagonalRightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 18):
                        diagonalRightDown = [27, 36, 45, 54, 63]

                        count2 = 0
                        for i in diagonalRightDown:
                            illegalMoves.append(diagonalRightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 27):
                        diagonalRightDown = [36, 45, 54, 63]

                        count2 = 0
                        for i in diagonalRightDown:
                            illegalMoves.append(diagonalRightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 36):
                        diagonalRightDown = [45, 54, 63]

                        count2 = 0
                        for i in diagonalRightDown:
                            illegalMoves.append(diagonalRightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 45):
                        diagonalRightDown = [54, 63]

                        count2 = 0
                        for i in diagonalRightDown:
                            illegalMoves.append(diagonalRightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 54):
                        diagonalRightDown = [63]

                        count2 = 0
                        for i in diagonalRightDown:
                            illegalMoves.append(diagonalRightDown[count2])
                            count2 = count2 + 1

                # Left
                if (currentIllegalMove in straightLeft):
                    if (currentIllegalMove == -7):
                        straightLeft = [-6, -5, -4, -3, -2, -1]

                        count2 = 0
                        for i in straightLeft:
                            illegalMoves.append(straightLeft[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -6):
                        straightLeft = [-5, -4, -3, -2, -1]

                        count2 = 0
                        for i in straightLeft:
                            illegalMoves.append(straightLeft[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -5):
                        straightLeft = [-4, -3, -2, -1]

                        count2 = 0
                        for i in straightLeft:
                            illegalMoves.append(straightLeft[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -4):
                        straightLeft = [-3, -2, -1]

                        count2 = 0
                        for i in straightLeft:
                            illegalMoves.append(straightLeft[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -3):
                        straightLeft = [-2, -1]

                        count2 = 0
                        for i in straightLeft:
                            illegalMoves.append(straightLeft[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -2):
                        straightLeft = [-1]

                        count2 = 0
                        for i in straightLeft:
                            illegalMoves.append(straightLeft[count2])
                            count2 = count2 + 1

                # Right
                if (currentIllegalMove in straightRight):
                    if (currentIllegalMove == 1):
                        straightRight = [2, 3, 4, 5, 6, 7]

                        count2 = 0
                        for i in straightRight:
                            illegalMoves.append(straightRight[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 2):
                        straightRight = [3, 4, 5, 6, 7]

                        count2 = 0
                        for i in straightRight:
                            illegalMoves.append(straightRight[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 3):
                        straightRight = [4, 5, 6, 7]

                        count2 = 0
                        for i in straightRight:
                            illegalMoves.append(straightRight[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 4):
                        straightRight = [5, 6, 7]

                        count2 = 0
                        for i in straightRight:
                            illegalMoves.append(straightRight[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 5):
                        straightRight = [6, 7]

                        count2 = 0
                        for i in straightRight:
                            illegalMoves.append(straightRight[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 6):
                        straightRight = [7]

                        count2 = 0
                        for i in straightRight:
                            illegalMoves.append(straightRight[count2])
                            count2 = count2 + 1

                # Down
                if (currentIllegalMove in straightDown):
                    if (currentIllegalMove == 8):
                        straightDown = [16, 24, 32, 40, 48, 56]

                        count2 = 0
                        for i in straightDown:
                            illegalMoves.append(straightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 16):
                        straightDown = [24, 32, 40, 48, 56]

                        count2 = 0
                        for i in straightDown:
                            illegalMoves.append(straightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 24):
                        straightDown = [32, 40, 48, 56]

                        count2 = 0
                        for i in straightDown:
                            illegalMoves.append(straightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 32):
                        straightDown = [40, 48, 56]

                        count2 = 0
                        for i in straightDown:
                            illegalMoves.append(straightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 40):
                        straightDown = [48, 56]

                        count2 = 0
                        for i in straightDown:
                            illegalMoves.append(straightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 48):
                        straightDown = [56]

                        count2 = 0
                        for i in straightDown:
                            illegalMoves.append(straightDown[count2])
                            count2 = count2 + 1

                # Up
                if (currentIllegalMove in straightUp):
                    if (currentIllegalMove == -8):
                        straightUp = [-16, -24, -32, -40, -48, -56]

                        count2 = 0
                        for i in straightUp:
                            illegalMoves.append(straightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -16):
                        straightUp = [-24, -32, -40, -48, -56]

                        count2 = 0
                        for i in straightUp:
                            illegalMoves.append(straightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -24):
                        straightUp = [-32, -40, -48, -56]

                        count2 = 0
                        for i in straightUp:
                            illegalMoves.append(straightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -32):
                        straightUp = [-40, -48, -56]

                        count2 = 0
                        for i in straightUp:
                            illegalMoves.append(straightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -40):
                        straightUp = [-48, -56]

                        count2 = 0
                        for i in straightUp:
                            illegalMoves.append(straightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -48):
                        straightUp = [-56]

                        count2 = 0
                        for i in straightUp:
                            illegalMoves.append(straightUp[count2])
                            count2 = count2 + 1

            count = count + 1

        count = 0
        for i in legalMoves:
            if (intialBoardPos + legalMoves[count] > 63 or intialBoardPos + legalMoves[count] < 0):
                illegalMoves.append(legalMoves[count])
            else:
                if (board[intialBoardPos + legalMoves[count]] in whiteList):
                    illegalMoves.append(legalMoves[count])
            count = count + 1

        legalMoves = [x for x in legalMoves if x not in illegalMoves]

    elif (findPiece == "♜"):

        legalMoves = [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 16, 24, 32, 40, 48, 56, -8, -16, -24, -32, -40, -48, -56]

        count = 0
        straightLeft = [-7, -6, -5, -4, -3, -2, -1]
        straightRight = [1, 2, 3, 4, 5, 6, 7]
        straightUp = [8, 16, 24, 32, 40, 48, 56]
        straightDown = [-8, -16, -24, -32, -40, -48, -56]

        for i in legalMoves:
            if (intialBoardPos + legalMoves[count] > 63):
                if (legalMoves[count] in illegalMoves):
                    continue
                else:
                    illegalMoves.append(legalMoves[count])
            elif (board[intialBoardPos + legalMoves[count]] in whiteList):
                currentIllegalMove = legalMoves[count]
                illegalMoves.append(legalMoves[count])
                #Left
                if (currentIllegalMove in straightLeft):
                    if (currentIllegalMove == -7):
                        straightLeft.pop(6)
                        straightLeft.pop(5)
                        straightLeft.pop(4)
                        straightLeft.pop(3)
                        straightLeft.pop(2)
                        straightLeft.pop(1)

                        count2 = 0
                        for i in straightLeft:
                            illegalMoves.append(straightLeft[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -6):
                        straightLeft.pop(6)
                        straightLeft.pop(5)
                        straightLeft.pop(4)
                        straightLeft.pop(3)
                        straightLeft.pop(2)

                        count2 = 0
                        for i in straightLeft:
                            illegalMoves.append(straightLeft[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -5):
                        straightLeft.pop(6)
                        straightLeft.pop(5)
                        straightLeft.pop(4)
                        straightLeft.pop(3)

                        count2 = 0
                        for i in straightLeft:
                            illegalMoves.append(straightLeft[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -4):
                        straightLeft.pop(6)
                        straightLeft.pop(5)
                        straightLeft.pop(4)

                        count2 = 0
                        for i in straightLeft:
                            illegalMoves.append(straightLeft[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -3):
                        straightLeft.pop(6)
                        straightLeft.pop(5)

                        count2 = 0
                        for i in straightLeft:
                            illegalMoves.append(straightLeft[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -2):
                        straightLeft.pop(6)

                        count2 = 0
                        for i in straightLeft:
                            illegalMoves.append(straightLeft[count2])
                            count2 = count2 + 1

                # Right
                if (currentIllegalMove in straightRight):
                    if (currentIllegalMove == 1):
                        straightRight.pop(6)
                        straightRight.pop(5)
                        straightRight.pop(4)
                        straightRight.pop(3)
                        straightRight.pop(2)
                        straightRight.pop(1)

                        count2 = 0
                        for i in straightRight:
                            illegalMoves.append(straightRight[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 2):
                        straightRight.pop(6)
                        straightRight.pop(5)
                        straightRight.pop(4)
                        straightRight.pop(3)
                        straightRight.pop(2)

                        count2 = 0
                        for i in straightRight:
                            illegalMoves.append(straightRight[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 3):
                        straightRight.pop(6)
                        straightRight.pop(5)
                        straightRight.pop(4)
                        straightRight.pop(3)

                        count2 = 0
                        for i in straightRight:
                            illegalMoves.append(straightRight[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 4):
                        straightRight.pop(6)
                        straightRight.pop(5)
                        straightRight.pop(4)

                        count2 = 0
                        for i in straightRight:
                            illegalMoves.append(straightRight[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 5):
                        straightRight.pop(6)
                        straightRight.pop(5)

                        count2 = 0
                        for i in straightRight:
                            illegalMoves.append(straightRight[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 6):
                        straightRight.pop(6)

                        count2 = 0
                        for i in straightRight:
                            illegalMoves.append(straightRight[count2])
                            count2 = count2 + 1

                # Down
                if (currentIllegalMove in straightDown):
                    if (currentIllegalMove == 8):
                        straightDown.pop(6)
                        straightDown.pop(5)
                        straightDown.pop(4)
                        straightDown.pop(3)
                        straightDown.pop(2)
                        straightDown.pop(1)

                        count2 = 0
                        for i in straightDown:
                            illegalMoves.append(straightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 16):
                        straightDown.pop(6)
                        straightDown.pop(5)
                        straightDown.pop(4)
                        straightDown.pop(3)
                        straightDown.pop(2)

                        count2 = 0
                        for i in straightDown:
                            illegalMoves.append(straightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 24):
                        straightDown.pop(6)
                        straightDown.pop(5)
                        straightDown.pop(4)
                        straightDown.pop(3)

                        count2 = 0
                        for i in straightDown:
                            illegalMoves.append(straightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 32):
                        straightDown.pop(6)
                        straightDown.pop(5)
                        straightDown.pop(4)

                        count2 = 0
                        for i in straightDown:
                            illegalMoves.append(straightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 40):
                        straightDown.pop(6)
                        straightDown.pop(5)

                        count2 = 0
                        for i in straightDown:
                            illegalMoves.append(straightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 48):
                        straightDown.pop(6)

                        count2 = 0
                        for i in straightDown:
                            illegalMoves.append(straightDown[count2])
                            count2 = count2 + 1

                # Up
                if (currentIllegalMove in straightUp):
                    if (currentIllegalMove == -8):
                        straightUp.pop(6)
                        straightUp.pop(5)
                        straightUp.pop(4)
                        straightUp.pop(3)
                        straightUp.pop(2)
                        straightUp.pop(1)

                        count2 = 0
                        for i in straightUp:
                            illegalMoves.append(straightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -16):
                        straightUp.pop(6)
                        straightUp.pop(5)
                        straightUp.pop(4)
                        straightUp.pop(3)
                        straightUp.pop(2)

                        count2 = 0
                        for i in straightUp:
                            illegalMoves.append(straightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -24):
                        straightUp.pop(6)
                        straightUp.pop(5)
                        straightUp.pop(4)
                        straightUp.pop(3)

                        count2 = 0
                        for i in straightUp:
                            illegalMoves.append(straightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -32):
                        straightUp.pop(6)
                        straightUp.pop(5)
                        straightUp.pop(4)

                        count2 = 0
                        for i in straightUp:
                            illegalMoves.append(straightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -40):
                        straightUp.pop(6)
                        straightUp.pop(5)

                        count2 = 0
                        for i in straightUp:
                            illegalMoves.append(straightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -48):
                        straightUp.pop(6)

                        count2 = 0
                        for i in straightUp:
                            illegalMoves.append(straightUp[count2])
                            count2 = count2 + 1

            count = count + 1

        legalMoves = [x for x in legalMoves if x not in illegalMoves]

    elif (findPiece == "♝"):
        illegalMoves = []
        legalMoves = [-63, -54, -45, -36, -27, -18, -9, 9, 18, 27, 36, 45, 54, 63, -49, -42, -35, -28, -21, -14, -7,
                      7, 14, 21, 28, 35, 42, 49]

        count = 0
        diagonalLeftUp = [-63, -54, -45, -36, -27, -18, -9]
        diagonalRightDown = [9, 18, 27, 36, 45, 54, 63]
        diagonalRightUp = [-49, -42, -35, -28, -21, -14, -7]
        diagonalLeftDown = [7, 14, 21, 28, 35, 42, 49]

        for i in legalMoves:
            if (intialBoardPos + legalMoves[count] > 63 or intialBoardPos + legalMoves[count] < 0):
                if (legalMoves[count] in illegalMoves):
                    illegalMoves.append(legalMoves[count])
            elif (board[intialBoardPos + legalMoves[count]] in whiteList):
                currentIllegalMove = legalMoves[count]
                illegalMoves.append(legalMoves[count])
                # Left Up
                if (currentIllegalMove in diagonalLeftUp):
                    if (currentIllegalMove == -54):
                        diagonalLeftUp = [-63]

                        count2 = 0
                        for i in diagonalLeftUp:
                            illegalMoves.append(diagonalLeftUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -45):
                        diagonalLeftUp = [-63, -54]

                        count2 = 0
                        for i in diagonalLeftUp:
                            illegalMoves.append(diagonalLeftUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -36):
                        diagonalLeftUp = [-63, -54, -45]

                        count2 = 0
                        for i in diagonalLeftUp:
                            illegalMoves.append(diagonalLeftUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -27):
                        diagonalLeftUp = [-63, -54, -45, -36]

                        count2 = 0
                        for i in diagonalLeftUp:
                            illegalMoves.append(diagonalLeftUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -18):
                        diagonalLeftUp = [-63, -54, -45, -36, -27]

                        count2 = 0
                        for i in diagonalLeftUp:
                            illegalMoves.append(diagonalLeftUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -9):
                        diagonalLeftUp = [-63, -54, -45, -36, -27, -18]

                        count2 = 0
                        for i in diagonalLeftUp:
                            illegalMoves.append(diagonalLeftUp[count2])
                            count2 = count2 + 1

                # Right Up
                if (currentIllegalMove in diagonalRightUp):
                    if (currentIllegalMove == -42):
                        diagonalRightUp = [-49]

                        count2 = 0
                        for i in diagonalRightUp:
                            illegalMoves.append(diagonalRightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -35):
                        diagonalRightUp = [-49, -42]

                        count2 = 0
                        for i in diagonalRightUp:
                            illegalMoves.append(diagonalRightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -28):
                        diagonalRightUp = [-49, -42, -35]

                        count2 = 0
                        for i in diagonalRightUp:
                            illegalMoves.append(diagonalRightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -21):
                        diagonalRightUp = [-49, -42, -35, -28]

                        count2 = 0
                        for i in diagonalRightUp:
                            illegalMoves.append(diagonalRightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -14):
                        diagonalRightUp = [-49, -42, -35, -28, -21]

                        count2 = 0
                        for i in diagonalRightUp:
                            illegalMoves.append(diagonalRightUp[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == -7):
                        diagonalRightUp = [-49, -42, -35, -28, -21, -14]

                        count2 = 0
                        for i in diagonalRightUp:
                            illegalMoves.append(diagonalRightUp[count2])
                            count2 = count2 + 1

                # Left Down
                if (currentIllegalMove in diagonalLeftDown):
                    if (currentIllegalMove == 7):
                        diagonalLeftDown = [14, 21, 28, 35, 42, 49]

                        count2 = 0
                        for i in diagonalLeftDown:
                            illegalMoves.append(diagonalLeftDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 14):
                        diagonalLeftDown = [21, 28, 35, 42, 49]

                        count2 = 0
                        for i in diagonalLeftDown:
                            illegalMoves.append(diagonalLeftDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 21):
                        diagonalLeftDown = [28, 35, 42, 49]

                        count2 = 0
                        for i in diagonalLeftDown:
                            illegalMoves.append(diagonalLeftDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 28):
                        diagonalLeftDown = [35, 42, 49]

                        count2 = 0
                        for i in diagonalLeftDown:
                            illegalMoves.append(diagonalLeftDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 35):
                        diagonalLeftDown = [42, 49]

                        count2 = 0
                        for i in diagonalLeftDown:
                            illegalMoves.append(diagonalLeftDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 42):
                        diagonalLeftDown = [49]

                        count2 = 0
                        for i in diagonalLeftDown:
                            illegalMoves.append(diagonalLeftDown[count2])
                            count2 = count2 + 1

                # Right Down
                if (currentIllegalMove in diagonalRightDown):
                    if (currentIllegalMove == 9):
                        diagonalRightDown = [18, 27, 36, 45, 54, 63]

                        count2 = 0
                        for i in diagonalRightDown:
                            illegalMoves.append(diagonalRightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 18):
                        diagonalRightDown = [27, 36, 45, 54, 63]

                        count2 = 0
                        for i in diagonalRightDown:
                            illegalMoves.append(diagonalRightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 27):
                        diagonalRightDown = [36, 45, 54, 63]

                        count2 = 0
                        for i in diagonalRightDown:
                            illegalMoves.append(diagonalRightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 36):
                        diagonalRightDown = [45, 54, 63]

                        count2 = 0
                        for i in diagonalRightDown:
                            illegalMoves.append(diagonalRightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 45):
                        diagonalRightDown = [54, 63]

                        count2 = 0
                        for i in diagonalRightDown:
                            illegalMoves.append(diagonalRightDown[count2])
                            count2 = count2 + 1

                    elif (currentIllegalMove == 54):
                        diagonalRightDown = [63]

                        count2 = 0
                        for i in diagonalRightDown:
                            illegalMoves.append(diagonalRightDown[count2])
                            count2 = count2 + 1

            count = count + 1

        count = 0
        for i in legalMoves:
            if (intialBoardPos + legalMoves[count] > 63 or intialBoardPos + legalMoves[count] < 0):
                illegalMoves.append(legalMoves[count])
            else:
                if (board[intialBoardPos + legalMoves[count]] in whiteList):
                    illegalMoves.append(legalMoves[count])
            count = count + 1

        legalMoves = [x for x in legalMoves if x not in illegalMoves]

    elif (findPiece == "♞"):
        legalMoves.append(-6)
        legalMoves.append(6)
        legalMoves.append(-10)
        legalMoves.append(10)
        legalMoves.append(-15)
        legalMoves.append(15)
        legalMoves.append(-17)
        legalMoves.append(17)

        count = 0
        knightMoves = [-6, 10, 6, -1, -15, -17, 15, 17]

        for i in legalMoves:
            if (intialBoardPos + legalMoves[count] > 63):
                if (legalMoves[count] in illegalMoves):
                    continue
                else:
                    illegalMoves.append(legalMoves[count])
        for i in knightMoves:
            if (knightMoves[count] in whiteList):
                illegalMoves.append(legalMoves[count])
                count = count + 1

        legalMoves = [x for x in legalMoves if x not in illegalMoves]

    elif (findPiece == "♟"):
        if (intialBoardPos > 47 and intialBoardPos < 56):
            legalMoves.append(-8)
            legalMoves.append(-16)
            legalMoves.append(-7)
            legalMoves.append(-9)
        #En passant
        elif (enPassant(FEN) != "-"):
            legalMoves.append(-8)
            legalMoves.append(-7)
            legalMoves.append(-9)
        else:
            legalMoves.append(-8)
            legalMoves.append(-7)
            legalMoves.append(-9)
    else:
        return -1

    if ((finalBoardPos - intialBoardPos) in legalMoves):
        if (findPiece == "♟" and (finalBoardPos - intialBoardPos) == -16):
            enPassantPos = finalBoardPos + 8
            if (enPassantPos == 40):
                enPassantLast = "a3"
                return enPassantLast
            elif (enPassantPos == 41):
                enPassantLast = "b3"
                return enPassantLast
            elif (enPassantPos == 42):
                enPassantLast = "c3"
                return enPassantLast
            elif (enPassantPos == 43):
                enPassantLast = "d3"
                return enPassantLast
            elif (enPassantPos == 44):
                enPassantLast = "e3"
                return enPassantLast
            elif (enPassantPos == 45):
                enPassantLast = "f3"
                return enPassantLast
            elif (enPassantPos == 46):
                enPassantLast = "g3"
                return enPassantLast
            elif (enPassantPos == 47):
                enPassantLast = "h3"
                return enPassantLast

        return 1
    else:
        return -1

def getFutureBoardStates(tempBoard, whiteList, blackList, states, tempFEN):
    boardStates = []
    while (states > 0):
        blackMoves = blackThreats(tempBoard, blackList, blackThreats, tempFEN)
        count = 0
        for i in blackMoves:
            piece = blackMoves[count]
            moveCount = len(piece) - 1
            count = count + 1
            if (moveCount > 0):
                intialBoardPos = piece[0]
                piece.pop(0)
                count2 = 0
                while moveCount > 0:
                    moveCount = moveCount - 1
                    FENToBoard(tempFEN, tempBoard)
                    finalBoardPos = intialBoardPos + piece[count2]
                    Piece = tempBoard[intialBoardPos]
                    tempBoard[intialBoardPos] = "　"
                    capture = 0
                    if (tempBoard[finalBoardPos] in blackList):
                        if (tempBoard[finalBoardPos] == "♖"):
                            whiteCaptureList.append("♖")
                            capture = 5
                        elif (tempBoard[finalBoardPos] == "♘"):
                            whiteCaptureList.append("♘")
                            capture = 3
                        elif (tempBoard[finalBoardPos] == "♗"):
                            whiteCaptureList.append("♗")
                            capture = 3
                        elif (tempBoard[finalBoardPos] == "♕"):
                            whiteCaptureList.append("♕")
                            capture = 9
                        elif (tempBoard[finalBoardPos] == "♔"):
                            whiteCaptureList.append("♔")
                            capture = 999
                        elif (tempBoard[finalBoardPos] == "♙"):
                            whiteCaptureList.append("♙")
                            capture = 1

                    elif (tempBoard[finalBoardPos] in whiteList):
                        if (tempBoard[finalBoardPos] == "♜"):
                            blackCaptureList.append("♜")
                            capture = 5
                        elif (tempBoard[finalBoardPos] == "♞"):
                            blackCaptureList.append("♞")
                            capture = 3
                        elif (tempBoard[finalBoardPos] == "♝"):
                            blackCaptureList.append("♝")
                            capture = 3
                        elif (tempBoard[finalBoardPos] == "♛"):
                            blackCaptureList.append("♛")
                            capture = 9
                        elif (tempBoard[finalBoardPos] == "♚"):
                            blackCaptureList.append("♚")
                            capture = 999
                        elif (tempBoard[finalBoardPos] == "♟"):
                            blackCaptureList.append("♟")
                            capture = 1

                    tempBoard[finalBoardPos] = Piece
                    tempFEN = boardToFEN(tempFEN, tempBoard, capture, enPassantLast)
                    boardStates.append(tempFEN)
                    count2 = count2 + 1

        states = states - 1

    count = 0
    for i in boardStates:
        tempFEN = boardStates[count]
        print("Board State " + str(count))
        print(tempFEN)
        FENToBoard(tempFEN, tempBoard)
        displayBoard(board, whiteCaptureList, blackCaptureList, whiteCaptureCounter)
        count = count + 1
        FENToBoard(FEN, tempBoard)



def calcBoardSpace(pieceLetter, pieceNumber):
    pieceCount = 0
    pieceLetter = pieceLetter.lower()
    if (int(pieceNumber) > 0 and int(pieceNumber) < 9):
        pieceCount = (8 * (int(pieceNumber) - 1)) - 1
    else:
        return -1
    if (pieceLetter == "a"):
        pieceCount = pieceCount + 8
    elif (pieceLetter == "b"):
        pieceCount = pieceCount + 7
    elif (pieceLetter == "c"):
        pieceCount = pieceCount + 6
    elif (pieceLetter == "d"):
        pieceCount = pieceCount + 5
    elif (pieceLetter == "e"):
        pieceCount = pieceCount + 4
    elif (pieceLetter == "f"):
        pieceCount = pieceCount + 3
    elif (pieceLetter == "g"):
        pieceCount = pieceCount + 2
    elif (pieceLetter == "h"):
        pieceCount = pieceCount + 1
    else:
        return -1

    pieceCount = 63 - pieceCount
    return pieceCount

def makeMove(board, intialBoardPos, finalBoardPos):
    Piece = board[intialBoardPos]
    board[intialBoardPos] = "　"
    capture = 0
    if (board[finalBoardPos] in blackList):
        if (board[finalBoardPos] == "♖"):
            whiteCaptureList.append("♖")
            capture = 5
        elif (board[finalBoardPos] == "♘"):
            whiteCaptureList.append("♘")
            capture = 3
        elif (board[finalBoardPos] == "♗"):
            whiteCaptureList.append("♗")
            capture = 3
        elif (board[finalBoardPos] == "♕"):
            whiteCaptureList.append("♕")
            capture = 9
        elif (board[finalBoardPos] == "♔"):
            whiteCaptureList.append("♔")
            capture = 999
        elif (board[finalBoardPos] == "♙"):
            whiteCaptureList.append("♙")
            capture = 1

    elif (board[finalBoardPos] in whiteList):
        if (board[finalBoardPos] == "♜"):
            blackCaptureList.append("♜")
            capture = 5
        elif (board[finalBoardPos] == "♞"):
            blackCaptureList.append("♞")
            capture = 3
        elif (board[finalBoardPos] == "♝"):
            blackCaptureList.append("♝")
            capture = 3
        elif (board[finalBoardPos] == "♛"):
            blackCaptureList.append("♛")
            capture = 9
        elif (board[finalBoardPos] == "♚"):
            blackCaptureList.append("♚")
            capture = 999
        elif (board[finalBoardPos] == "♟"):
            blackCaptureList.append("♟")
            capture = 1

    board[finalBoardPos] = Piece
    return capture

def playerMove(FEN, board, whiteList, blackList, enPassantLast, whiteCaptureList, whiteCaptureCounter):
    Piece = []
    Move = []
    intialBoardPos = -1
    finalBoardPos = -1
    enPassantLast = "-"
    while (len(Piece) != 2):
        playerMovePiece = input("Move Piece: ")
        for letter in playerMovePiece:
            Piece.append(letter)

        if (len(Piece) == 2):
            if (Piece[1].isnumeric()):
                pieceNumber = Piece[1]
                pieceLetter = Piece[0]
                intialBoardPos = calcBoardSpace(pieceLetter, pieceNumber)
            elif (Piece[0].isnumeric()):
                pieceNumber = Piece[0]
                pieceLetter = Piece[1]
                intialBoardPos = calcBoardSpace(pieceLetter, pieceNumber)
            else:
                print("Not Valid")
                Piece = []
        else:
            print("Not Valid")
            Piece = []

        if (board[intialBoardPos] in whiteList and intialBoardPos != -1):
            continue
        else:
            print("Not Valid")
            Piece = []

    Piece = []
    while (len(Piece) != 2):
        playerMove = input("Move To: ")
        for letter in playerMove:
            Piece.append(letter)

        if (len(Piece) == 2):
            if (Piece[1].isnumeric()):
                pieceNumber = Piece[1]
                pieceLetter = Piece[0]
                finalBoardPos = calcBoardSpace(pieceLetter, pieceNumber)
            elif (Piece[0].isnumeric()):
                pieceNumber = Piece[0]
                pieceLetter = Piece[1]
                finalBoardPos = calcBoardSpace(pieceLetter, pieceNumber)
            else:
                print("Not Valid")
                Piece = []
        else:
            print("Not Valid")
            Piece = []

        if (finalBoardPos != -1):
            if (whiteLegalMoves(board, whiteList, blackList, intialBoardPos, finalBoardPos, enPassantLast, FEN) == 1):
                capture = makeMove(board, intialBoardPos, finalBoardPos)
                boardToFEN(FEN, board, capture, enPassantLast)
                whiteCaptureCounter = whiteCaptureCounter + capture
                displayBoard(board, whiteCaptureList, blackCaptureList, whiteCaptureCounter)
            elif (whiteLegalMoves(board, whiteList, blackList, intialBoardPos, finalBoardPos, enPassantLast, FEN) == -1):
                print("Not Valid")
                Piece = []
            else:
                enPassantLast = whiteLegalMoves(board, whiteList, blackList, intialBoardPos, finalBoardPos, enPassantLast, FEN)
                capture = makeMove(board, intialBoardPos, finalBoardPos)
                boardToFEN(FEN, board, capture, enPassantLast)
                whiteCaptureCounter = whiteCaptureCounter + capture
                displayBoard(board, whiteCaptureList, blackCaptureList, whiteCaptureCounter)
        else:
            print("Not Valid")
            Piece = []

def blackMove(blackMoves, board, enPassantLast, FEN, whiteList):
    pieceCount = 0
    moveCount = 0
    pieceMoved = False

    whiteAnalysis = 0
    blackAnalysis = 0

    while (pieceMoved == False):

        captureList = []
        count = 0
        for i in blackMoves:
            piece = blackMoves[count]
            count2 = 0
            for i in piece:
                initialBoardPos = piece[0]
                finalBoardPos = piece[0] + piece[count2]
                if (board[finalBoardPos] in whiteList):
                    if (board[finalBoardPos] == "♜"):
                        captureList.append([initialBoardPos, finalBoardPos, 5])
                    elif (board[finalBoardPos] == "♞"):
                        captureList.append([initialBoardPos, finalBoardPos, 3])
                    elif (board[finalBoardPos] == "♝"):
                        captureList.append([initialBoardPos, finalBoardPos, 3])
                    elif (board[finalBoardPos] == "♛"):
                        captureList.append([initialBoardPos, finalBoardPos, 9])
                    elif (board[finalBoardPos] == "♚"):
                        captureList.append([initialBoardPos, finalBoardPos, 999])
                    elif (board[finalBoardPos] == "♟"):
                        captureList.append([initialBoardPos, finalBoardPos, 1])
                count2 = count2 + 1
            count = count + 1

            if (len(captureList) > 0):
                for i in captureList:
                    sortedCaptureList = sorted(captureList, key=lambda l: l[2], reverse=True)
                move = sortedCaptureList[0]
                initialBoardPos = move[0]
                finalBoardPos = move[1]
                capture = makeMove(board, initialBoardPos, finalBoardPos)
                pieceMoved = True
                return capture

        pieceCount = len(blackMoves)
        pieceCount = pieceCount - 1

        piece = random.randint(0, pieceCount)

        pieceMoves = blackMoves[piece]

        moveCount = len(pieceMoves)
        moveCount = moveCount - 1

        moveCount = moveCount - 1

        if (moveCount >= 1):
            move = random.randint(1, moveCount)
            initialBoardPos = pieceMoves[0]
            finalBoardPos = pieceMoves[0] + pieceMoves[move]
            capture = makeMove(board, initialBoardPos, finalBoardPos)
            pieceMoved = True
            return capture

states = 1

print(FEN)
while (gameGoing == True):
    FENToBoard(FEN, board)
    displayBoard(board, whiteCaptureList, blackCaptureList, whiteCaptureCounter)
    playerMove(FEN, board, whiteList, blackList, enPassantLast, whiteCaptureList, whiteCaptureCounter)
    tempBoard = board
    tempFEN = FEN
    getFutureBoardStates(tempBoard, whiteList, blackList, states, tempFEN)
    blackMoves = blackThreats(board, blackList, blackThreats, FEN)
    whiteMoves = whiteThreats(board, whiteList)
    capture = blackMove(blackMoves, board, enPassantLast, FEN, whiteList)
    FEN = boardToFEN(FEN, board, capture, enPassantLast)