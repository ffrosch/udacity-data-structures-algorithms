import math
from heapq import heappop, heappush
from typing import Dict, Tuple


class PriorityQueue:
    """A priority queue on top of pythons heap data structure."""

    def __init__(self):
        self.queue = list()

    def add(self, value: float, priority: float = 0.0):
        heappush(self.queue, (priority, value))

    def pop(self):
        _, value = heappop(self.queue)  # _ = priority, not used
        return value

    def __len__(self):
        return len(self.queue)


# Distance functions
# ------------------------
# Euclidean: Euclidean distance is the straight-line distance between two
# points. This means that movement is allowed at every angle.
# It guarantees to find the shortest distance possible, but might
# underestimate the real distance if e.g. an object is in the way.
# Euclidean distance is quite expensive to calculate because it uses squares
# and square roots.
# formula: d =  √[ (x2 – x1)2 + (y2 – y1)2]
#
# Manhatten: Manhatten distance calculates the absolute differences between
# to coordinate-pairs. For Manhatten distance only horizontal and vertical
# moves are allowed, which makes it very useful for distances between point
# on grids. For road networks it might actually be a better choice, because
# roads rarely go from A to B "as-the-bird-flies" and thus be more similar
# to a grid structure than anything else. Manhatten distance could overestimate
# the real distance.
# formula:  d = |x1 - x2| + |y1 - y2|
#
# Diagonal: Diagonal distance allows diagonal moves and tries to find the
# shortest path by combining diagonal with horizontal movement. Its distance
# estimates will usually lie somewhere between Euclidean and Manhatten
# distance.
# formula:
# d(n) = c_dd_min+c_n(d_max−d_min)
# d_max=max(∣n.x−goal.x∣,∣n.y−goal.y∣)d\_{max} = max(|n.x - goal.x|, |n.y - goal.y|)d_max=max(∣n.x−goal.x∣,∣n.y−goal.y∣)
# d_min=min(∣n.x−goal.x∣,∣n.y−goal.y∣)d\_{min} = min(|n.x - goal.x|, |n.y - goal.y|)d_min=min(∣n.x−goal.x∣,∣n.y−goal.y∣)
# c_n=cost of non-diagonal movementc\_n = \text{cost of non-diagonal movement}c_n=cost of non-diagonal movement
# cd=cost of diagonal movement=cn2≈cn⋅1.414c_d = \text{cost of diagonal movement} = c_n \sqrt{2} \approx c_n \cdot 1.414c​d​​=cost of diagonal movement=c​n​​√​2​​​≈c​n​​⋅1.414
#
# Dijkstra: Starts at a specified source and generates all shortest-paths to
# every node.
#
# A*: A* is a very efficient algorithm to find the shortes path between a defined
# start and a defined end. Its major drawback is its high space complexity of
# O(b^d). It is guaranteed to find a solution if it exists.


def distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """Calculate Euclidean Distance between two points.

    Args
    ----

    p1: Tuple[float, float]
    p2: Tuple[float, float]

    Returns
    -------
    distance: float
    """

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def reconstruct_path(origin: Dict[int, int], start: int, end: int):
    """Reconstruct a path from start to end.

    Given its predecessors, the start and the end, the path can be
    reconstructed.

    Args
    ----

    origin: Dict[int, int]
        key: node ID
        value: node's predecessor
    start: int
        ID of the origin intersection
    end: int
        ID of the destination intersection

    Returns
    -------

    List[int]
        list of integers representing a path from start to destination
    """
    reversed_path = [end]

    while end != start:
        end = origin[end]
        reversed_path.append(end)

    return list(reversed(reversed_path))


def shortest_path(M: object, start: int, end: int) -> list:
    """Return the shortest path based on A* algorithm.

    Code inspired by: https://leetcode.com/problems/shortest-path-in-binary-matrix/discuss/313347/a-search-in-python  # noqa

    Args
    ----

    map: object
        A representation of the 2D space
    start: int
        ID of the starting point
    end: int
        ID of the ending point

    Returns
    -------
    path: List[int]
        list of integers representing a path from start to destination
    """

    node_coords, nodes_adjacent = M.intersections, M.roads  # type: ignore

    end_coords = node_coords[end]
    visited, origin = set(), dict()

    # initialize single nodes distance from the origin
    nodes_id = node_coords.keys()
    dist_from_start = {node_id: math.inf for node_id in nodes_id}
    dist_from_start[start] = 0

    priority_queue = PriorityQueue()
    priority_queue.add(start)

    while priority_queue:
        # node with min cost
        node = priority_queue.pop()

        if node in visited:
            continue

        if node == end:
            return reconstruct_path(origin, start, node)

        visited.add(node)

        # examine all possible neighbours and update the cost function f
        # for nodes near the current node
        node_coord = node_coords[node]

        for neighbour in nodes_adjacent[node]:
            neighbour_coord = node_coords[neighbour]

            # total distance travelled to reach the neighbour
            cost_g = dist_from_start[node] + distance(
                node_coord, neighbour_coord
            )

            # estimated distance for the remaining distance to end
            cost_h = distance(neighbour_coord, end_coords)

            # estimated cost of the path
            # start to end via neighbour's position
            cost_f = cost_g + cost_h

            # is the actual distance travelled better
            # than the distance calculated previously?
            if cost_g < dist_from_start[neighbour]:

                # update neighbour's distance, predecessor
                # add it to the Priority Queue
                dist_from_start[neighbour] = cost_g
                origin[neighbour] = node
                priority_queue.add(neighbour, priority=cost_f)

    # no solution: graph may not be fully connected
    return list()
