#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
#
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
#
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
#
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[16]:


## Represents a single node in the Trie


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


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        self.root.insert(word)

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        root = self.root.children
        for letter in prefix:
            if letter not in root:
                return False
            root = root[letter].children
        return root


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)



print(MyTrie.root.suffixes('ant'))  # returns ['hology', 'hagonist', 'haonym']
print(MyTrie.find('fu'))  # returns the prefixNode
print(MyTrie.find(''))  # returns the rootnode
print(MyTrie.find('trigger'))  # returns False



from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f, prefix='')

# In[ ]:
