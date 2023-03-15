class Trie(object):
    def __init__(self):
        # key가 None인 노드 하나를 헤드로 지정
        self.head = {}

    def insert(self, arr):
        curr_node = self.head

        # 삽입할 String 각 문자에 대해 자식 Node를 만들며 뿌리를 뻗어 나간다.
        for i in range(len(arr)):
            # 자식Node 중 같은 문자가 없으면 Node 새로 생성
            if arr[i] not in curr_node:
                curr_node[arr[i]] = {}

            # 자식 Node 중 같은 문자가 있으면 기존 꺼 사용
            curr_node = curr_node[arr[i]]

            # 마침표 찍어준다.
            curr_node['*'] = {}


    # 재귀 함수로 출력
    def print_trie(self, l, cur_node=None):
        if l == 0:
            cur_node = self.head

        # 키 이름으로 사전순 오름차순 정렬하여 내려간다.
        for c in sorted(cur_node.keys()):
            if c != '*':
                print('--' * l, c, sep="")
            self.print_trie(l + 1, cur_node[c])


t = Trie()
n = int(input())
for i in range(n):
    temp = list(input().split())
    t.insert(temp[1:])

t.print_trie(0)

