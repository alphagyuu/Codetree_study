class Node:
    def __init__(self):
        self.is_end = False
        self.children = {}

def insert_and_check(root, word):
    cur = root
    for char in word:
        # 1. 가는 길에 이미 끝나는 단어가 있다면? (기존 단어가 내 접두사)
        if cur.is_end:
            return False
        
        if char not in cur.children:
            cur.children[char] = Node()
        cur = cur.children[char]
    
    # 2. 단어 삽입을 마쳤는데, 이 노드에 이미 자식이 있다면? (내가 기존 단어의 접두사)
    if cur.children:
        return False
    
    # 3. 단어 삽입을 마쳤는데, 이미 is_end가 True라면? (중복 단어 입력)
    if cur.is_end:
        return False

    cur.is_end = True
    return True


n = int(input())
sequences = [input().strip() for _ in range(n)]

root = Node()
prefix_yes = 1

for seq in sequences:
    if not insert_and_check(root, seq):
        prefix_yes = 0
        break  # 하나라도 발견되면 더 볼 필요 없음
        
print(prefix_yes)

