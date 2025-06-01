
def dls_iterative(graph , start , goal , limit):

    #no visited set 
    stack = [(start , [start] , 0)] # => [ ( node , [ path ] , depth ) ] 


    while stack :
        node , path , depth = stack.pop()  # pop from the end of the list (LIFO)

        if node == goal :
            return path 
        
        if depth < limit :
            for son in reversed(graph.get(node , [])):
                if son not in path :
                    new_path = list(path)
                    new_path.append(son)
                    stack.append((son , new_path , depth + 1 ))
    
    return None 

# problem here with esch level it will store copy of  the full path 
# 1-  [(A , [A] , 0)] sons is B , C
# 2-  [   (B , [A,B] , 1)     ,  (C , [A,C] , 1)        ] CATCH B sons OF B IS E,D
# 3-  [ (C , [A,C] , 1) ,   (E , [A,B,E] , 2)     ,  (D , [A,B,D] , 2)        ] sons is B , C 
# وكذا اخون كل باث كفول باث ودا كده BFS مش DLS


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

print(dls_iterative(graph, 'A', 'G', limit=2))  # None (too shallow)
print(dls_iterative(graph, 'A', 'G', limit=3))  # ['A', 'D', 'G']
