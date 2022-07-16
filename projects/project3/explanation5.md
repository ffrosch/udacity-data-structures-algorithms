# Problem 5 - Autocomplete with Tries

Tries are very similar to normal tree data structures. They can be used to
store words from a dictionary for e.g. autocomplete functionality.

Given that **M** is the number of words in the Trie and **N** is the average
length of a word:

**Time Complexity**

```
TrieNode.__init__: O(1)
TrieNode.insert: O(1)
TrieNode.suffixes: O(M*N)

Trie.__init__: O(1)
Trie.insert: O(n)
Trie.find: O(n)
```

**Space Complexity**

```
TrieNode.__init__: O(1)
TrieNode.insert: O(1) / O(n) -> basically the same because it would be
dependent on the size of the input in theory, but because the input is always
one character it's basically constant.
TrieNode.suffixes: O(M*N)

Trie.__init__: O(1)
Trie.insert: O(n)
Trie.find: O(n) -> we need to iterate over the prefix and thus the space needed
is dependend on the size of the prefix.
```
