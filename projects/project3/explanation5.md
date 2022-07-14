# Problem 5 - Autocomplete with Tries

Tries are very similar to normal tree data structures. They can be used to
store words from a dictionary for e.g. autocomplete functionality.

If `N` is the average length of a word in the Trie, then Time Complexity is
`O(N)`. Each operation (insert, find, suffixes) has to traverse the height of
the Trie for the given word or the possible suffixes to find.
