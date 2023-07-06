# Travelling Salesman Problem
typ=input()
n=int(input())

cities=[]
for _ in range(n):
    a,b=map(float,input().split())
    cities.append([a,b])

edge=[]
for _ in range(n):
    e=list(map(float,input().split()))
    edge.append(e)

def costPath(path,edge):
    cost=edge[path[-1]][path[0]]
    for j in range(1,n):
        cost+=edge[path[j-1]][path[j]]
    return cost

# TSP Nearest Neighbour 
cost=float('inf')
for k in range(n):
    v=k
    path=[v]
    for i in range(1,n):
        m=max(edge[v])+1
        ind=-1
        for j in range(n):
            if edge[v][j]<m and v!=j and (j not in path):
                m=edge[v][j]
                ind=j
        path.append(ind)
        v=ind
    c=costPath(path,edge)
    if c<cost:
        for i in range(n):
            print(path[i],end=' ')
        print()
        cost=c