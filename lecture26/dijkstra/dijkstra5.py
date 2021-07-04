from collections import deque


def dijkstra5_adapter(wrappee):
    def wrapper(*args, **kwargs):
        result = wrappee(*args, **kwargs)
        for v in result:
            if result[v] == float("+inf"):
                result[v] = None
        return result

    return wrapper


@dijkstra5_adapter
def dijkstra5(G: dict, start) -> dict:
    if start not in G:
        return "There is no start-vertex in graph"

    q = deque()
    q.append(start)
    d = {v: float("+inf") for v in G}
    d[start] = 0

    while q:
        v = q.popleft()
        for n in G[v]:
            if d[v] + G[v][n] < d[n]:
                d[n] = d[v] + G[v][n]
                q.append(n)

    return d
