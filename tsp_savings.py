import random

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

edges=[]
for i in range(n):
    for j in range(n):
        if i!=j:
            edges.append([i,j,edge[i][j]])

edges=sorted(edges, key = lambda v:v[2])

def printPath(path,n):
    for i in range(n):
        print(path[i],end=' ')
    print()

def costPath(path,edge):
    cost=edge[path[-1]][path[0]]
    for j in range(1,n):
        cost+=edge[path[j-1]][path[j]]
    return cost

def assign(path,n):
    P=[]
    for i in range(n):
        P.append(path[i])
    return P

cost=float('inf')
for k in range(n):
    v=k
    tours=[]
    for i in range(n):
        if i!=v:
            tours.append([i])
    
    while(len(tours)>1):
        m=0
        # print(len(tours))
        for i in range(len(tours)):
            for j in range(i+1,len(tours)):
                if edge[v][tours[i][0]]+edge[v][tours[j][0]]-edge[tours[i][0]][tours[j][0]]>m:
                    ind=[i,0,j,0]
                    m=edge[v][tours[i][0]]+edge[v][tours[j][0]]-edge[tours[i][0]][tours[j][0]]
                if edge[v][tours[i][0]]+edge[v][tours[j][-1]]-edge[tours[i][0]][tours[j][-1]]>m:
                    ind=[i,0,j,-1]
                    m=edge[v][tours[i][0]]+edge[v][tours[j][-1]]-edge[tours[i][0]][tours[j][-1]]
                if edge[v][tours[i][-1]]+edge[v][tours[j][0]]-edge[tours[i][-1]][tours[j][0]]>m:
                    ind=[i,-1,j,0]
                    m=edge[v][tours[i][-1]]+edge[v][tours[j][0]]-edge[tours[i][-1]][tours[j][0]]
                if edge[v][tours[i][-1]]+edge[v][tours[j][-1]]-edge[tours[i][-1]][tours[j][-1]]>m:
                    ind=[i,-1,j,-1]
                    m=edge[v][tours[i][-1]]+edge[v][tours[j][-1]]-edge[tours[i][-1]][tours[j][-1]]
        if (ind[1]==0 and ind[-1]==-1) or (ind[1]==-1 and ind[-1]==0):
            tours[ind[0]]=tours[ind[0]]+tours[ind[2]]
            del tours[ind[2]]
        else:
            C=[]
            for j in range(len(tours[ind[2]])-1,-1,-1):
                C=C+[tours[ind[2]][j]]
            if ind[1]==-1 and ind[-1]==-1:
                tours[ind[0]]=tours[ind[0]]+C
            else:
                tours[ind[0]]=C+tours[ind[0]]
            del tours[ind[2]]

    path=tours[0]
    path=[v]+path
    
    c=costPath(path,edge)
    if c<cost:
        bestPath=assign(path,n)
        printPath(path,n)
        cost=c