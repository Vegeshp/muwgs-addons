from trie import Trie


def load_dict_from_file(path: str):
    t = Trie()
    with open(path, 'r') as f:
        for line in f.readlines():
            if len(line) != 0:
                t.insert(line)
