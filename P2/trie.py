# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete
# feature. To do that, we need to implement a new function on the TrieNode object that will return all complete word
# suffixes that exist below it in the trie. For example, if our Trie contains the words ["fun", "function",
# "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back
# from node.suffixes().
#
# Using the code you wrote for the TrieNode above, try to add the suffixes function below. (Hint: recurse down the
# trie, collecting suffixes as you go.)

# Represents a single node in the Trie


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, char):
        root = self.children
        for letter in char:
            if letter not in root:
                root[letter] = TrieNode()
            root = root[letter].children
        root['is_word'] = True

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        root = self.children
        for letter in suffix:
            root = root[letter].children
        arr = self.get_nested_values(root, [], "")

        return arr

    def get_nested_values(self, value, array, str):
        for key in value:
            if key == 'is_word' and value[key] and str != '':
                array.append(str)
            if key != 'is_word':
                str += key
                self.get_nested_values(value[key].children, array, str)
        return array


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        self.root.insert(word)


    def find(self, prefix):
        # Find the Trie node that represents this prefix
        root = self.root
        for letter in prefix:
            if letter not in root.children:
                return False
            root = root.children[letter]
        return root


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# print(MyTrie.root.suffixes('ant'))
# node=MyTrie.find('fu')
# print(MyTrie.find('triger'))
#
