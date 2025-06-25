#Okay, this is going to be extremely slowwww and messy, but learning all the proper ways of doing an engine is going to cost me too many brain cells. 

#The idea is such: Every piece will be represented as an object and have a map atribute
#The atribute will the map of possible moves of the piece. This atribute will be updated as the piece moves
#a function will be call to check that no other piece is in that square, or that the move is indead possible. It will return possible moves for that piece

#For now, that the idea

#Possibly use vector math 


class Piece():

    def __init__(self, location, isWhite):
        self.value = None
        self.map = []
        self.location = location 
        self.isWhite = isWhite



class Pawn(Piece):
    def __init__(self, location, isWhite):
        super().__init__(location, isWhite)   
        self.value = 1
        self.hasMoved = False
        self.map = [(0, 1)]
        
##Array of all pieces
p1 = Pawn((0, 1), True)
blackp = Pawn((1, 2), False)
pieces = [p1, blackp]




#Check if a sqaure is empty and possible in the board
def check(square, isWhite):


    #Check if a square is in bounds
    if not (square[0] <= 8 and square[0] >= 0 and square[1] <= 8 and square[1] >= 0):
        return 0



    #Check if the square is empty
    for piece in pieces: 
        if piece.location == square:
            if isWhite == piece.isWhite:
                return -2
            else: 
                return -1                

    return 1







def pawn_possible_moves(pawn): 
    #Going to hardcode some stuff, as this is a pawn. Might fix it later
    possible = [] 
    

    #Check y+1
    if check((pawn.location[0], pawn.location[1] + 1), pawn.isWhite) == 1:
        possible.append((pawn.location[0], pawn.location[1] + 1))
    
    #if pawn hasnt moved, check y+2
    if not pawn.hasMoved: 
        if check((pawn.location[0], pawn.location[1] + 2), pawn.isWhite) == 1:
            possible.append((pawn.location[0], pawn.location[1] + 2))
    

    #Check diagonal capturing, towards right
    if check((pawn.location[0] + 1 , pawn.location[1] + 1), pawn.isWhite) == -1:
        possible.append((pawn.location[0] + 1 , pawn.location[1] + 1))
    
     #Check diagonal capturing, towards right
    if check((pawn.location[0] - 1 , pawn.location[1] - 1), pawn.isWhite) == -1:
        possible.append((pawn.location[0] + -1, pawn.location[1] + 1))
    
    return possible

print(pawn_possible_moves(p1))





    
    


def evaluate(board):
    pass #this will evaluate the board