#!/usr/bin/env python3.10


class TrieNode:
    def __init__(self, value=""):
        # Initialize this node in the Trie
        self.word_end = False
        self.value = value
        self.next = {}

    def insert(self, char):
        # Add a child node in this Trie
        self.next[char] = self.next.get(char, TrieNode(char))

    def suffixes(self, suffix=""):
        # Recursive function that collects the suffix for
        # all complete words below this point
        suffixes = []
        # do not return suffixes if we are at the root
        if not self.value:
            return suffixes

        if self.word_end:
            suffixes.append(suffix)
        for char, node in self.next.items():
            suffixes += node.suffixes(suffix + char)
        return suffixes


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current_node = self.root

        for char in word:
            current_node.insert(char)
            current_node = current_node.next[char]

        current_node.word_end = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            current_node = current_node.next.get(char, None)
            if current_node is None:
                return TrieNode()
        return current_node


MyTrie = Trie()
wordList = [
    "ant",
    "anthology",
    "antagonist",
    "antonym",
    "fun",
    "function",
    "factory",
    "trie",
    "trigger",
    "trigonometry",
    "tripod",
]
for word in wordList:
    MyTrie.insert(word)

prefixes = ["", "b", "a", "ant", "f", "trig"]
for prefix in prefixes:
    print(f"{prefix}".ljust(5), MyTrie.find(prefix).suffixes(), sep=":")
