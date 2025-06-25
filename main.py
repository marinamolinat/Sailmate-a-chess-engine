#Okay, this is going to be extremely slowwww and messy, but learning all the proper ways of doing an engine is going to cost me too many brain cells. 

##I really wanna draw a board :/. I wasn't thinking of doing a gui but I think it would be easier if I could vizualise


#Possibly use vector math 


class Piece():

    def __init__(self, location, isWhite):
        self.value = None
        self.location = location 
        self.isWhite = isWhite



class Pawn(Piece):
    def __init__(self, location, isWhite):
        super().__init__(location, isWhite)   
        self.value = 1

        if location[1] == 1 and isWhite or location[1] == 6 and  not isWhite:
            self.hasMoved = False
        else:
            self.hasMoved = True



class Rook(Piece): 
    def __init__(self, location, isWhite):
        super().__init__(location, isWhite)   
        self.value = 1



        
##Array of all pieces

p1 = Pawn((0, 1), True)
blackp = Pawn((1, 2), False)
pieces = [p1, blackp]






#Check if a sqaure is empty and possible in the board
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

print(pawn_possible_moves(p1))
print(pawn_possible_moves(blackp))







    
    


def evaluate(board):
    pass #this will evaluate the board