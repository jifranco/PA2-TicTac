class Board:
    #constructor for the class
    def __init__(self):
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        self.winner = ""

    #function to get the size
    def get_size(self):
        return len(self.board)

    def get_winner(self):
        #check for row same
        if self.board[0] == self.board[1] == self.board[2] != " ":
            return self.board[1]
        elif self.board[3] == self.board[4] == self.board[5] != " ":
            return self.board[4]
        elif self.board[6] == self.board[7] == self.board[8] != " ":
            return self.board[7]
        #check for same column
        elif self.board[3] == self.board[0] == self.board[6] != " ":
            return self.board[3]
        elif self.board[1] == self.board[4] == self.board[7] != " ":
            return self.board[4]
        elif self.board[2] == self.board[8] == self.board[5] != " ":
            return self.board[8]
        #check for diagonals
        elif self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[4]
        elif self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[4]

    #place the move on the board
    def set(self,cell,sign):
        self.board[cell] = sign

    #check of the cell is empty
    def isempty(self,cell):
        for i in range(self.size**2):
            if self.board[i] != " ":
                return False

        return True

    #check if we reach to the terminating codition
    def isdone(self):
        done = False

        #check for row same
        if self.board[0] == self.board[1] == self.board[2] != " ":
            done = True
        elif self.board[3] == self.board[4] == self.board[5] != " ":
            done = True
        elif self.board[6] == self.board[7] == self.board[8] != " ":
            done = True
        #check for same column
        elif self.board[3] == self.board[0] == self.board[6] != " ":
            done = True
        elif self.board[1] == self.board[4] == self.board[7] != " ":
            done = True
        elif self.board[2] == self.board[8] == self.board[5] != " ":
            done = True
        #check for diagonals
        elif self.board[0] == self.board[4] == self.board[8] != " ":
            done = True
        elif self.board[2] == self.board[4] == self.board[6] != " ":
            done = True

        return done

    #show the board
    def show(self):
        mat = ["A","B","C"]

        print("  ",end = "")
        #for first column only
        for ch in mat:
            print(ch,end = "  ")
        cnt = 1
        #for reamining rows and columns
        for i in range(9):
            if i%3 == 0:
                print()
                print(" +--"*3+"+")
                print(f"{cnt}",end="|")
                cnt += 1
            print(f" {self.board[i]} ",end = "|")