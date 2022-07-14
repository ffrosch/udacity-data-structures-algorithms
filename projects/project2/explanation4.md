# Active Directory

The task was to efficiently determine whether a user belongs to a specific group.

The Active Directory is basically a tree structure with an unlimited number of branches per node and an unlimited depth.
The structure is arbitrary and there is no way to know how to traverse the tree most effectively.
Pretty much like a file system...
The solution to this is a recursive tree traversal algorithm.

It will take O(n) in the worst case, where `n = number of groups + number of users`.

The given structure (based on lists) would not be a good solution for production.
For starters, every group and every user can only exist exactly once.
Thus dictionaries or sets together with some checks would be a much better solution.

The task however was to only write an efficient lookup.
