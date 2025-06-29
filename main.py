import copy

class Piece():

    def __init__(self, location, isWhite):
        self.location = location 
        self.isWhite = isWhite


    def possibleMoves(self, pieces, board):
        raise NotImplementedError("Must be implemented by the subclass") 
    
   



class Pawn(Piece):
    def __init__(self, location, isWhite):
        super().__init__(location, isWhite)  

        self.value = 1

        if (location[1] == 1 and isWhite) or (location[1] == 6 and not isWhite):
            self.hasMoved = False
        else:
            self.hasMoved = True

        if isWhite: 
            self.type = "♟"
            self.direction = 1
        else: 
            self.type = "♙"
            self.direction = -1
    
    def possibleMovesAttacking(self, board):  #only squares that are attacked
        possible = []

         #Scan diagonal capturing, towards right
        move = (self.location[0] + 1 , self.location[1] + self.direction)
        if board.scan(move, self.isWhite) == -1:
            possible.append(move)
        
        #Scan diagonal capturing, towards left
        move = (self.location[0] - 1 , self.location[1] + self.direction)
        if board.scan(move, self.isWhite) == -1:
            possible.append(move)
    
        return possible

    

    def possibleMoves(self, board): 

        possible = [] 


        
        #Scan y+1
        move = ((self.location[0]), (self.location[1] + self.direction))
        if board.scan(move, self.isWhite) == 1:
            possible.append(move)

        #Scan y+2
        if not self.hasMoved:
            move = ((self.location[0]), (self.location[1] + self.direction*2))
            if board.scan(move, self.isWhite) == 1 and board.scan((move[0], move[1] + self.direction * -1), self.isWhite) == 1:
                possible.append("doubleMove") #This is done to account for en Passant

        possible += self.possibleMovesAttacking(board)



        #En passant
        if (board.enPassant[0] == True) and (board.enPassant[1] == (self.location[0] + 1, self.location[1]) or board.enPassant[1] == (self.location[0] -1, self.location[1])):
            possible.append("enPassant")


    
        return possible
            


class Knight(Piece): 
    def __init__(self, location, isWhite):
        super().__init__(location, isWhite)   
        self.value = 3
        if isWhite: 
            self.type = "♞"
        else: 
            self.type = "♘"   
    def possibleMoves(self, board):
        possible = []
        map = [(2, 1),(-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        for i in map:
            move = ((self.location[0] + i[0]), (self.location[1] + i[1]))
            conditional = board.scan(move, self.isWhite)
            if conditional == 1 or conditional == -1:
                possible.append(move)

        return possible
                 



class Bishop(Piece):
    def __init__(self, location, isWhite):
        super().__init__(location, isWhite)
        self.value = 3.5
        if isWhite: 
            self.type = "♝"
        else: 
            self.type = "♗" 
    def possibleMoves(self, board):
        possible = [] 

        for i in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for j in range(1, 7):
                move =  ((self.location[0] + (j*i[0])), (self.location[1] + (j * i[1])))
    
    
                conditional = board.scan(move, self.isWhite)
                if conditional == 1:
                    possible.append(move)
                elif conditional == -1:
                    possible.append(move)
                    break
                else:
                    break

        return possible

        

class King(Piece):
    def __init__(self, location, isWhite):
        super().__init__(location, isWhite)
        self.value = 100000
        if isWhite: 
            self.type = "♚"
            self.hasMoved = False if location == (4, 0) else True
        else: 
            self.type = "♔" 
            self.hasMoved = False if location == (4, 7) else True
  
    
    def attackingSquares(self, board):
        #Really shitty king that doesnt understand that can put itself into checkmate

        squares = []
        map = [(0, 1),(0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0)]
        for i in map:
            move = ((self.location[0] + i[0]), (self.location[1] + i[1]))
            conditional = board.scan(move, self.isWhite)
            if conditional == 1 or conditional == -1:
                squares.append(move)
        return squares

    #Currently, this is so disguting. I swear ill fix it soon enough
    def canCastle(self, board):
       
        castles = []
        squares = board.attackingSquares(self.isWhite)

        if self.hasMoved or self.location in squares:
            return castles
        
        y = 0 if self.isWhite else 7

        importantSquares = [  #This contain the squares that must be empty as well as the rook square [0] is for shory castling, [1] for long

        [[(5, y), (6, y)], (7, y), "0-0"],
        [[(3, y), (2, y), (1, y)], (0, y), "0-0-0"]

        ]
    

        
        #Loop through both types of castling (i.e 2 times)
        for castlingType in importantSquares:
            break_outer_loop = False  

            #Will make sure square is empty, if its not, it will try long castling
            for square in castlingType[0]:
                if board.scan(square, self.isWhite) != 1 or square in squares:
                    break_outer_loop = True
                    break
            if break_outer_loop:
                continue
            
            
            #Will make sure the correspondant rook exists
            for p in board.pieces:
                if p.location == castlingType[1] and p.__class__.__name__ == "Rook":
                    if not p.hasMoved:
                        castles.append(castlingType[2])
                    
        return castles
                        

    def possibleMoves(self, board):
        possible = []
        possible += self.attackingSquares(board)
        possible += self.canCastle(board)
        return possible


        
class Queen(Piece): 
    def __init__(self, location, isWhite):
        self.value = 9
        super().__init__(location, isWhite)
        if isWhite: 
            self.type = "♛"
        else: 
            self.type = "♕"
    def possibleMoves(self, board):
        # This just borrows code from the rook and bishop

        possible = []

        #Bishop code
        for i in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for j in range(1, 8):
                move =  ((self.location[0] + (j*i[0])), (self.location[1] + (j * i[1])))
   
                conditional = board.scan(move, self.isWhite)
                if conditional == 1:
                    possible.append(move)
                elif conditional == -1:
                    possible.append(move)
                    break
                else:
                    break

        #Rook code
        for i in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            for j in range(1, 8):
                move =  ((self.location[0] + (j*i[0])), (self.location[1] + (j * i[1])))
                conditional = board.scan(move, self.isWhite)
                if conditional == 1:
                    possible.append(move)
                elif conditional == -1:
                    possible.append(move)
                    break
                else:
                    break
        return possible



class Rook(Piece): 
    def __init__(self, location, isWhite):
        super().__init__(location, isWhite)   
        self.value = 5
        if isWhite: 
            self.type = "♜"
        else: 
            self.type = "♖"
        self.hasMoved = False
    def possibleMoves(self, board):       
        possible = [] 
        for i in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            for j in range(1, 8):
                move =  ((self.location[0] + (j*i[0])), (self.location[1] + (j * i[1])))
                conditional = board.scan(move, self.isWhite)
                if conditional == 1:
                    possible.append(move)
                elif conditional == -1:
                    possible.append(move)
                    break
                else:
                    break
        
        return possible        
                
        



        
##Might do a board class, instead of an array of pieces

class Board(): 
    def __init__(self, pieces, doesWhitePlay):
        self.pieces = pieces
        self.doesWhitePlay = doesWhitePlay
        self.enPassant = [False, None] #Will store the pawn that can currently be captured ith enPessant
        self.checkMate = False 

    def move(self, piece, square):
        self.enPassant[0] = False

        #Check if a piece has been captured, and removes it in the case
        for p in self.pieces:
            if p.location == square:
                self.pieces.remove(p)

        if piece.__class__.__name__ == "Pawn":
        
            if not piece.hasMoved:
                piece.hasMoved = True

                if square == "doubleMove":
                    square = (piece.location[0], piece.location[1] + (piece.direction * 2))
                    self.enPassant[1] = square
                    self.enPassant[0] = True

            elif square[1] == 0 or square[1] == 7:
                new = Queen(square, piece.isWhite)

                for p in self.pieces:
                    if p.location == piece.location and p.isWhite == piece.isWhite and p.__class__ == piece.__class__:
                        self.pieces.remove(p)
                
                self.pieces.append(new)

            elif square == "enPassant":

                #The square to which the pawn will move to
                square = (self.enPassant[1][0], self.enPassant[1][1] + piece.direction)

                #Removing the other pawn
                for p in self.pieces:
                    if p.location == self.enPassant[1]:
                        self.pieces.remove(p)

        elif  piece.__class__.__name__ == "King" or  piece.__class__.__name__ == "Rook": 
            if piece.hasMoved == False:
                piece.hasMoved = True  

            if square == "0-0":
                y = 0 if piece.isWhite else 7

                square = (6, y)

                #Search for rook and place it accordingly
                for p in self.pieces:
                    if p.location == (7, y):
                        p.location = (5, y)

            elif square == "0-0-0":
                y = 0 if piece.isWhite else 7

                square = (2, y)

                #Search for rook and place it accordingly
                for p in self.pieces:
                    if p.location == (0, y):
                        p.location = (3, y)



                
        self.doesWhitePlay = not self.doesWhitePlay
        piece.location = square


    
             

    def draw(self): 
        board = []
        for i in range(8):
            board.append([])
            for j in range(8):
                board[i].append("[ ]")
                
        for piece in self.pieces:
            board[piece.location[0]][piece.location[1]] = f"[{piece.type}]"
        

        #Now, draw:
        for i in range(7, -1, -1):
            stringy = ""
            for j in range(8):
                stringy += board[j][i]
            print(f"{i} " + stringy)
        print("   0  1  2  3  4  5  6  7 ")

    
    def checkOrStailMate(self):
        if self.isInCheck(self.doesWhitePlay):
            return "CHECKMATE"
        else:
            return "STALEMATE"
    
    #Return a dictionary with the piece object, and a list where such piece can move
    def possibleMoves(self):
        legalMoves = False

        possible = {}

        for piece in self.pieces:
            moves =  []
            if piece.isWhite == self.doesWhitePlay:
                for move in piece.possibleMoves(self):
                    pieces_copy = copy.deepcopy(self.pieces)
                    board_copy = Board(pieces_copy, self.doesWhitePlay)
                    pCopy = None
                   

                    #I need to find the piece in the deep copy :/
                    for p in pieces_copy:
                        if p.location == piece.location:
                            pCopy = p
                             

                    board_copy.move(pCopy, move)

                    if not board_copy.isInCheck(self.doesWhitePlay):
                        moves.append(move)
                        legalMoves = True

            possible[piece] = moves
    
        if not legalMoves:
            return self.checkOrStailMate() 
                   
        return possible
    
    
    #Scan if a square is empty and possible in the board. 
    # 1: its empty; -2: its occupied by a piece of the same color; -1: occupied by an enemy piece
    def scan(self, square, isWhite):

        #Scan if a square is in bounds
        if not (square[0] <= 7 and square[0] >= 0 and square[1] <= 7 and square[1] >= 0):
            return 0

        #Scan if the square is empty
        for piece in self.pieces: 
            if piece.location == square:
                if isWhite == piece.isWhite:
                    return -2
                else: 
                    return -1                

   
   
   
        return 1    
    
    #Will check if that the king cannot be captured with a given move 
    def isInCheck(self, isWhite):
        king = None
        attackedSquares = []
        for p in self.pieces:
            if  p.__class__.__name__ == "King" and p.isWhite == isWhite:
                king = p
                break
        
        attackedSquares = self.attackingSquares(isWhite)

        if king.location in attackedSquares:
            return True
        else:
            return False
        
    def attackingSquares(self, isWhite):
        attackedSquares = []

        for p in self.pieces:
            if not p.isWhite == isWhite:
                    if p.__class__.__name__ == "Pawn":
                        attackedSquares += p.possibleMovesAttacking(self)
                    elif p.__class__.__name__ == "King":
                        attackedSquares += p.attackingSquares(self)
                    else:
                        attackedSquares += p.possibleMoves(self)
        return attackedSquares


                

                


        

            


        




#A function that will take a fen as input, and create a respective board
def FEN(fen, doesWhitePlay):
    x = 0
    y = 7
    pieces = []
    for char in fen: 
        is_int = False
        if char.isupper():
            char = char.lower()
            isWhite = True
        else: 
            isWhite = False

    

        match char:
            case 'p':
                piece = Pawn((x, y), isWhite)
                x += 1
            case 'q':
                piece = Queen((x, y), isWhite) 
                x += 1
            case 'k':
                piece = King((x, y), isWhite)
                x +=1
            case 'n':
                piece = Knight((x, y), isWhite)
                x += 1
            case 'r':
                piece = Rook((x, y), isWhite)
                x += 1
            case 'b':
                piece = Bishop((x, y), isWhite)
                x += 1
            case '/':
                is_int = True
                y -= 1
                x = 0 

            case _:  # It has to be an int
                is_int = True
                char = int(char)
                x += char

        if not is_int:
            pieces.append(piece)

    return Board(pieces, doesWhitePlay)
    


myBoard = FEN("4k3/pppppppp/1n6/4r3/1K6/7r/2r5/8", True)
myBoard.draw()
possible = myBoard.possibleMoves()
print("Possible Moves: ", possible)



#Simple eval function lol
def evaluate(board):
    eval = 0
    
    for piece in board.pieces:
        if piece.isWhite:
            eval += piece.value
        else:
            eval -= piece.value

    return eval



#MINIMAX
def minimax(board, depth):


    if depth == 0:
        return evaluate(board)
    
    if board.doesWhitePlay:
        best = -1000

        for piece in board.possiblePieces():
            for move in piece.possibleMoves(board):
                
                pieces_copy = copy.deepcopy(board.pieces)
                board_copy = Board(pieces_copy, board.doesWhitePlay)
                for p in pieces_copy:
                    if p.location == piece.location and p.isWhite == piece.isWhite and p.__class__ == piece.__class__:
                        new_piece = p
                
                board_copy.move(new_piece, move)
                score = minimax(board_copy, depth-1)
                if score > best:
                    best = score    


              

    else:
        best = 1000

        for piece in board.possiblePieces():
            for move in piece.possibleMoves(board):
                pieces_copy = copy.deepcopy(board.pieces)
                board_copy = Board(pieces_copy, board.doesWhitePlay)
                for p in pieces_copy:
                    if p.location == piece.location and p.isWhite == piece.isWhite and p.__class__ == piece.__class__:
                        new_piece = p
                
                board_copy.move(new_piece, move)
                score = minimax(board_copy, depth-1)
                if score < best:
                    best = score    

            
                    

    return best




                
   
        
    







