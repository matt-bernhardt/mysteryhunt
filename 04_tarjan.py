# Asking around to see which of the townspeople know each other really well...
def func(graph):
  stack = []
  lowlinks = {}
  components = []
  def connect(node):
    index = len(lowlinks)
    lowlinks[node] = index
    stack_len = len(stack)
    stack.append(node)
    for neighbor in graph[node]:
      if not neighbor in lowlinks:
        connect(neighbor)
      lowlinks[node] = min(lowlinks[node], lowlinks[neighbor])
    if index >= lowlinks[node]: 
      component = stack[stack_len:]
      components.append(component)
      for component_piece in component:
        lowlinks[component_piece] = len(graph)
        stack.pop()
  for node in graph:
    if not node in lowlinks:
      connect(node)
  return components