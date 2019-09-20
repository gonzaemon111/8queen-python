# 8queens_all.py
from copy import deepcopy
 
SUCCESS = 1
FAIL = 0
 
FREE = 1
NOT_FREE = 0
N = 8
 
class Queens:
    def __init__(self):
        self.pos = [-1 for _ in range(N)]
        self.col = [FREE for _ in range(N)]
        self.up = [FREE for _ in range(2*N-1)]
        self.down = [FREE for _ in range(2*N-1)]
        self.count = 0
        self.answer = {}
 
    def print_queens(self, pos):
        for i in range(N):
            for j in range(N):
                if pos[i] == j:
                    print("Q ", end="")
                else:
                    print(". ", end="")
            print()
        print("---------------")
 
    def put_queen(self, a):
        for b in range(N):
            if self.col[b] == FREE and self.up[a+b] == FREE and \
                self.down[a-b+(N-1)] == FREE:
                self.pos[a] = b
                self.col[b] = NOT_FREE
                self.up[a+b] = NOT_FREE
                self.down[a-b+(N-1)] = NOT_FREE
 
                if a + 1 >= N:
                    self.count += 1
                    pos = deepcopy(self.pos)
                    self.answer[self.count] = pos
                else:
                    self.put_queen(a+1)
 
                self.pos[a] = -1
                self.col[b] = FREE
                self.up[a+b] = FREE
                self.down[a-b+(N-1)] = FREE
 
    def run(self):
        self.put_queen(0)
        if self.count:
            print("Found {} solutions.".format(self.count))
        else:
            print("Sorry, but there is no solution.")
 
if __name__ == '__main__':
    q = Queens()
    q.run()
    for k in q.answer.keys():
        q.print_queens(q.answer[k])
