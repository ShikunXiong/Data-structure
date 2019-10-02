def bfs(g, startNode, dic1, dic2):
    already = [dic1[startNode]]
    now = [dic1[startNode]]
    l = BFS(g, now, already)
    print(l)
    for i in range(len(l)):
        l[i] = dic2[l[i]]
    return l


def BFS(g, now, already):
    if len(now)<1:
        return already
    tmp = []
    for r in now:
        for c in range(len(g[0])):
            if g[r][c] == 1 and r!=c and c not in already:
                tmp.append(c)
                already.append(c)
    now = tmp
    return BFS(g, now, already)

def DFS(g, node, dic1, dic2, already):
    index = dic1[node]
    already.append(index)
    for col in (range(len(g[0]))):
        if g[index][col] == 1 and col not in already:
            DFS(g, dic2[col], dic1, dic2, already)
    return already


if __name__=="__main__":
    matrix = [[1,1,0,1,0,0,0,0,1,0],
              [1,1,1,1,1,0,0,0,0,0],
              [0,1,1,0,1,1,0,0,0,0],
              [1,1,0,0,1,0,1,0,0,0],
              [0,1,1,1,1,1,1,1,0,0],
              [0,0,1,0,1,1,0,1,0,0],
              [0,0,0,1,1,0,1,1,1,1],
              [0,0,0,0,1,1,1,1,0,1],
              [1,0,0,0,0,0,1,0,1,1],
              [0,0,0,0,0,0,1,1,1,1]]
    dic1 = {}  #c->n
    dic2 = {}  #n->c
    index = ord("A")
    for i in range(10):
        c = chr(index)
        dic1.setdefault(c,i)
        dic2.setdefault(i,c)
        index += 1
    l = []
    # BFS
    print(bfs(matrix, 'B', dic1, dic2))

    # DFS
    dfsl = (DFS(matrix, 'A', dic1, dic2, []))
    for i in range(len(dfsl)):
        dfsl[i] = dic2[dfsl[i]]
    print(dfsl)