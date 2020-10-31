from sys import argv
from stack_array import *


class Vertex:
    def __init__(self, key, in_degree=0, adjacent_vertices=None):
        self.key = key
        self.in_degree = in_degree
        if adjacent_vertices is None:
            self.adjacent_vertices = []
        else:
            self.adjacent_vertices = adjacent_vertices


def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility "tsort".  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
    if len(vertices) == 0:
        raise ValueError("input contains no edges")
    if len(vertices) % 2 != 0:
        raise ValueError('input contains an odd number of tokens')
    vertex_dictionary = {}
    i = 0
    while i < len(vertices):
        vert1 = vertices[i]
        vert2 = vertices[i + 1]
        if not vert1 in vertex_dictionary:
            vertex_dictionary[vert1] = Vertex(vert1, 0, [vert2])
            if not vert2 in vertex_dictionary:
                vertex_dictionary[vert2] = Vertex(vert2, 1)
            else:
                vertex_dictionary.get(vert2).in_degree += 1
        else:
            if vert2 not in vertex_dictionary.get(vert1).adjacent_vertices:
                vertex_dictionary.get(vert1).adjacent_vertices.append(vert2)
            if not vert2 in vertex_dictionary:
                vertex_dictionary[vert2] = Vertex(vert2, 1, [])
            else:
                vertex_dictionary.get(vert2).in_degree += 1
        i += 2

    stack = Stack(len(vertices))
    for vert in vertex_dictionary:
        if vertex_dictionary[vert].in_degree == 0:
            stack.push(vertex_dictionary[vert])

    output = ""
    while not stack.is_empty():
        vert = stack.pop()
        output += vert.key + '\n'
        #print(vert.key, vert.adjacent_vertices)
        for key in vert.adjacent_vertices:
            vertex_dictionary[key].in_degree -= 1
            if vertex_dictionary[key].in_degree == 0:
                stack.push(vertex_dictionary[key])
    if output == "":
        raise ValueError("input contains a cycle")
    return output


def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()

    vertices = []
    for line in f:
        vertices += line.split()

    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
