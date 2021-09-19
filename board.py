class Draw:
    def __init__(self, arr, p1, p2):
        self.array = arr
        self.p1 = p1
        self.p2 = p2
        #Get the board ready with certain values from array
    def show(self):
        board = '''-------------------------
    1   2   3
  + - + - + - +
1 | '''+self.array[0]+''' | '''+self.array[1]+''' | '''+self.array[2]+''' |
  + - + - + - +
2 | '''+self.array[3]+''' | '''+self.array[4]+''' | '''+self.array[5]+''' |
  + - + - + - +
3 | '''+self.array[6]+''' | '''+self.array[7]+''' | '''+self.array[8]+''' |
  + - + - + - +'''
        #Display board and some info
        print(board)
        print()
        print(self.p1 + ": X")
        print(self.p2 + ": O")