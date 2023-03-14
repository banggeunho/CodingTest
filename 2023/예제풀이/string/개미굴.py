class Node(object):
    # 생성자
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = dict()

class Trie(object):
    def __init__(self):
        # key가 None인 노드 하나를 헤드로 지정
        self.head = Node(None)

    def insert(self, arr):
        curr_node = self.head

        # 삽입할 String 각 문자에 대해 자식 Node를 만들며 뿌리를 뻗어 나간다.
        for i in range(len(arr)):
            # 자식Node 중 같은 문자가 없으면 Node 새로 생성
            if arr[i] not in curr_node.children:
                curr_node.children[arr[i]] = Node(arr[i])

            # 자식 Node 중 같은 문자가 있으면 기존 꺼 사용
            curr_node = curr_node.children[arr[i]]

        # 문자열이 끝난 지점에 노드의 data에 해당 문자열 저장
        # curr_node.data = string

    def search(self, arr):
        # 가장 위에 있는 노드부터 탐색 시작
        curr_node = self.head
        # 각각의 문자에 대해 탐색
        for string in arr:
            print(curr_node.key, curr_node.data, curr_node.data)
            # 자식 노드를 갖고 있으면
            if string in curr_node.children:
                curr_node = curr_node.children[string]
            # 갖고 있지 않으면, 트라이 자료구조에 없는 것이다.
            else:
                return False

        # 탐색이 끝나고 해당 노드의 data가 존재한다면, 문자를 찾은 것이다.
        if curr_node.data is not None:
            return True

    # 재귀 함수로 출력
    def print_trie(self, l, cur_node=None):
        if l == 0:
            cur_node = self.head

        # 키 이름으로 사전순 오름차순 정렬하여 내려간다.
        for c in sorted(cur_node.children.keys()):
            if c != '*':
                print('--' * l, c, sep="")
            self.print_trie(l + 1, cur_node.children[c])


t = Trie()
n = int(input())
for i in range(n):
    temp = list(input().split())
    t.insert(temp[1:])

t.print_trie(0)

