class Node:
    def __init__(self, key):
        self.key = key
        self.terminal = False
        self.child = {}
    
    def __str__(self):
        return str(self.key)
    
class Trie:
    def __init__(self):
        self.root = Node(key=None)
    
    def insert(self, string):
        now = self.root
        for i in range(len(string)):
            if string[i] not in now.child.keys():
                now.child[string[i]] = Node(key=string[i])
            now = now.child[string[i]]
        now.terminal = True
        return string

    def search(self, string):
        now = self.root
        for s in string:
            if s not in now.child.keys():
                return False
            now = now.child[s]
        if now.terminal:
            return True
        return False

    def match(self, string):
        """ Return the count needed to reach the target string

        Args :
            string (str) : target string
        
        Returns :
            int : input count to reach 'string'
        """
        now = self.root
        point = -1
        for i in range(len(string)):
            if not now.terminal and len(now.child) == 1:
                if point == -1:
                    point = i
            else:
                point = -1
            now = now.child.get(string[i])
        if now.child == {} and point != -1:
            return point
        return len(string)

trie = Trie()
arr = ["word","war","warrior","world"]
for a in arr:
    trie.insert(a)

print(trie.search('wolf'))      # False
print(trie.search('wa'))        # False
print(trie.search('war'))       # True
for a in arr:
    print(trie.match(a))        # 4, 3, 4, 4
