class Solution(object):
    n = 0
    m = 0
    word = ""
    visited = []
    board = []
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    result = False

    def exist(self, board, word):

        self.board = board
        self.word = word
        self.n = len(board)
        self.m = len(board[0])
        self.visited = [[False] * len(board[0]) for _ in range(len(board))]

        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == word[0]:
                    self.visited[i][j] = True
                    self.dfs(i, j, board[i][j], 0)
                    self.visited[i][j] = False

        return self.result

    def dfs(self, x, y, temp, depth):
        print(x, y, temp, depth, self.visited)
        if temp == self.word:
            self.result = True

        if len(temp) > len(self.word):
            return

        if temp != self.word[:depth + 1]:
            print('----------')
            return None



        for i in range(4):
            nx, ny = x + self.dx[i], y + self.dy[i]
            if 0 <= nx < self.n and 0 <= ny < self.m and not self.visited[nx][ny]:
                self.visited[nx][ny] = True
                self.dfs(nx, ny, temp + self.board[nx][ny], depth + 1)
                self.visited[nx][ny] = False


        return

s = Solution()
print(s.exist(board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], word = "AAAAAAAAAAAABAA"))