class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    # 각 행을 기준으로 보겠다, 각 열을 기준으로 보겠다, 3X3 안의 같은 수가 있는지 보겠다.
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]

        print(res)
        # 중복 제거했을때 길이를 보겠다.
        return len(res) == len(set(res))