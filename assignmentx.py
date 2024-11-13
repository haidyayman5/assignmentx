import heapq
graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("D", 0)],  # D is the goal
    "C": [("D", 0)],
    "D": []
}
heuristics = {
    "A": 6,
    "B": 4,
    "C": 2,
    "D": 0  # Goal node
}


def greedy_best_first_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], start))
    visited = set()

    while open_list:
        _, current_node = heapq.heappop(open_list)
        print(f"Visiting: {current_node}")
        if current_node == goal:
            print("Goal found!")
            return
        visited.add(current_node)
        for neighbor, _ in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(open_list, (heuristics[neighbor], neighbor))

    print("Goal not reachable")
greedy_best_first_search("A", "D")
