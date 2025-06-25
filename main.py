#Okay, this is going to be extremely slowwww and messy, but learning all the proper ways of doing an engine is going to cost me too many brain cells. 

##I really wanna draw a board :/. I wasn't thinking of doing a gui but I think it would be easier if I could vizualise


#Possibly use vector math 

# Also, ♟ is going to be white cause it makes more sense for me, taking into acccount my use of darkmode. I might change this later.


class Piece():

    def __init__(self, location, isWhite):
        self.value = None
        self.location = location 
        self.isWhite = isWhite
        self.type = None



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


class Knight(Piece): 
    def __init__(self, location, isWhite):
        super().__init__(location, isWhite)   
        if isWhite: 
            self.type = "♞"
        else: 
            self.type = "♘"      



class Bishop(Piece):
    def __init__(self, location, isWhite):
        super().__init__(location, isWhite)
        if isWhite: 
            self.type = "♝"
        else: 
            self.type = "♗" 

class King(Piece):
     def __init__(self, location, isWhite):
        super().__init__(location, isWhite)
        if isWhite: 
            self.type = "♚"
        else: 
            self.type = "♔"      

class Queen(Piece): 
    def __init__(self, location, isWhite):
        super().__init__(location, isWhite)
        if isWhite: 
            self.type = "♛"
        else: 
            self.type = "♕"



class Rook(Piece): 
    def __init__(self, location, isWhite):
        super().__init__(location, isWhite)   
        self.value = 5
        if isWhite: 
            self.type = "♜"
        else: 
            self.type = "♖"
        



        
##Array of all pieces

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








#Check if a square is empty and possible in the board. 
# 1: its empty; -2: its occupied by a piece of the same color; -1: occupied by an enemy piece
def check(square, isWhite):


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



#Knight moves, quite more elegant than others
def knight_possible_moves(knight):
    possible = []
    map = [(2, 1),(-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
    for i in map:
        move = ((knight.location[0] + i[0]), (knight.location[1] + i[1]))
        conditional = check(move, knight.isWhite)
        if conditional == 1 or conditional == -1:
            possible.append(move)

    return possible


#Really shitty king that doesnt understand that it can be captured
def king_possible_moves(king):
    possible = []
    map = [(0, 1),(0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0)]
    for i in map:
        move = ((king.location[0] + i[0]), (king.location[1] + i[1]))
        conditional = check(move, king.isWhite)
        if conditional == 1 or conditional == -1:
            possible.append(move)

    return possible



def bishop_possible_moves(bishop):
    possible = [] 


    #checking right up
    for i in range(1, 7):
        move =  ((bishop.location[0] + i), (bishop.location[1]+ i))
        conditional = check(move, bishop.isWhite)
        if conditional == 1:
            possible.append(move)
        elif conditional == -1:
            possible.append(move)
            break
        else:
            break
        
    #checking left up
    for i in range(1, 7):
        move =  ((bishop.location[0] - i), bishop.location[1] + i)
        conditional = check(move, bishop.isWhite)
        if conditional == 1:
            possible.append(move)
        elif conditional == -1:
            possible.append(move)
            break
        else:
            break   
   
        
    #checking right down
    for i in range(1, 7):
        move =  ((bishop.location[0] + i), (bishop.location[1] - i))
        conditional = check(move, bishop.isWhite)
        if conditional == 1:
            possible.append(move)
        elif conditional == -1:
            possible.append(move)
            break
        else:
            break
   
        
     #checking left down
    for i in range(1, 7):
        move =  ((bishop.location[0] -i ), (bishop.location[1] - i))
        conditional = check(move, bishop.isWhite)
        if conditional == 1:
            possible.append(move)
        elif conditional == -1:
            possible.append(move)
            break
        else:
            break
    
    return possible        
            
    
            
       
            



def rook_possible_moves(rook):
    #I dont think this is the cleanest or most optimized, but it works :)
    possible = [] 


    #checking x direction, right
    for i in range(1, 8):
        move =  ((rook.location[0] + i), rook.location[1])
        conditional = check(move, rook.isWhite)
        if conditional == 1:
            possible.append(move)
        elif conditional == -1:
            possible.append(move)
            break
        else:
            break
        
    #checking x direction, right 
    for i in range(1, 8):
        move =  ((rook.location[0] - i), rook.location[1])
        conditional = check(move, rook.isWhite)
        if conditional == 1:
            possible.append(move)
        elif conditional == -1:
            possible.append(move)
            break
        else:
            break   
   
        
    #checking y direction, up 
    for i in range(1, 8):
        move =  ((rook.location[0]), rook.location[1] + i)
        conditional = check(move, rook.isWhite)
        if conditional == 1:
            possible.append(move)
        elif conditional == -1:
            possible.append(move)
            break
        else:
            break
   
        
     #checking y direction, down
    for i in range(1, 8):
        move =  ((rook.location[0]), rook.location[1] - i)
        conditional = check(move, rook.isWhite)
        if conditional == 1:
            possible.append(move)
        elif conditional == -1:
            possible.append(move)
            break
        else:
            break
    
    return possible        
            
    
            
        
        
def queen_possible_moves(queen):
    possible = bishop_possible_moves(queen) + rook_possible_moves(queen)
    return possible    




def pawn_possible_moves(pawn): 
    #Going to hardcode some stuff, as this is a pawn. Might fix it later
    possible = [] 

    direction = 1

    if not pawn.isWhite:
        direction = -1


    #Check y+1
    if check((pawn.location[0], pawn.location[1] + direction), pawn.isWhite) == 1:
        possible.append((pawn.location[0], pawn.location[1] + direction))
    
    #if pawn hasnt moved, check y+2
    if not pawn.hasMoved: 
        if check((pawn.location[0], pawn.location[1] + direction*2), pawn.isWhite) == 1:
            possible.append((pawn.location[0], pawn.location[1] + direction*2))
    

    #Check diagonal capturing, towards right
    if check((pawn.location[0] + 1 , pawn.location[1] + direction), pawn.isWhite) == -1:
        possible.append((pawn.location[0] + 1 , pawn.location[1] + direction))
    
     #Check diagonal capturing, towards left
    if check((pawn.location[0] - 1 , pawn.location[1] + direction), pawn.isWhite) == -1:
        possible.append((pawn.location[0] + - 1, pawn.location[1] + direction))
    
    return possible



def draw(pieces): 
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append("[ ]")
            
    for piece in pieces:
        board[piece.location[0]][piece.location[1]] = f"[{piece.type}]"
    

    #Now, draw:
    print("   0  1  2  3  4  5  6  7 ")
    for i in range(7, -1, -1):
        stringy = ""
        for j in range(8):
            stringy += board[j][i]
        print(f"{i} " + stringy)
    
            
            



draw(pieces)


print(len(queen_possible_moves(queen)))
print(queen_possible_moves(queen))
                    
print(len(queen_possible_moves(queen2)))
print(queen_possible_moves(queen2))
                    
    









    


def evaluate(board):
    pass #this will evaluate the board