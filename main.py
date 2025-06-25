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
pieces = [p1, bp1, bp2, p2, p3, r1]








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





def rook_possible_moves(rook):
    #I dont think this is the cleanest or most optimized, but it works :)
    possible = [] 

    #checking x direction, right
    for i in range(1, 8): 
        if check(((rook.location[0] + i), rook.location[1]), rook.isWhite) == 1:
            possible.append(((rook.location[0] + i), rook.location[1]))
        elif check(((rook.location[0] + i), rook.location[1]), rook.isWhite) == -1:
            possible.append(((rook.location[0] + i), rook.location[1]))
            break
        else:
            break
        
    #checking x direction, right    
    for i in range(1, 8): 
        if check(((rook.location[0] - i), rook.location[1]), rook.isWhite) == 1:
            possible.append(((rook.location[0] - i), rook.location[1]))
        elif check(((rook.location[0] - i), rook.location[1]), rook.isWhite) == -1:
            possible.append(((rook.location[0] - i), rook.location[1]))
            break
        else:
            break
        
    #checking y direction, up 
    for i in range(1, 8): 
        if check((rook.location[0], (rook.location[1] + i)), rook.isWhite) == 1:
            possible.append(((rook.location[0]), (rook.location[1] + i)))
        elif check(((rook.location[0]), rook.location[1] + i), rook.isWhite) == -1:
            possible.append(((rook.location[0]), (rook.location[1] + i)))
            break
        else:
            break
        
     #checking y direction, down
    for i in range(1, 8): 
        if check(((rook.location[0]), rook.location[1] - i), rook.isWhite) == 1:
            possible.append(((rook.location[0]), (rook.location[1] - i)))
        elif check(((rook.location[0]), rook.location[1] - i), rook.isWhite) == -1:
            possible.append(((rook.location[0]), (rook.location[1] - i)))
            break
        else:
            break
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
    for i in range(7, -1, -1):
        stringy = ""
        for j in range(8):
            stringy += board[j][i]
        print(f"{i} " + stringy)
    
            
            



draw(pieces)


                    

    


print(f"White pawn possible moves: {pawn_possible_moves(p1)}")
print(f"Black pawn possible moves: {pawn_possible_moves(bp1)}")
print(f"Bp2: {pawn_possible_moves(bp2)}")
print(f"p2: {pawn_possible_moves(p2)}")
print(f"p3 {pawn_possible_moves(p3)}")
print(f"r1 {rook_possible_moves(r1)}")
print(f"len {len(rook_possible_moves(r1))}")







    


def evaluate(board):
    pass #this will evaluate the board