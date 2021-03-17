
"""Depth-First Search (Recursive) Package"""

from typing import Optional
from collections.abc import Iterable, Mapping


def dfs_recursive(graph: Mapping[int, Iterable[int]], start: int, path: Optional[list[int]] = None):
    """Depth-First Search (Recursive)"""

    if path is None:
        path = []

    path.append(start)

    for node in graph[start]:
        if node not in path:
            dfs_recursive(graph, node, path)

    return path
