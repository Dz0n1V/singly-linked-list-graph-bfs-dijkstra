class ListNode:

    def __init__(self, data):

        self.data = data
        self.next = None

    def __repr__(self):

        return self.data

class LinkedList:

    def __init__(self):

        self.header = ListNode(None)
        self.count = 0

    def __repr__(self):

        curr = self.header.next
        output = []
        while curr is not None:
            output.append(str(curr.data))
            curr = curr.next
        output.append("None")
        return " -> ".join(output)


    def add_first(self, data):

        new_node = ListNode(data)
        new_node.next = self.header.next
        self.header.next = new_node
        self.count += 1


    def add_last(self, data):

        new_node = ListNode(data)
        curr = self.header
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        self.count += 1


    def remove(self, data):

        curr = self.header
        while curr.next is not None:
            if curr.next.data == data:
                curr.next = curr.next.next
                self.count -= 1
                return True
            curr = curr.next
        return False


    def contains(self, data):

        curr = self.header.next
        while curr is not None:
            if curr.data == data:
                return True
            curr = curr.next
        return False


    def is_empty(self):

        return self.count == 0


    def size(self):

        return self.count


    def find(self, data):

        curr = self.header.next
        while curr is not None:
            if curr.data == data:
                return curr
            curr = curr.next
        return None


class Queue:

    def __init__(self):

        self.items = LinkedList()


    def enqueue(self, element):

        self.items.add_last(element)


    def dequeue(self):

        if self.items.is_empty():
            return None
        first = self.items.header.next.data
        self.items.header.next = self.items.header.next.next
        self.items.count -= 1
        return first


    def is_empty(self):

        return self.items.is_empty()


class Stack:

    def __init__(self):

        self.items = LinkedList()


    def push(self, element):

        self.items.add_first(element)


    def pop(self):

        if self.items.is_empty():
            return None
        top = self.items.header.next.data
        self.items.header.next = self.items.header.next.next
        self.items.count -= 1
        return top


    def is_empty(self):

        return self.items.is_empty()



class Graph:

    def __init__(self):
        self.adjacency = {}


    def add_node(self, node_id):

        if node_id not in self.adjacency:
            self.adjacency[node_id] = LinkedList()
            print(f"Node {node_id} added to the graph.")
        else:
            print(f"Node {node_id} already exists in the graph.")


    def remove_node(self, node_id):

        if node_id in self.adjacency:
            del self.adjacency[node_id]
            for node in self.adjacency:
                neighbors = self.adjacency[node]
                curr = neighbors.header
                while curr.next is not None:
                    if curr.next.data[0] == node_id:
                        curr.next = curr.next.next
                        neighbors.count -= 1
                        break
                    curr = curr.next
            print(f"Node {node_id} removed from the graph.")
        else:
            print(f"Node {node_id} does not exist in the graph.")


    def add_edge(self, start_id, end_id, weight):

        if start_id not in self.adjacency:
            self.add_node(start_id)
        if end_id not in self.adjacency:
            self.add_node(end_id)
        neighbors = self.adjacency[start_id]
        curr = neighbors.header.next
        while curr is not None:
            if curr.data[0] == end_id:
                print(f"Edge from {start_id} to {end_id} already exists.")
                return
            curr = curr.next
        self.adjacency[start_id].add_last((end_id, weight))
        print(f"Edge from {start_id} to {end_id} with weight {weight} added.")


    def remove_edge(self, start_id, end_id):

        if start_id in self.adjacency:
            neighbors = self.adjacency[start_id]
            curr = neighbors.header
            while curr.next is not None:
                if curr.next.data[0] == end_id:
                    curr.next = curr.next.next
                    neighbors.count -= 1
                    print(f"Edge from {start_id} to {end_id} removed.")
                    return
                curr = curr.next
            print(f"Edge from {start_id} to {end_id} does not exist.")
        else:
            print(f"Node {start_id} does not exist in the graph.")


    def print_graph(self):

        print("\n---GRAPH REPRESENTATION---")
        if not self.adjacency:
            print("The graph is empty.")
            return
        for node in sorted(self.adjacency.keys()):
            print(f"{node}: ", end="")
            neighbors = self.adjacency[node]
            if neighbors.is_empty():
                print("[]")
            else:
                neighbor_list = []
                curr = neighbors.header.next
                while curr is not None:
                    neighbor_list.append(f"({curr.data[0]}, {curr.data[1]})")
                    curr = curr.next
                print(" -> ".join(neighbor_list))
        print()


def load_from_file(graph, file_name):

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        if not lines:
            print("The file is empty.")
            return False
        places = lines[0].strip().split(',')
        for place in places:
            graph.add_node(place.strip())
        for i in range(1, len(lines)):
            line = lines[i].strip()
            if line:
                parts = line.split('-')
                if len(parts) == 3:
                    id1, id2 = parts[0].strip(), parts[1].strip()
                    try:
                        time = int(parts[2].strip())
                        graph.add_edge(id1, id2, time)
                    except ValueError:
                        print(f"Error: time '{parts[2].strip()}' is not a number on line {i+1}")
                else:
                    print(f"Error: invalid line {i+1}: {line}")
        print(f"Graph successfully loaded from file {file_name}.")
        return True
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return False


def bfs_reachable_places(graph, start_node):

    if start_node not in graph.adjacency:
        print(f"Node {start_node} does not exist in the graph.")
        return LinkedList()
    visited = set()
    queue = Queue()
    result = LinkedList()
    queue.enqueue(start_node)
    visited.add(start_node)
    while not queue.is_empty():
        current = queue.dequeue()
        result.add_last(current)
        neighbors = graph.adjacency[current]
        curr = neighbors.header.next
        while curr is not None:
            neighbor = curr.data[0]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
            curr = curr.next
    return result


def dijkstra(graph, start, end):

    if start not in graph.adjacency or end not in graph.adjacency:
        print("One of the nodes does not exist in the graph.")
        return None, float('inf')
    distances = {}
    predecessor = {}
    visited = set()
    for node in graph.adjacency:
        distances[node] = float('inf')
        predecessor[node] = None
    distances[start] = 0
    while len(visited) < len(graph.adjacency):
        min_distance = float('inf')
        min_node = None
        for node in graph.adjacency:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node
        if min_node is None:
            break
        visited.add(min_node)
        neighbors = graph.adjacency[min_node]
        curr = neighbors.header.next
        while curr is not None:
            neighbor = curr.data[0]
            weight = curr.data[1]
            if neighbor not in visited:
                new_distance = distances[min_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessor[neighbor] = min_node
            curr = curr.next
    if distances[end] == float('inf'):
        return None, float('inf')
    path = LinkedList()
    current = end
    while current is not None:
        path.add_first(current)
        current = predecessor[current]
    return path, distances[end]


graph = None
while True:
    print("-----MENU-----")
    print("1. Create a new graph")
    print("2. Add a node to the graph")
    print("3. Remove a node from the graph")
    print("4. Add an edge between nodes")
    print("5. Remove an edge between nodes")
    print("6. Print the graph representation")
    print("7. Load the graph from a file")
    print("8. Find all reachable places (BFS)")
    print("9. Find the shortest path")
    print("0. Exit the program")
    try:
        option = input("Choose an option (0-9): ").strip()
        if option == '0':
            print("Exiting the program...")
            break
        elif option == '1':
            graph = Graph()
            print("New graph created.")
        elif option == '2':
            if graph is None:
                print("Create a graph first (option 1).")
                continue
            node_id = input("Enter node ID: ").strip()
            if not node_id:
                print("Node ID cannot be empty.")
                continue
            graph.add_node(node_id)
        elif option == '3':
            if graph is None:
                print("Create a graph first (option 1).")
                continue
            node_id = input("Enter the ID of the node to remove: ").strip()
            if not node_id:
                print("Node ID cannot be empty.")
                continue
            graph.remove_node(node_id)
        elif option == '4':
            if graph is None:
                print("Create a graph first (option 1).")
                continue
            start_id = input("Enter the start node ID: ").strip()
            end_id = input("Enter the end node ID: ").strip()
            weight_str = input("Enter the edge weight (time in minutes): ").strip()
            if not start_id or not end_id or not weight_str:
                print("All fields must be filled in.")
                continue
            try:
                weight = int(weight_str)
                if weight <= 0:
                    print("The weight must be positive.")
                    continue
                graph.add_edge(start_id, end_id, weight)
            except ValueError:
                print("The weight must be an integer.")
        elif option == '5':
            if graph is None:
                print("Create a graph first.")
                continue
            start_id = input("Enter the start node ID: ").strip()
            end_id = input("Enter the end node ID: ").strip()
            if not start_id or not end_id:
                print("Both IDs must be entered.")
                continue
            graph.remove_edge(start_id, end_id)
        elif option == '6':
            if graph is None:
                print("Create a graph first.")
                continue
            graph.print_graph()
        elif option == '7':
            graph = Graph()
            file_name = input("Enter the file name: ").strip()
            if not file_name:
                print("File name cannot be empty.")
                continue
            load_from_file(graph, file_name)
        elif option == '8':
            if graph is None:
                print("Create a graph first.")
                continue
            start = input("Enter the starting node: ").strip()
            if not start:
                print("Node ID cannot be empty.")
                continue
            reachable = bfs_reachable_places(graph, start)
            print(f"Places reachable from node {start}:")
            if reachable.is_empty():
                print("No reachable places.")
            else:
                curr = reachable.header.next
                i = 1
                while curr is not None:
                    print(f"{i}. {curr.data}")
                    curr = curr.next
                    i += 1
        elif option == '9':
            if graph is None:
                print("Create a graph first (option 1).")
                continue
            start = input("Enter the start node: ").strip()
            end = input("Enter the end node: ").strip()
            if not start or not end:
                print("Both nodes must be entered.")
                continue
            path, distance = dijkstra(graph, start, end)
            if path is None:
                print(f"No path exists from {start} to {end}.")
            else:
                print(f"Shortest path from {start} to {end}:")
                path_list = []
                curr = path.header.next
                while curr is not None:
                    path_list.append(curr.data)
                    curr = curr.next
                print(" -> ".join(path_list))
                print(f"Total time: {distance} minutes")
        else:
            print("Invalid option. Choose a number from 0 to 9.")
    except ValueError:
        print("Invalid input. Please try again.")
