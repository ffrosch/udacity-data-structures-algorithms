# Problem 7 - HTTPRouter using Trie

This router uses a Trie data structure to efficiently determine the correct
handler for a route or return a 404 message if there is no handler for a route.

The router also automatically deals with trailing slashes.

`HTTPRouter` is based on `RouteTrie` which is based on `RouteTrieNode`.

Given that **M** is the number of words in the Trie and **N** is the average
length of a word:

**Time Complexity**

```
RouteTrieNode.__init__: O(1)
RouteTrieNode.insert: O(1) / O(n) -> basically the same because it would be
dependent on the size of the input in theory, but because the input is always
one character it's basically constant.

RouteTrie.__init__: O(1)
RouteTrie.insert: O(n)
RouteTrie.find: O(M*N)

Router.__init__: O(1)
Router.add_handler: O(n)
Router.lookup: O(M*N)
Router.split_path: O(n)
```

**Space Complexity**

```
RouteTrieNode.__init__: O(1)
RouteTrieNode.insert: O(1) / O(n) -> basically the same because it would be
dependent on the size of the input in theory, but because the input is always
one character it's basically constant.

RouteTrie.__init__: O(1)
RouteTrie.insert: O(n)
RouteTrie.find: O(M*N)

Router.__init__: O(1)
Router.add_handler: O(n)
Router.lookup: O(M*N)
Router.split_path: O(n)
```
