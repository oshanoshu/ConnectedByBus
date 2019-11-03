import Networkx
import SearchResults
import networkx


def FindRoute(source,target,date):


    graph = Networkx.Graph()
    G = graph.GetGraph()

    try:
        smallGraph = graph.GetSmallerGraph(source, target)
    except:
        print("No Path Found")
        exit(0)
    path = [way for way in networkx.all_shortest_paths(smallGraph, source=source, target=target)]
    print(path)
    return (path,smallGraph)




#for edge in smallGraph.edges:
    #print(edge)

    #BusTimes = []
    #soup = ""

    #soup = SearchResults.Launchwindow(int(edge[0]), int(edge[1]))
    #BusTimes = SearchResults.PrintResult(soup)

    #smallGraph[edge[0]][edge[1]]['BusTimes'] = BusTimes



def ReturnRoutes(path,smallGraph):
    cheapRoutes = []
    setbreak = False
    for way in path:

        cheapPath = []
        start = way[0]
        prev = 0
        for i in range(0, len(way) - 1):
            soup = ""
            BusTimesList = []
            if i == 0:
                soup = SearchResults.Launchwindow(int(way[i]), int(way[i + 1]))
                BusTimesList = SearchResults.PrintResult(soup, way[i], way[i + 1])
            # BusTimesList = smallGraph[way[i]][way[i + 1]]['BusTimes']

            else:
                lastRoute = cheapPath[-1]
                soup = SearchResults.Launchwindow(int(way[i]), int(way[i + 1]))
                BusList = SearchResults.PrintResult(soup, way[i], way[i + 1])

                FilteredList = []
                FilteredList.clear()
                [FilteredList.append(obj) for obj in BusList if obj.StartID == way[i]]

                # BusList = smallGraph[way[i]][way[i + 1]]['BusTimes']
                BusTimesList = [route for route in FilteredList if route.StartingTime > lastRoute.EndingTime]

                if len(BusTimesList) == 0:
                    soup = SearchResults.Launchwindow(way[i], way[i + 1], '2019-11-04')
                    List = SearchResults.PrintResult(soup, way[i], way[i + 1])

                    #smallGraph[way[i]][way[i + 1]]['BusTimes'] = List
                    #BusTimesList = smallGraph[way[i]][way[i + 1]]['BusTimes']
                    BusTimesList=List
                    if (len(BusTimesList) == 0):
                        setbreak = True
                        break

            # smallGraph[way[i]][way[i+1]]['PriceList']=[a.Price for a in BusTimesList]
            priceList = [a.Price for a in BusTimesList]
            try:
                minPrice = min(priceList)
                minPriceIndex = priceList.index(minPrice)
                cheapPath.append(BusTimesList[minPriceIndex])
            except:
                return [['Path not found']]

            

        cheapRoutes.append(cheapPath)
        return cheapRoutes

# def PrintRoutes(cheapRoutes):
#     for routes in cheapRoutes:
#         for node in routes:
#             print(node.StartingAddress+"        TO       "+node.DestAddress)
#         print("------------")






