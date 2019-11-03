import FindPathFin
def cheapRoute(source,target,date):
    path, smallGraph = FindPathFin.FindRoute(source,target,date)
    cheapRoutes = FindPathFin.ReturnRoutes(path,smallGraph)
    #FindPathFin.PrintRoutes(cheapRoutes)
    return cheapRoutes
