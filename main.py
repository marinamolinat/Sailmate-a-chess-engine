#Okay, this is going to be extremely slowwww and messy, but learning all the proper ways of doing an engine is going to cost me too many brain cells. 

#The idea is such: Every piece will be represented as an object and have a map atribute
#The atribute will the map of possible moves of the piece. This atribute will be updated as the piece moves
#a function will be call to check that no other piece is in that square, or that the move is indead possible. It will return possible moves for that piece

#For now, that the idea


class Piece():

    def __init__(self, location):
        self.value = None
        self.map = []
        self.location = location 



class Pawn(Piece):
    def __init__(self, location):
        super().__init__(location)   
        self.value = 1
        self.hasmoved = False
        self.map = [(0, 1)]
        self.map_notmoved = map.append((0, 2))






p1 = Pawn((0, 1))

pieces = {Pawn: (0, 1)}

print(p1.value)
def pawn_possible_moves(pawn): 
    pawn.map
    if not pawn.hasmoved:
        pass
        
    
       
    




def evaluate(board):
    pass #this will evaluate the board