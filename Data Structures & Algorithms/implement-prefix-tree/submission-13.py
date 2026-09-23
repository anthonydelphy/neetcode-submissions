class TreeNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        temp = self.root
        for i in word:
            if i not in temp.children:
                temp.children[i] = TreeNode()
            temp = temp.children[i]
        temp.endOfWord = True

    def search(self, word: str) -> bool:
        
        if len(self.root.children) == 0:
            return False
        temp = self.root
        for i in word:
            if i not in temp.children:
                return False
            temp = temp.children[i]
        return temp.endOfWord
        

    def startsWith(self, prefix: str) -> bool:

        if len(self.root.children) == 0:
            return False
        temp = self.root
        for i in prefix:
            if i not in temp.children:
                return False
            temp = temp.children[i]
        return True
        

        