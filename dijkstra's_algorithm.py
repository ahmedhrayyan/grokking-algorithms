# Example of dijkstra's algorithm

# Find the shortest path in a weighted graph
# REF: Grokking algorithm, loc: 1635

from typing import Optional

graph: dict[str, dict[str, int]] = {
    "start": {"a": 6, "b": 2},
    "a": {"fin": 1},
    "b": {"fin": 5, "a": 3},
    "fin": {},
}
parents: dict[str, Optional[str]] = {"a": "start", "b": "start", "fin": None}
costs: dict[str, int] = {"a": 6, "b": 2, "fin": float("inf")}

processed: list[str] = []


def get_lowest_cost_node():
    """
    Get the cheapest node which have not been processed yet

    :return: None if all nodes have been processed or node
    """
    lowest_cost_node = None
    lowest_cost = float("inf")
    for node, cost in costs.items():
        if node in processed:
            continue
        if cost < lowest_cost:
            lowest_cost_node = node
            lowest_cost = cost

    return lowest_cost_node


def find_shortest_path():
    """
    Find the shortest path in a weighted graph
    """

    node = get_lowest_cost_node()
    while node is not None:
        node_cost = costs[node]
        for neighbour, neighbour_cost in graph[node].items():
            new_cost = node_cost + neighbour_cost
            if new_cost < costs[neighbour]:
                costs[neighbour] = new_cost
                parents[neighbour] = node

        processed.append(node)
        node = get_lowest_cost_node()


if __name__ == "__main__":
    find_shortest_path()
    print(parents)
