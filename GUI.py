
'''
Im going so insane with this project,
but im learning a ton. 

Im going to try writting some documentation 
to understand my mess

TODO: 
- [ ]


Classes: 
    Piece --- use as a blueprint for other pieces classes

        Attributes: 
            location (a tuple with x and y cordintaes)
            isWhite (Boolean)

        Methods: 
            possibleMoves -- returns an array of tuples of where the piece con move. 
            IMPLEMENTED BY SUBCLASES
            However the basic premise is the following. Taking to account a pieces
            graph, I calculate each square and add it to a list if 
            its empty or can be captured
    
            
    Pawn -- some special properties that differ from other pieces

        Attributes: 
                location (a tuple with x and y cordintaes)
                isWhite (Boolean)
                value (int, the value of the piece)
                type (ascii character)
                Direction (either 1 or -1, is determined by isWhite)
                hasMoved (Boolean, for double moves. Also takes into account were the peice is thrown)
        
        Methods:
            possibleMovesAttacking ---> List of tuples
                The diagonals that the pawn can capture, but not move, to. 
                I just fixed this. This method is only rarely called, for stuff like castling
                and check.

            possibleMoves ---> List of tuples (or an ocassional string for en Pessant)

    Knight -im so proud of this one :'), its so beautiful and simple. 
        Attributes: 
                location (a tuple with x and y cordintaes)
                isWhite (Boolean)
                value (int, the value of the piece)
                type (ascii character)
            
        
        Methods:
            possibleMoves --> List of tuples
    
    Bishop - also clean af
     Attributes: 
                location (a tuple with x and y cordintaes)
                isWhite (Boolean)
                value (int, the value of the piece) 3.5 here
                type (ascii character)
            
        
        Methods:
            possibleMoves --> List of tuples. It checks the 4 diagonals and stops checking
            if it encountures an a blocked piece, it stops the search.
    
    King 
      Attributes: 
                location (a tuple with x and y cordintaes)
                isWhite (Boolean)
                value (int, the value of the piece) 1000 here
                type (ascii character)
                hasMoved (boolean, used for castling logic)

            
        
        Methods:
            attackingSquares --> List of tuples.
                Normal squares it can move to

            canCastle -> returns a list of "0-0", "0-0-0" or an empty list depnding if it can castle
                First, it uses board.attackingSquares(self.isWhite) to get the squares of the enemy that are attacked



            possibleMoves(self, board): --> sums both of the methods and returns the result
    
    
    Queen
        Attributes: 
                location (a tuple with x and y cordintaes)
                isWhite (Boolean)
                value (int, the value of the piece) 1000 here
                type (ascii character)
    

            
        
        Methods:
            Possible Moves --> List of tuples.
                Literally copied and paste rook and bishop code

    Rook
       Attributes: 
                location (a tuple with x and y cordintaes)
                isWhite (Boolean)
                value (int, the value of the piece) 1000 here
                type (ascii character)
                hasMoved -- used for castling
    

            
        
        Methods:
            Possible Moves --> List of tuples.
                Similar to bishops code, but for columns and rows. 


    
    class Board(): 
    def __init__(self, pieces, doesWhitePlay):
        Attributes:
            pieces --- array of piece objects
            doesWhitePlay -- boolean
            enPassant -- an array with a boolean at 0 and a tuple at 1. 
                The logic is the following. Every time a pawn double moves, its square will get stored
                and enPessant[0] == True. Hence, when checking for possible moves, it might be detected as
                capturable. 
                However, in the move function, at th start enPessant[0] will be put to false, 
                making the rule work as intendead.

            self.checkMate = [False, None] ---> The idea is that checkMate[1] will store who gave checkmate
            self.staleMate = False
    
        Methods
            move(self, piece, square)
                1. It iters if a piece is in the square. If it is, its most certenly and enemy piece, 
                and the piece is removed. ---> I find this logic valid

                2. Now it checks if the piece is a pawn
                    if hasMoved is false, then the variable is changed to True
                        if square is doubleMove, square is changed to the corresponding square
                        Also, the self.enPessant array is changed and 0 is true and 1 the square

                    elif, coronation --> The pawn is removed and a queen is placed there instead
                
                    elif square == "enPassant"
                        It moved the pawn to the appropiate squares and removed the captured pawn

                3.5 Elif, the piece is either a king or rook
                    if hasMoved == False, then hasMoved = True

                    if square is 0-0:
                        square is changed to the lcoation of the king
                        the rook is searched and place accordingly

                4. It changed the location of the piece to square

                5. It changed the doesWhitePlay Boolean

            draw(self)
                I belief this works beautifully. 
            
            checkOrStailMate: --> Either "CHECKMATE" OR "STAILMATE"
                This method works to assist the possibleMoves of the board class.
                If no moves are possible, it is called
            
            def possibleMoves(self):
                FIRST, it has a legalMoves boolean, which checks is turned to True if 
                there exist atleast one legal move

                possible is a dictionary, the pieces are the key, the value is an array of tuples (the moves)
                FIRST it iters through every single piece
                if the piece colour is the color that moves:
                    jesus christ, here is the issue. 
                    For every single move in piece.possibleMoves:
                        it will create a deep copy of the board 
                        find the piece in the deep copy
                        move the move, 
                        and if its not in check, i.e, the move is legal
                        it will append it. 



        

    

            
        


'''
import sailMate

myBoard = sailMate.FEN("kbK5/pp6/1P6/8/8/8/8/R7", True)

myBoard.draw()
bestMove = sailMate.bestMove(myBoard, 3)
print(f"Best move: {bestMove}")

for piece in myBoard.pieces:
    print(f"{piece.ascii} at {piece.location} with value {piece.value}")


