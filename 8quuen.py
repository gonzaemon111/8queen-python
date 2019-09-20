# 8queens.py
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
 
    def print_queens(self):
        for i in range(N):
            for j in range(N):
                if self.pos[i] == j:
                    print("Q ", end="")
                else:
                    print(". ", end="")
            print()
 
    def put_queen(self, a):
        for b in range(N):
            if self.col[b] == FREE and self.up[a+b] == FREE and \
                self.down[a-b+(N-1)] == FREE:
                self.pos[a] = b
                self.col[b] = NOT_FREE
                self.up[a+b] = NOT_FREE
                self.down[a-b+(N-1)] = NOT_FREE
 
                if a + 1 >= N:
                    return SUCCESS
                else:
                    if self.put_queen(a+1) == SUCCESS:
                        return SUCCESS
                    else:
                        self.pos[a] = -1
                        self.col[b] = FREE
                        self.up[a+b] = FREE
                        self.down[a-b+(N-1)] = FREE
 
        return FAIL
 
    def run(self):
        if self.put_queen(0) == SUCCESS:
            self.print_queens()
        else:
            print("Sorry, but there is no solution.")
 
if __name__ == '__main__':
    q = Queens()
    q.run()
