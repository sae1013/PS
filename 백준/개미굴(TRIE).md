TRIE 알고리즘. 
트리 알고리즘 문제 슬슬 정복하기

```python
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data  # data is set to None if node is not the final char of string
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)  # Trie객체 초기화시, head에 빈 노드객체저장

    """ Insert string """

    def insert(self, string):
        cur_node = self.head

        for char in string: 
            if char not in cur_node.children:  # 단어가 현재노드에 포함되어있나?
                cur_node.children[char] = Node(char)  # 노드를새로생성하고 하위객체에 저장
            cur_node = cur_node.children[char]  # 현재노드는 위에서 만든 자식객체


    def order(self,curNode): 
        if len(curNode.children)>1:
            curNode.children = dict(sorted(curNode.children.items(), key = lambda x : x[0]))
            for x in curNode.children:
                self.order(curNode.children[x])    
        else:
            for x in curNode.children:
                self.order(curNode.children[x])

    def find(self,curNode,depth):
        string = depth*"--"+curNode.key
        print(string)
        if len(curNode.children)>0:
            for x in curNode.children:
                self.find(curNode.children[x],depth+1)

trie = Trie()

N = int(input())
for i in range(N):
    string = input().split()
    string = string[1:]
    trie.insert(string)
        
#children 사전순으로 정렬
trie.order(trie.head) #root 노드를 던져줌

# 출력코드
for x in trie.head.children:
    trie.find(trie.head.children[x],0)

```
