# Source : https://gist.github.com/skylarker/04335be7b0e607e26030
class Node(object):
    def __init__(self):
        self.parent = None
        self.children = {}
        self.data = ''


class Trie(object):
    def __init__(self):
        self.root = Node()
        self.root.data = ''

    def insert(self, word):
        curr = self.root
        i = 0
        for c in word:
            try:
                curr = curr.children[c]
            except KeyError:
                self.create_sub_tree(word[i:len(word)], curr)
                break
            i += 1

    @staticmethod
    def create_sub_tree(word_, node):
        curr = node
        for c in word_:
            curr.children[c] = Node()
            curr.children[c].parent = curr
            curr.children[c].data = curr.children[c].parent.data + c
            curr = curr.children[c]
            # print(curr, curr.parent, curr.data)

    def search(self, chars):
        start_node = self.root
        for c in chars:
            try:
                start_node = start_node.children[c]
            except KeyError:
                yield None
        node_stack = []

        for child in start_node.children:
            node_stack.append(start_node.children[child])

        while len(node_stack) != 0:
            curr_node = node_stack.pop()
            curr_word = curr_node.data

            if len(curr_node.children) == 0:
                yield curr_word
            for child in curr_node.children:
                temp = curr_node.children[child]
                node_stack.append(temp)


if __name__ == '__main__':
    trie = Trie()
    with open('./dict.txt', 'r+') as dictionary:
        for entry in dictionary.readlines():
            trie.insert(entry.rstrip())
    for item in trie.search('sa'):
        print(item)