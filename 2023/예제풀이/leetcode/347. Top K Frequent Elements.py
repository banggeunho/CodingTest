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

        alphaDict = {}
        wordAlphaDict = {}
        for i in range(self.n):
            for j in range(self.m):
                alphaDict[board[i][j]] = alphaDict.get(board[i][j], 0) + 1

        for i in range(len(self.word)):
            wordAlphaDict[word[i]] = wordAlphaDict.get(word[i], 0) + 1

        for alpha, count in wordAlphaDict.items():
            if alpha not in alphaDict.keys() or alphaDict[alpha] < count:
                return False

        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == word[0] and not self.result:
                    self.visited[i][j] = True
                    self.dfs(i, j, board[i][j], 0)
                    self.visited[i][j] = False

        return self.result

    def dfs(self, x, y, temp, depth):
        if temp == self.word:
            self.result = True
            return None

        if temp != self.word[:depth + 1]:
            print('----------')
            return None

        if depth == len(self.word):
            return None

        for i in range(4):
            nx, ny = x + self.dx[i], y + self.dy[i]
            if 0 <= nx < self.n and 0 <= ny < self.m and not self.visited[nx][ny]:
                self.visited[nx][ny] = True
                self.dfs(nx, ny, temp + self.board[nx][ny], depth + 1)
                self.visited[nx][ny] = False

        return None