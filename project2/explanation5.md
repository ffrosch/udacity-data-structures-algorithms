# Problem 5: Blockchain

The task was to create a simple blockchain with basic mechanisms to ensure authenticity of each block.

As required, the blockchain was build as a linked list.
Nothing fancy here.
One important thing to consider was how to add new blocks.
A blockchain is destined to become a very large object over time.
So iterating over the whole chain to add a new block is no option.
Thus the **blockchain** keeps track of its tail so that blocks can be added with O(1).
Additionally the blockchain also keeps track of its size, so that its length can also be determined with O(1).

The hashing algorithm hashes the combination of *timestamp*, *data*, and *previous hash*.
This way none of these vital attributes can be manipulated without creating inconsistencies.
The hashing uses the magic string method which is also used for printing out information about the object.
This reduces duplicated code.

## Summary

This blockchain efficiently adds new blocks with O(1) and safeguards all vital information in blocks against manipulation. Accessing specific blocks apart from `head` and `tail` will take O(n).
