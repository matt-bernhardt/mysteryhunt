def func(graph, start, end):
  unvisited = {node: math.inf for node in graph.nodes}
  unvisited[start] = 0
  visited = {}
  while not end in visited:
    min_node = None
    for node in unvisited:
      if min_node is None or unvisited[min_node] < unvisited[node]:
        min_node = node
    distance = unvisited.pop(min_node)
    for neighbor in graph.neighbors[min_node]:
      if neighbor in unvisited:
        neighbor_dist = distance + graph.distances[(min_node, neighbor)]
        if neighbor_dist < unvisited[neighbor]:
          unvisited[neighbor] = neighbor_dist
    visited[min_node] = distance
  return visited[end]
