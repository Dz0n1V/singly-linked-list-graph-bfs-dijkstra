# singly-linked-list-weighted-graph-bfs-dijkstra

Directed weighted graph implemented with adjacency lists built on a custom singly linked list. Includes BFS reachability and Dijkstra's shortest path, with an interactive CLI menu.

The project models a mountain cable car network: nodes are locations on the mountain, edges are cable car lines, and edge weights are travel times in minutes. Everything is written in pure Python with no external dependencies.

## Features

- Custom **singly linked list with a header node**: create, destroy, print, insert at a given position, delete by value, search by value
- **Directed weighted graph** stored as adjacency lists, where each adjacency list is an instance of the custom linked list
- Add and remove nodes, add and remove edges, print the graph
- Load an entire cable car network from a text file
- **BFS** to find all locations reachable from a starting point (the queue is also built on the custom linked list)
- **Dijkstra's algorithm** for the shortest path between two locations, with the path reconstructed into a custom linked list
- Interactive menu-driven CLI with input validation

## Project structure

```text
.
├── cable_car_graph.py   # Graph program: linked list, queue, stack, graph, BFS, Dijkstra, menu
├── linked_list_demo.py  # Standalone interactive demo of the linked list (Task 1)
├── data/
│   └── example.txt   # Example cable car network
├── LICENSE
└── README.md
```

## Run

Requirements: Python 3.6+ (no external dependencies).

```bash
git clone https://github.com/Dz0n1V/singly-linked-list-weighted-graph-bfs-dijkstra.git
cd singly-linked-list-weighted-graph-bfs-dijkstra

# Graph program (Task 2)
python cable_car_graph.py

# Linked list demo (Task 1)
python linked_list_demo.py
```

Both programs print a menu and wait for you to enter the number of an option. They ask for additional parameters when needed and repeat until you choose to exit.

### Graph program menu

```text
1. Create a new graph
2. Add a node to the graph
3. Remove a node from the graph
4. Add an edge between nodes
5. Remove an edge between nodes
6. Print the graph representation
7. Load the graph from a file
8. Find all reachable places (BFS)
9. Find the shortest path
0. Exit the program
```

### Linked list demo menu

```text
1. Create a new list
2. Delete the list
3. Print the list
4. Insert an element at a given position
5. Delete an element with a given value
6. Search the list for a given value
7. Exit the program
```

Positions start at 0. Inserting at position `n` puts the new element at index `n` and shifts the following elements by one. Position equal to the current size appends to the end.

## Example input file

The first line lists all locations separated by commas. Each following line describes one cable car as `id1-id2-time`, where `time` is the travel time in minutes (a positive integer). The file `data/example.txt` contains:

```text
A1,A2,A3,A4,B1,B2,B3,C1
A1-A2-5
A2-A1-5
A2-A3-7
A3-A2-7
A1-B1-12
B1-B2-4
B2-B3-6
A3-B3-3
A3-A4-9
C1-A1-8
```

Notes on the format:

- A cable car that runs in **both directions** is written as two lines (`A1-A2-5` and `A2-A1-5`). A **one-way** cable car is written once (`A3-B3-3`).
- Identifiers must not contain `,` or `-`.
- Empty lines are ignored. Lines that are malformed or have a non-numeric time are reported and skipped.
- If an edge refers to a location that is not in the first line, the location is created automatically.

In this network `C1` can reach everything but nothing can reach `C1`, and `A3-B3` only works in one direction.

## Example session

Choose `7` and enter `data/example.txt` to load the file, then `6` to print the graph:

```text
A1: (A2, 5) -> (B1, 12)
A2: (A1, 5) -> (A3, 7)
A3: (A2, 7) -> (B3, 3) -> (A4, 9)
A4: []
B1: (B2, 4)
B2: (B3, 6)
B3: []
C1: (A1, 8)
```

Option `8` (BFS reachability) from `A1`, and then from `B1`:

```text
Places reachable from node A1:
1. A1
2. A2
3. B1
4. A3
5. B2
6. B3
7. A4

Places reachable from node B1:
1. B1
2. B2
3. B3
```

Option `9` (shortest path):

```text
Shortest path from A1 to B3:
A1 -> A2 -> A3 -> B3
Total time: 15 minutes

Shortest path from A1 to A4:
A1 -> A2 -> A3 -> A4
Total time: 21 minutes

No path exists from A1 to C1.
```

Note that the route `A1 -> A2 -> A3 -> B3` (15 min) beats the route over mountain B, `A1 -> B1 -> B2 -> B3` (22 min).

## Implementation notes

- The graph is a Python `dict` that maps each location identifier to its adjacency list. The adjacency list itself is the custom singly linked list, and each node stores a `(neighbor, weight)` pair.
- The BFS queue and the stack are thin wrappers around the custom linked list. A Python `set` is used only to remember visited nodes.
- Dijkstra's algorithm uses a simple linear scan to pick the closest unvisited node, so it runs in O(V²). That is fine for a cable car network of this size.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Assignment

This project was written as a university assignment on linked lists and graphs. The task description, translated to English, follows.

### Task 1 – Linked Lists

Write an interactive program that illustrates working with an appropriate type of linked list.

You need to implement and use a singly linked list with a header node

You need to implement the following operations for working with linked lists:

1. Creating and destroying a linked list
2. Printing the linked list
3. Inserting an element at a given position
4. Deleting an element with a given value
5. Searching the list based on a given value

The content of the node's information field is left to the person to implement and can be adapted to the needs of Task 2.

The user interacts with the program through a simple menu. The program should print the contents of the menu and then wait for the user to select (by entering via keyboard) the ordinal number of one of the offered items, after which, before execution, it expects the user to enter additional parameters if necessary. The procedure repeats until the user selects the option to exit the program from the menu.

### Task 2 – Graphs

A directed weighted graph is used to model a system of cable cars on a mountain range. In the graph, nodes represent locations on the mountain that offer various activities for visitors. An edge between two nodes means that it is possible to travel by cable car from the first point to the second. Between some locations there is a cable car that carries passengers in only one direction, and between others there is one that carries them in both directions.

Each location is determined by a unique identifier (e.g., A2, where A is the identifier of the mountain, and 2 is the ordinal number of the cable car on mountain A). The weight of an edge between two locations models the time needed to travel by cable car, expressed in minutes.

You need to implement the following operations for working with the directed weighted graph used to model the cable cars on this mountain range:

1. Creating and destroying the graph
2. Adding a node to the graph and removing a node from the graph
3. Adding and removing an edge between two nodes in the graph
4. Printing the graph representation

It must also be possible to load the entire plan of the mountain range from a file in the following format. The first line of the file contains the identifiers of all locations separated by commas, and all other lines in the file represent information about cable cars in the form `id1-id2-time`, where `id1` and `id2` are location identifiers, and `time` is the time needed to get from location `id1` to location `id2` by cable car.

When solving the given problem, you must use adjacency lists as the memory representation of the graph. For this representation, you must use the linked list structure implemented in Task 1. If stacks or queues are used in the solution, they must also be implemented using the list from Task 1.

Additionally, for more efficient organization of touring the mountain, the following must be supported:

1. Determining all locations on the mountain that can be reached by cable car from a given starting point
2. Determining the shortest path between two given locations on the mountain using Dijkstra's algorithm

Determining all locations on the mountain that can be reached by cable car from a given starting point should be implemented using *breadth-first search* (BFS)

The user interacts with the program through a simple menu. The program should print the contents of the menu and then wait for the user to select (by entering via keyboard) the ordinal number of one of the offered items, after which, before execution, it expects the user to enter additional parameters if necessary. The procedure repeats until the user selects the option to exit the program from the menu.
