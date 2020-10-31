from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.visited = False
        self.color = 'red'


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        with open(filename, 'r') as f:
            file = f.read().split('\n')
        dict = {}
        for line in file:
            if line != '':
                verticies = line.split()
                vert1 = verticies[0]
                vert2 = verticies[1]
                if vert1 in dict:
                    if vert2 not in dict[vert1].adjacent_to:
                        dict[vert1].adjacent_to.append(vert2)
                else:
                    new_vert = Vertex(vert1)
                    new_vert.adjacent_to.append(vert2)
                    dict[vert1] = new_vert
                if vert2 in dict:
                    if vert1 not in dict[vert2].adjacent_to:
                        dict[vert2].adjacent_to.append(vert1)
                else:
                    new_vert = Vertex(vert2)
                    new_vert.adjacent_to.append(vert1)
                    dict[vert2] = new_vert
            else:
                pass
 
        self.graph = dict


    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if key not in self.graph:
            self.graph[key] = Vertex(key)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key in self.graph:
            return self.graph[key]
        return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        if v2 not in self.graph[v1].adjacent_to:
            self.graph[v1].adjacent_to.append(v2)
        if v1 not in self.graph[v2].adjacent_to:
            self.graph[v2].adjacent_to.append(v1)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        ids = []
        for v in self.graph:
            ids.append(v)
        ids.sort()
        return ids

    def depth_first_search(self, lst, vertex, stack):
        stack.push(vertex.id)
        lst.append(vertex.id)
        vertex.visited = True
        if len(vertex.adjacent_to) > 0:
            for v in vertex.adjacent_to:
                neighbor = self.get_vertex(v)
                if neighbor.visited == False:
                    self.depth_first_search(lst, neighbor, stack)
        stack.pop()
        if stack.is_empty():
            return lst
                    

    def conn_components(self): 
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        components = []
        for vert in self.graph:
            self.graph[vert].visited = False
        for v in self.graph:
            v = self.graph[v]
            if v.visited == False:
                dfs = self.depth_first_search([], v, Stack(len(self.graph)))
                dfs.sort()
                components.append(dfs)
        components.sort()
        return components

    def breadth_first_search(self, lst, vertex, queue):
        if len(vertex.adjacent_to) > 0:
            lst.append(vertex)
            for v in vertex.adjacent_to:
                neighbor = self.get_vertex(v)
                if neighbor.visited == False:
                    if vertex.color == 'red':
                        neighbor.color = 'black'
                    queue.enqueue(neighbor)
                    lst.append(neighbor)
                    neighbor.visited = True
        if queue.is_empty():
            return lst
        next_vertex = queue.dequeue()
        return self.breadth_first_search(lst,next_vertex,queue)

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        for v in self.graph:
            self.graph[v].visited = False
        for j in self.graph:
            j = self.graph[j]
            if j.visited == False:
                j.visited = True
                bfs = self.breadth_first_search([], j, Queue(len(self.graph)))
                for k in bfs:
                    for i in k.adjacent_to:
                        neighbor = self.get_vertex(i)
                        if k.color == neighbor.color:
                            return False
        return True 
