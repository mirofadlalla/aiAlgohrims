

def dls(grapth , start , goal , limit):

    stack = [(start , 0)] # only stores the node and the depth 

    parent  = {start : None}

    while stack :
        node , depth = stack.pop()

        if node == goal :
            path = []
            while node is not None :
                path.append(node)
                node = parent[node]

            return path[::-1]

        if depth < limit :
            for son in reversed(grapth.get(node , [])):
                if son not in parent:  # to prevent cycles لازم نتاكد اننا ماعديناش على العقده دي قبل كده والحل نستخدم parent dict لانه هو المتاح 
                # if son not in path:  # this is not needed as we are using parent dict
                    # new_path = list(path)  # this is not needed as we are using parent dict
                    # new_path.append(son)  # this is not needed as we are using parent dict
                    stack.append((son , depth + 1)) 
                    parent[son] = node 
        
    return None