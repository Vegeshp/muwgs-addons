class Trie(object):
    class TrieNode(object):
        def __init__(self, is_end=False):
            self.next = dict()
            self.is_end = is_end

        def insert(self, s: str, index: int):
            if index == len(s):
                self.is_end = True
                return
            if s[index] not in self.next:
                self.next[s[index]] = Trie.TrieNode()
            self.next[s[index]].insert(s, index + 1)

        def find(self, s: str, index: int) -> bool:
            if index == len(s):
                return self.is_end
            if s[index] not in self.next:
                return False
            next = self.next[s[index]]
            return next.find(s, index + 1)

    def __init__(self):
        self.root = Trie.TrieNode()

    def insert(self, s: str):
        if type(s) != str:
            raise TypeError('input is not of type "str"')
        elif not s.isalpha():
            raise RuntimeError(f'"{s}" is not an alphabetic string')
        s = str.lower(s)
        self.root.insert(s, 0)

    def find(self, s) -> bool:
        return self.root.find(s, 0)
