# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler="/", error_message="not found handler"):
        self.root = RouteTrieNode(handler)
        self.error_message = error_message
        # Initialize the trie with an root node and a handler, this is the root path or home page node

    def insert(self, path, handler):
        self.root.insert(path, handler)
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

    def find(self, path_list):
        if len(path_list) == 0:
            return self.root.handler
        root = self.root.children
        for idx, path in enumerate(path_list):
            if idx == len(path_list) - 1 and bool(root):
                return root[path].handler if root[path].handler is not None else self.error_message
            if bool(root):
                root = root[path].children
        return self.error_message
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler="/"):
        self.handler = handler
        self.children = {}
        # Initialize the node with children as before, plus a handler

    def insert(self, path_list, handler):
        root = self.children
        for idx, path in enumerate(path_list):
            if idx == len(path_list) - 1:
                root[path] = RouteTrieNode(handler)
            else:
                root[path] = RouteTrieNode(None)
            root = root[path].children

        # Insert the node as before


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler="/", error_message="not found handler"):
        self.routes = RouteTrie(root_handler, error_message)
        pass

    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!

    def add_handler(self, path, handler):
        path_list = self.split_path(path)
        self.routes.insert(path_list, handler)

    # Add a handler for a path
    # You will need to split the path and pass the pass parts
    # as a list to the RouteTrie

    def lookup(self, path):
        path_list = self.split_path(path)
        return self.routes.find(path_list)

    # lookup path (by parts) and return the associated handler
    # you can return None if it's not found or
    # return the "not found" handler if you added one
    # bonus points if a path works with and without a trailing slash
    # e.g. /about and /about/ both return the /about handler

    def split_path(self, path):
        paths = path.split("/")
        out = []
        # trim blank strings
        for path in paths:
            if path != "":
                out.append(path)
        return out
    # you need to split the path into parts for
    # both the add_handler and loopup functions,
    # so it should be placed in a function here


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
