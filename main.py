import sys


INF = sys.maxsize
vertices = 5

#створємо мартицю суміжності
Graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]


selected = [0, 0, 0, 0, 0]
# set number of edge to 0
counter = 0

selected[0] = True

print("Edge : Weight\n")
while (counter < vertices - 1):

    minimum = INF
    start_vertex = 0
    end_vertex = 0
    for items in range(vertices):
        if selected[items]:
            for j in range(vertices):
                if ((not selected[j]) and Graph[items][j]):
                    if minimum > Graph[items][j]:
                        minimum = Graph[items][j]
                        start_vertex = items
                        end_vertex = j
    print(str(start_vertex) + "-" + str(end_vertex) + ":" + str(Graph[start_vertex][end_vertex]))
    selected[end_vertex] = True
    counter += 1
