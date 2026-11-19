from collections import deque
from typing import Dict, List, Optional

import pytest
from solution import Node, Solution

sol = Solution()


def build_graph(adj_list: List[List[int]]) -> Optional[Node]:
    """Converts a 1-indexed adjacency list into a connected graph of Node objects."""
    if not adj_list:
        return None

    nodes = [Node(i + 1) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[val - 1] for val in neighbors]

    return nodes[0]


def collect_nodes(start: Optional[Node]) -> Dict[int, Node]:
    """Traverses the graph via BFS and returns a mapping of node.val -> Node."""
    if not start:
        return {}

    visited: Dict[int, Node] = {start.val: start}
    queue = deque([start])

    while queue:
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if neighbor.val not in visited:
                visited[neighbor.val] = neighbor
                queue.append(neighbor)

    return visited


def to_adj_list(start: Optional[Node]) -> List[List[int]]:
    """Serializes a graph back into a normalized (sorted neighbors) 1-indexed adjacency list."""
    nodes_by_val = collect_nodes(start)
    if not nodes_by_val:
        return []

    return [
        sorted(nbr.val for nbr in nodes_by_val[val].neighbors)
        for val in range(1, len(nodes_by_val) + 1)
    ]


@pytest.mark.parametrize("adj_list", [
    # --- Standard Examples ---
    [[2], [1, 3], [2]],                                                        # Example 1: 3-node line
    [[]],                                                                      # Example 2: Single isolated node
    [],                                                                        # Example 3: Empty graph
    [[2, 4], [1, 3], [2, 4], [1, 3]],                                          # Classic 4-node cycle (square)

    # --- Minimal & Simple Cycles ---
    [[2], [1]],                                                                # Minimal 2-node edge
    [[2, 3], [1, 3], [1, 2]],                                                  # Triangle (K3)
    [[2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]],                              # Complete graph (K4)

    # --- Hub & Tree Topologies ---
    [[2, 3, 4, 5], [1], [1], [1], [1]],                                        # Star graph (hub at start node)
    [[2], [1, 3, 4, 5], [2], [2], [2]],                                        # Star graph (hub at non-start node)
    [[2], [1, 3], [2, 4], [3, 5], [4]],                                        # Linear path (5 nodes)
    [[2, 3], [1, 4, 5], [1, 6, 7], [2], [2], [3], [3]],                        # Binary tree structure (acyclic)

    # --- Bridges & Mixed Structures ---
    [[2, 3], [1, 3], [1, 2, 4], [3, 5, 6], [4, 6], [4, 5]],                    # Barbell (two triangles joined by a bridge)
    [[2, 4], [1, 3], [2, 4, 5], [1, 3], [3]],                                  # Lollipop (cycle with dangling tail)

    # --- Dense & Max Constraint Stress Tests ---
    [[i + 1 for i in range(10) if i != j] for j in range(10)],                 # Dense complete graph (K10)
    [[(i - 1) % 100 + 1, (i + 1) % 100 + 1] for i in range(100)],              # Max constraint: 100-node cycle
])
def test_cloneGraph(adj_list):
    """
    Tests cloneGraph across 15 standard, boundary, and complex graph topologies.
    Verifies both structural parity and strict deep-copy memory isolation.
    """
    original = build_graph(adj_list)
    cloned = sol.cloneGraph(original)

    if not adj_list:
        assert cloned is None
        return

    # 1. Verify identical graph structure and node values
    expected_normalized = [sorted(neighbors) for neighbors in adj_list]
    assert to_adj_list(cloned) == expected_normalized

    # 2. Verify strict deep-copy memory isolation (no shared Node references)
    original_nodes = collect_nodes(original)
    cloned_nodes = collect_nodes(cloned)

    assert len(original_nodes) == len(cloned_nodes)
    original_ids = {id(n) for n in original_nodes.values()}
    cloned_ids = {id(n) for n in cloned_nodes.values()}
    assert original_ids.isdisjoint(cloned_ids)