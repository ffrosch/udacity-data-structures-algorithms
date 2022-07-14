#!/usr/bin/env python3.10

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, value="", handler=""):
        # Initialize the node with children as before, plus a handler
        self.value = value
        self.next = {}
        self.handler = handler

    def insert(self, node):
        # Insert the node as before
        self.next[node] = self.next.get(node, RouteTrieNode(value=node))


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with a root node and a handler,
        # this is the root path or home page node
        self.root = RouteTrieNode(handler=handler)

    def insert(self, nodes, handler):
        # Recursively add nodes
        # assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for node in nodes:
            current_node.insert(node)
            current_node = current_node.next[node]
        current_node.handler = handler

    def find(self, nodes):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if nodes == [""]:
            return self.root.handler

        current_node = self.root
        for node in nodes:
            current_node = current_node.next.get(node, None)
            if current_node is None:
                return ""

        return current_node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler):
        # Create a new RouteTrie for holding our routes
        # You could add a handler for 404 page not found responses as well!
        self.tree = RouteTrie(handler=handler)
        self.add_handler("404", "404 - Not Found")

    def add_handler(self, route, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.tree.insert(self.split_path(route), handler)

    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler = self.tree.find(self.split_path(route))
        if handler == "":
            return self.lookup("404")
        return handler

    def split_path(self, route):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return route.rstrip("/").split("/")


# fmt: off
# Some test cases

# create the router and add a route
router = Router("root handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup(""))  # should print 'root handler'
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("404"))  # should print '404 - Not Found'
print(router.lookup("/home"))  # should print '404 - Not Found'
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler'
print(router.lookup("/home/about/me"))  # should print '404 - Not Found'
print(router.lookup("/home/about/me/"))  # should print '404 - Not Found'
