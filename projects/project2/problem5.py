#!/usr/bin/env python3.10

import hashlib
from datetime import datetime


class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.utcnow().isoformat()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(str(self))
        self.next = None

    def __str__(self):
        return (
            f"{str(self.timestamp)} {str(self.data)} {str(self.previous_hash)}"
        )

    def calc_hash(self, data):
        sha = hashlib.sha256()
        sha.update(data.encode("utf-8"))
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.size = 0
        self.root = None
        self.tail = None

    def __len__(self):
        return self.size

    def __str__(self):
        if self.root is None:
            return "No Blocks."

        blocks = []
        current = self.root
        while current:
            blocks.append(str(current))
            current = current.next

        return f"\n--- Blockchain Size: {self.size} ---\n" + "\n".join(blocks)

    def add_block(self, data):
        self.size += 1

        if self.root is None:
            self.root = Block(data, 0)
            self.tail = self.root
            return

        last = self.tail
        last.next = Block(data, last.hash)


if __name__ == "__main__":
    b = Blockchain()
    print(b)
    # No Blocks.
    b.add_block("Dummy Data1")
    print(b)
    # --- Blockchain Size: 1 ---
    # ...
    b.add_block("Dummy Data2")
    print(b)
    # --- Blockchain Size: 2 ---
    # ...
    print(b.root.hash == b.root.next.previous_hash)
    # True
    print(b.root.previous_hash)
    # 0
    b = Blockchain()
    for x in range(1000000):
        b.add_block(f"Dummy Data{x}")
    print("Created long blockchain (1M). Size:", len(b))
    # Created long blockchain (1M). Size: 1000000
