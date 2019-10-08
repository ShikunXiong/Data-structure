# Vertices: n
# Edges: m
# Convert from an adjacency matrix to adjacency lists
def matrixToList(arr):
    # time complexity: O(n^2)
    dic = {}
    size = len(arr)
    for i in range(size-1):
        for j in range(i+1, size):
            if arr[i][j] == 1:
                dic.setdefault(i,[])
                dic.setdefault(j, [])
                dic[i].append(j)
                dic[j].append(i)
    return dic


# Convert an adjacency list to an incidence matrix
def listToIncidence(link):
    # time complexity: O(m*n + m)
    vertices = len(link)
    dic = {}
    for k, l in link.items():
        for v in l:
            s = str(k) + str(v)
            if s in dic.keys() or s[::-1] in dic.keys():
                continue
            dic.setdefault(s, [])
            dic[s].append(k)
            dic[s].append(v)
    edges = len(dic)
    matrix = [[0 for i in range(edges)] for j in range(vertices)]
    edge = 0
    for k, l in dic.items():
        for v in l:
            matrix[v][edge] = 1
        edge += 1
    return matrix


# Convert from an incidence matrix to adjacency lists.
def incidenceToliist(matrix):
    # time complexity: O(m*n + m + n)
    dic = {}
    col = len(matrix[0])
    row = len(matrix)
    for c in range(col):
        dic.setdefault(c, [])
        for r in range(row):
            if matrix[r][c] == 1:
                dic[c].append(r)
    result = [[0 for i in range(row)] for j in range(row)]
    for k, l in dic.items():
        result[l[0]][l[1]] = 1
        result[l[1]][l[0]] = 1
    for i in range(len(result)):
        result[i][i] = 1
    return result


if __name__ == "__main__":
    arr = [[1,1,1,0,0],
           [1,1,0,1,1],
           [1,0,1,0,0],
           [0,1,0,1,1],
           [0,1,0,1,1]]
    link = matrixToList(arr)
    m = listToIncidence(link)
    original = incidenceToliist(m)
    print(original)
