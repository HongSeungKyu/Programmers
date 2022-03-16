class Trie():
    def __init__(self):
        self.next = dict()
        self.value = 0
def solution(words):
    answer = 0
    tree = Trie()
    
    for word in words:
        subtree = tree
        for idx, val in enumerate(word):
            subtree.value += 1
            if val not in subtree.next:
                subtree.next[val] = Trie()
            subtree = subtree.next[val]
            if (idx == len(word) - 1):
                subtree.value += 1
            answer += subtree.value
    return answer