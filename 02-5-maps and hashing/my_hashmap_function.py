# TODO: increase num_entries on put
# TODO: add delete function
# TODO: add __repr__ function
# TODO: add auto-increase of bucket for coefficient n/b larger than 0.7


class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self, bucket_size=10, p=37):
        self.p = p
        self.bucket_arr = [None for _ in range(bucket_size)]
        self.num_entries = 0

    def put(self, key, value):
        idx = self.get_hash(key)
        bucket_node = self.bucket_arr[idx]

        new_node = LinkedListNode(key, value)
        # nothing has been added at this index position
        #   just add first node
        if bucket_node is None:
            self.bucket_arr[idx] = new_node
            return

        # if first node equals key, replace its value and return
        elif bucket_node.key == key:
            bucket_node.value = value
            return

        # at least one item has been added at this index position
        #  find end of linked list and append the new item
        while bucket_node.next is not None:
            # if current node equals key, replace its value and return
            if bucket_node.key == key:
                bucket_node.value = value
                return

            # else continue iteration
            bucket_node = bucket_node.next

        # none of the nodes equaled the key and
        #   end of linked list is reached.
        #   add new key, value pair at end of list
        bucket_node.next = new_node

    def get(self, key):
        idx = self.get_hash(key)
        bucket_node = self.bucket_arr[idx]

        # nothing has been added at this index position
        if bucket_node is None:
            return None

        # if there are more nodes at this index position iterate through them
        while bucket_node:
            if bucket_node.key == key:
                return bucket_node.value

            bucket_node = bucket_node.next

        # None of the nodes contained the key
        return None

    def get_hash(self, key):
        coeff = 1  # 1 == p^0

        hash_value = 0
        for char in str(key):
            # compression will always be a number in range(self.bucket_size)
            #   it can safely be used as an index to where in self.bucket_arr
            #   the value of the key is stored
            compression = self.bucket_size

            hash_value += ord(char) * coeff
            hash_value %= compression  # compress hash
            coeff *= self.p  # increase coefficient
            coeff %= compression  # compress coefficient

        return hash_value % compression  # third compression

    @property
    def size(self):
        return self.num_entries

    @property
    def bucket_size(self):
        return len(self.bucket_arr)
