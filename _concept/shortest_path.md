# Shortest Path Algorithm

- 가중치 그래프(`Weighted Graph`)에서 간선의 가중치 합이 최소가 되도록 하는 경로

## :pushpin: Types of shortest path

- single source - single destination  
  하나의 출발점과 하나의 도착점 사이의 최단 경로 문제
- single source - all destinations
  하나의 출발점에서 다른 모든 노드 각각의 최단 경로를 구하는 문제
- all pairs shortest paths  
  그래프 내 모든 노드 쌍에 대한 최단 경로 구하는 문제

## :pushpin: Algorithms

- BFS
- Dijkstra Algorithm
- Bellman-Ford Algorithm
- Floyd-Warshall Algorithm

## :pushpin: Dijkstra Algorithm

one of single source shortest path methods

- java
```java
public class Dijkstra {

  /**
   * we need three elements 
   * - MinHeap for shortest path selection (PriorityQueue) 
   * - distance map
   * - target for calculation
   * 
   * you can replace [Edge] class with Map.
   *
   * @return
   */
  static Map<String, Integer> dijkstraAlgorithm(Map<String, List<Edge>> graph, String start) {
    // create a distance map where each node is initialized with an infinite distance.
    Map<String, Integer> distance =
        graph.keySet()
            .stream()
            .collect(Collectors.toMap(
                key -> key,
                key -> Integer.MAX_VALUE
            ));

    // initial setup (insert start edge to heap queue)
    PriorityQueue<Edge> heapQ = new PriorityQueue<>(Comparator.comparingInt(Edge::getWeight));
    heapQ.add(new Edge(start, 0));
    distance.put(start, 0);

    while (!heapQ.isEmpty()) {
      Edge target = heapQ.poll();
      List<Edge> edges = graph.get(target.getTo());

      edges.forEach(edge -> {
        int calculatedWeight = target.getWeight() + edge.getWeight();
        Integer currentEdgeDist = distance.get(edge.getTo());

        // if the new result of distance calculation is smaller than existed one,
        // modify to the new one, and insert to heap queue.
        if (calculatedWeight < currentEdgeDist) {
          distance.put(edge.getTo(), calculatedWeight);
          heapQ.add(new Edge(edge.getTo(), calculatedWeight));
        }
      });
    }

    return distance;
  }

  public static void main(String[] args) {
    Map<String, List<Edge>> graph = new HashMap<>();
    graph.put("A", List.of(
        new Edge("B", 8),
        new Edge("C", 1),
        new Edge("D", 2)
    ));
    graph.put("B", Collections.emptyList());
    graph.put("C", List.of(
        new Edge("B", 5),
        new Edge("D", 2)
    ));
    graph.put("D", List.of(
        new Edge("E", 3),
        new Edge("F", 5)
    ));
    graph.put("E", List.of(
        new Edge("F", 1)
    ));
    graph.put("F", List.of(
        new Edge("A", 5)
    ));

    Map<String, Integer> distance = dijkstraAlgorithm(graph, "A");

    distance.forEach((key, value) -> {
      System.out.println("key: " + key + ", distance: " + value);
    });
  }
}
```

- python
```python
import heapq

mygraph = {
    'A': {'B':8, 'C':1, 'D':2},
    'B': {},
    'C': {'B':5, 'D':2},
    'D': {'E':3, 'F':5},
    'E': {'F':1},
    'F': {'A':5}
}

# distances: final result of the shortest path to each node from start node.
#   First, distances will be initiallized with all infinity except start node (0)
#   ex) start from A node > {'A':0, 'B':inf, 'C':inf, 'D':inf, ...}
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        # in case the distance of node is already less then distance in queue, it can be skipped
        if distances[current_node] < current_distance:
            continue
        
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances

result = dijkstra(mygraph, 'A')
```

### Complexity

Time complexity: $O((V + E)log{V})$ with **priority queue (min heap)**  
Space complexity: $O(V)$  
($V$: the number of vertices, $E$: the number of edges in graph)
