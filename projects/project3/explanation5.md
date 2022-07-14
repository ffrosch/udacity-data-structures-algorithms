# Problem 5 - Autocomplete with Tries

Tries are very similar to normal tree data structures. They can be used to
store words from a dictionary for e.g. autocomplete functionality.

Given that **M** is the number of words in the Trie and **N** is the average
length of a word:

```
TrieNode's time complexity and space complexity to insert a character is O(1).
TrieNode's time complexity and space complexity of suffixes of a node is O(M*N).

Trie's time complexity and space complexity to insert a word is O(n).
Trie's time complexity to find a prefix is O(n) and space complexity is O(1).
```
