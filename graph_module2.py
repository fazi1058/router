class Graph():
  def __init__(self,graph,status):
        self.graph=graph
        self.status=status

  def find_all_paths(self,start, end,path =[]): 
    path = path + [start] 
    if start == end: 
      return [path] 
    paths = []
    newpaths=[] 
    for node in self.graph[start]: 
      if (node not in path) and (self.status[node]=='1'):
        newpaths = self.find_all_paths( node, end, path) 
      for newpath in newpaths: 
        paths.append(newpath) 
    return paths
