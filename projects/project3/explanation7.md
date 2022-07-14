# Problem 7 - HTTPRouter using Trie

This router uses a Trie data structure to efficiently determine the correct
handler for a route or return a 404 message if there is no handler for a route.

The router also automatically deals with trailing slashes.

`HTTPRouter` is based on `RouteTrie` which is based on `RouteTrieNode`.

Given that **M** is the number of words in the Trie and **N** is the average
length of a word:

```
RouteTrieNode's time complexity and space complexity to insert a character is O(1).

RouteTrie's time complexity and space complexity to insert a route is O(n).
RouteTrie's time complexity and space complexity to find a handler is O(M*N).

Router's time complexity and space complexity to add a handler is O(n).
Router's time complexity and space complexity to lookup a route is O(M*N).
```
