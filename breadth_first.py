# Example of breadth first search

# find if any of your connection is a mango seller, the closer the connection is, the better
# REF: Grokking algorithm, loc: 1368

from collections import deque

graph: dict[str, list] = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    "alice": ["peggy"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": [],
}


def is_mango_seller(name: str) -> bool:
    """
    check if the connection is a mango seller
    """
    return name in ["anuj", "thom"]


def search(name: str) -> bool:
    """
    breadth first algorithm.

    search through person connections and check if any of them is a mango seller.
    """

    search_queue: deque[str] = deque()
    search_queue.extend(graph[name])

    have_processed: list[str] = []
    while search_queue:
        person = search_queue.popleft()
        if person in have_processed:
            continue
        if is_mango_seller(person):
            print("%s is a mango seller" % person)
            return True
        else:
            have_processed.append(person)
            search_queue.extend(graph[person])

    print("There is no mango sellers on your connections")
    return False


if __name__ == "__main__":
    search("you")
