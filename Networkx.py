import  networkx as nx
import  ast
import Result
import SearchResults

class Graph:

    def __init__(self):
        self.G = nx.Graph()


    def GetGraph(self):

        file = open("AdjList")

        for line in file.readlines():

            adjList = ast.literal_eval(line)
            self.G.add_node(adjList[0])

            for item in adjList[1]:
                if not self.G.has_edge(item, adjList[0]):
                    self.G.add_edge(adjList[0], item, weight=1)
        return self.G

    def GetSmallerGraph(self,source,dest):
        smallerGraph = nx.Graph()

        pathList = [path for path in nx.all_shortest_paths(self.G, source=source,target=dest)]
        for path in pathList:
            for node in path:
                if not smallerGraph.has_node(node):
                    smallerGraph.add_node(node)
        for path in pathList:
            for i in range(0,len(path)-1):
                if not smallerGraph.has_edge(path[i],path[i+1]):
                    smallerGraph.add_edge(path[i],path[i+1])

        return  smallerGraph




    def GetDuration(self):

        counter = 0
        for edge in self.G.edges:
            if counter >= 2:
                break
            print(edge)
            soupTag = SearchResults.Launchwindow(edge[0], edge[1])
            elems = soupTag[0].find_all(SearchResults.find_elem)
            Result = Result.Results(elems[0])
            self.G[edge[0]][edge[1]]['duration'] = Result.Duration.split(',')[0]
            print(self.G[edge[0]][edge[1]]['duration'])
            counter += 1
        return self.G