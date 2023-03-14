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

    def insert(self, string):
        curr_node = self.head

        # 삽입할 String 각 문자에 대해 자식 Node를 만들며 뿌리를 뻗어 나간다.
        for char in string:
            # 자식Node 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            # 자식 Node 중 같은 문자가 있으면 기존 꺼 사용
            curr_node = curr_node.children[char]

        # 문자열이 끝난 지점에 노드의 data에 해당 문자열 저장
        curr_node.data = string


    def search(self, string):
        # 가장 위에 있는 노드부터 탐색 시작
        curr_node = self.head
        # 각각의 문자에 대해 탐색
        for char in string:
            print(curr_node.key, curr_node.data, curr_node.data)
            # 자식 노드를 갖고 있으면
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            # 갖고 있지 않으면, 트라이 자료구조에 없는 것이다.
            else:
                return False

        # 탐색이 끝나고 해당 노드의 data가 존재한다면, 문자를 찾은 것이다.
        if curr_node.data is not None:
            return True

t = Trie()
t.insert('chunpense')
t.insert('chunpense1')

print(t.search('chunpense'))
print(t.search('chunpense2'))