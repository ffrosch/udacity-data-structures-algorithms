#!/usr/bin/env python3.10

import hashlib
from datetime import datetime


class Block:
    def __init__(self, data, previous_hash, index):
        self.index = index
        self.timestamp = datetime.utcnow().isoformat()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.next = None

    def __repr__(self):
        return (
            f"Index: {self.index}\n"
            f"Timestamp: {self.timestamp}\n"
            f"Data: {self.data}\n"
            f"Previous Hash: {self.previous_hash}\n"
            f"Hash: {self.hash}"
        )

    def calc_hash(self, data):
        sha = hashlib.sha256()
        sha.update(data.encode("utf-8"))
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.size = 0
        self.root = None

    def __repr__(self):
        if self.root is None:
            return "No Blocks."

        blocks = []
        current = self.root
        while current:
            blocks.append(str(current))
            current = current.next

        return f"\n--- Blockchain Size: {self.size} ---\n" + "\n--->\n".join(
            blocks
        )

    def add_block(self, data):
        self.size += 1

        if self.root is None:
            self.root = Block(data, 0, self.size)
            return

        current = self.root
        while current.next:
            current = current.next

        current.next = Block(data, current.hash, self.size)


if __name__ == "__main__":
    b = Blockchain()
    print(b)
    # No Blocks.
    b.add_block("Dummy Data1")
    print(b)
    # --- Blockchain Size: 1 --- ...
    b.add_block("Dummy Data2")
    print(b)
    # --- Blockchain Size: 2 --- ...
    print(b.root.hash == b.root.next.previous_hash)
    # True
    print(b.root.previous_hash)
    # 0
