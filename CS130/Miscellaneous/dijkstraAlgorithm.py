import heapq as hq
# constants
graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}
inf = float('inf')

def dijkstra(graph, source):
    distances = {}
    previous = {}
    visited = []
    for key in graph:
        distances[key] = inf
        previous[key] = None


    distances[source] = 0
    cnode = source
    visited.append(source)
    while(len(visited) != len(graph)):
        min = inf
        for v in graph[cnode]:
            graph[cnode][v]
            distances[v] = graph[cnode][v]
            if graph[cnode][v] < min:
                min = graph[cnode][v]

    return distances


print(dijkstra(graph, 'e'))


