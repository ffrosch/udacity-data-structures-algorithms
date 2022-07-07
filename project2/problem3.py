#!/usr/bin/env python3.10

import heapq
import sys
from collections import Counter
from typing import Tuple


class Node:
    def __init__(self, char, freq):
        self.char: str | None = char
        self.freq: int = freq
        self.left: Node | None = None
        self.right: Node | None = None

    def __lt__(self, other: "Node") -> bool:
        return other.freq > self.freq


def merge_heap(heap: list) -> Node:
    """Merge a heap list into a tree."""
    if len(heap) > 1:
        child1, child2 = heapq.heappop(heap), heapq.heappop(heap)
        parent = Node(None, child1.freq + child2.freq)
        parent.left, parent.right = child1, child2
        heapq.heappush(heap, parent)
        merge_heap(heap)
    return heap[0]


def text_to_tree(text: str) -> Node:
    """Convert text to a min-heap frequency tree."""
    frequencies = dict(Counter(text))
    # edge case empty text:
    if frequencies == {}:
        return Node("", 0)

    heap = [Node(key, value) for key, value in frequencies.items()]
    heapq.heapify(heap)
    tree = merge_heap(heap)
    return tree


def create_codes(node: Node, code: str = "") -> dict:
    """Create huffman codes."""
    # edge case: single character in text
    if code == "" and node.left is None:
        code = "0"

    codes = {}
    if node.char is not None:
        codes[node.char] = code
    else:
        codes |= create_codes(node.left, code + str(0))
        codes |= create_codes(node.right, code + str(1))
    return codes


def huffman_encoding(data: str) -> Tuple[str, Node]:
    """Encode data with huffman codes."""
    tree = text_to_tree(data)
    codes = create_codes(tree)
    code = "".join([codes[char] for char in data])
    return code, tree


def huffman_decoding(data: str, tree: Node) -> str:
    """Decode huffman codes to text."""
    # edge case: single character in text
    if tree.left is None:
        return "".join([tree.char for _ in data])

    decoded = ""
    node = tree
    for pos, c in enumerate(data):
        match c:
            case "0":
                node = node.left
            case "1":
                node = node.right
        if node.char:
            decoded += node.char
            decoded += huffman_decoding(data[pos + 1 :], tree)
            break
    return decoded


def huffmann_test(text):
    print("-------------------------------------------------------")
    print(f"----- {text}")
    print("-------------------------------------------------------")
    print("The size of the data is: {}".format(sys.getsizeof(text)))

    encoded_data, tree = huffman_encoding(text)

    if len(encoded_data) == 0:
        print(
            "The size of the encoded data is: {}".format(
                sys.getsizeof(encoded_data)
            )
        )
    else:
        print(
            "The size of the encoded data is: {}".format(
                sys.getsizeof(int(encoded_data, base=2))
            )
        )
    print("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print(
        "The size of the decoded data is: {}".format(
            sys.getsizeof(decoded_data)
        )
    )
    print("The content of the encoded data is: {}".format(decoded_data))


if __name__ == "__main__":
    huffmann_test("The bird is the word")
    huffmann_test("")
    huffmann_test("12304905ndylköxykcv 1234uiopxyn.asdf")
    huffmann_test(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    )
