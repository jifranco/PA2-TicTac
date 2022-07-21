from board import Board
#player class
class Player:
    #constructor for the class
    def __init__(self,name,sign):
        self.name = name
        self.sign = sign

    #defining the accessor methods
    def get_sign(self):
        return self.sign

    def get_name(self):
        return self.name

    def choose(self,b):
        #dictionary to store the values of cell
        s = {"A1":0 , "A2" :3,"A3" :6 ,"B1":1 , "B2":4,"B3":7,"C1": 2, "C2" :5,"C3" :8}
        while True:
            cell = input(f"\n{self.name},{self.sign} :Enter the cell number [A-C][1-3] : ")
            #check for the validdation of the cell
            if cell not in s:
                print("The given input is incorrect. Please rewrite")
                continue
            #deduce the value of the cell
            cell = s[cell]
            if cell >= 0 and cell < 9 and b.board[cell] == " ":
                #calling the function to set the sign
                b.set(cell,self.sign)
                break
            else:
                print("The given input is incorrect. Please rewrite")


# class MiniMax(Player):
#     def choose(self, board):
#         print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
#         cell = MiniMax.minimax(self, board, True, True)
#         print(cell)
#         board.set(cell, self.sign)
#     def minimax(self, board, self_player, start):
#         # check the base conditions
#         if board.isdone():
#             # self is a winner
#             if board.get_winner() == False:
#                 return 1
#             # is a tie
#             elif board.get_winner() == True:
#                 return 0
#             # self is a loser (opponent is a winner)
#             else:
#                 return -1
                
