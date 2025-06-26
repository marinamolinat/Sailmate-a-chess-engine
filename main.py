#Okay, this is going to be extremely slowwww and messy, but learning all the proper ways of doing an engine is going to cost me too many brain cells. 

##I really wanna draw a board :/. I wasn't thinking of doing a gui but I think it would be easier if I could vizualise


#Possibly use vector math 

# Also, ♟ is going to be white cause it makes more sense for me, taking into acccount my use of darkmode. I might change this later.
import random
import time

class Piece():

    def __init__(self, location, isWhite):
        self.value = None
        self.location = location 
        self.isWhite = isWhite
        self.type = None
        
    def possible_moves(self, pieces, board):
        raise NotImplementedError("Must be implemented by the subclass") 
    
   
       



class Pawn(Piece):
    def __init__(self, location, isWhite):
        super().__init__(location, isWhite)   
        self.value = 1

        if location[1] == 1 and isWhite or location[1] == 6 and not isWhite:
            self.hasMoved = False
        else:
            self.hasMoved = True

        if isWhite: 
            self.type = "♟"
        else: 
            self.type = "♙"
    def possible_moves(self, board):
        possible = [] 
        direction = 1

        if not self.isWhite:
            direction = -1
        
        #Check y+1
        move = ((self.location[0]), (self.location[1] + direction))
        if board.check(move, self.isWhite) == 1:
            possible.append(move)

        #Check y+2
        if not self.hasMoved:
            move = ((self.location[0]), (self.location[1] + direction*2))
            if board.check(move, self.isWhite) == 1:
                possible.append(move)
    
        

        #Check diagonal capturing, towards right
        move = (self.location[0] + 1 , self.location[1] + direction)
        if board.check(move, self.isWhite) == -1:
            possible.append(move)
        
        #Check diagonal capturing, towards left
        move = (self.location[0] - 1 , self.location[1] + direction)
        if board.check(move, self.isWhite) == -1:
            possible.append(move)
    
        return possible
            


class Knight(Piece): 
    def __init__(self, location, isWhite):
        super().__init__(location, isWhite)   
        if isWhite: 
            self.type = "♞"
        else: 
            self.type = "♘"   
    def possible_moves(self, board):
        possible = []
        map = [(2, 1),(-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        for i in map:
            move = ((self.location[0] + i[0]), (self.location[1] + i[1]))
            conditional = board.check(move, self.isWhite)
            if conditional == 1 or conditional == -1:
                possible.append(move)

        return possible
                 



class Bishop(Piece):
    def __init__(self, location, isWhite):
        super().__init__(location, isWhite)
        if isWhite: 
            self.type = "♝"
        else: 
            self.type = "♗" 
    def possible_moves(self, board):
        possible = [] 

        for i in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for j in range(1, 7):
                move =  ((self.location[0] + (j*i[0])), (self.location[1] + (j * i[1])))
    
                conditional = board.check(move, self.isWhite)
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
        if isWhite: 
            self.type = "♚"
        else: 
            self.type = "♔"      
    def possible_moves(self, board):
        #Really shitty king that doesnt understand that can put itself into checkmate

        possible = []
        map = [(0, 1),(0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0)]
        for i in map:
            move = ((self.location[0] + i[0]), (self.location[1] + i[1]))
            conditional = board.check(move, self.isWhite)
            if conditional == 1 or conditional == -1:
                possible.append(move)

        return possible

class Queen(Piece): 
    def __init__(self, location, isWhite):
        super().__init__(location, isWhite)
        if isWhite: 
            self.type = "♛"
        else: 
            self.type = "♕"
    def possible_moves(self, board):
        # This just borrows code from the rook and bishop

        possible = []

        #Bishop code
        for i in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for j in range(1, 8):
                move =  ((self.location[0] + (j*i[0])), (self.location[1] + (j * i[1])))
   
                conditional = board.check(move, self.isWhite)
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
                conditional = board.check(move, self.isWhite)
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
    def possible_moves(self, board):       
        possible = [] 
        for i in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            for j in range(1, 8):
                move =  ((self.location[0] + (j*i[0])), (self.location[1] + (j * i[1])))
                conditional = board.check(move, self.isWhite)
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
        self.pieces = pieces
    
    def move(self, piece, square):
        if piece.__class__.__name__ == "Pawn":
            if not piece.hasMoved:
                piece.hasMoved = True

        self.doesWhitePlay = not self.doesWhitePlay

        #Check if a piece has been captured, and removes it in the case
        for p in self.pieces:
            if p.location == square:
                self.pieces.remove(p)

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
        
    
    #Return a list of all pieces that can be moved? (All black or white pieces for now)
    def possiblePieces(self):

        possible = []

        for piece in self.pieces:
            if piece.isWhite == self.doesWhitePlay:
                possible.append(piece)
        
        return possible
    
    #Check if a square is empty and possible in the board. 
    # 1: its empty; -2: its occupied by a piece of the same color; -1: occupied by an enemy piece
    def check(self, square, isWhite):

        #Check if a square is in bounds
        if not (square[0] <= 7 and square[0] >= 0 and square[1] <= 7 and square[1] >= 0):
            return 0

        #Check if the square is empty
        for piece in pieces: 
            if piece.location == square:
                if isWhite == piece.isWhite:
                    return -2
                else: 
                    return -1                

        return 1    


p1 = Pawn((0, 1), True)
bp1 = Pawn((1, 2), False)
bp2 = Pawn((3, 5), False)
p2 = Pawn((2, 4), True)
p3 = Pawn((4, 4), True)

r1 = Rook((1, 5), True)
k1 = Knight((5, 6), False)
king = King((7, 7), False)
b1 = Bishop((5, 2), True)
b2 = Bishop((2, 6), False)
queen = Queen((3, 1), True)
queen2 = Queen((0, 6), False)


pieces = [p1, bp1, bp2, p2, p3, r1, k1, king, b1, b2, queen, queen2]



        


myBoard = Board(pieces, True)

myBoard.draw()

for i in range(100):
    time.sleep(1)
    piece = random.choice(myBoard.possiblePieces())

    print(f"The piece choosen is: {piece}")
    try:
        move = random.choice(piece.possible_moves(myBoard))
        print(piece.possible_moves(myBoard))
        print(move)
        myBoard.move(piece, move)
    except IndexError:
        print("Chose a piece with no moves")
    myBoard.draw()








            
            



    

def evaluate(board):
    pass #To come..