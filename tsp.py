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

def isValid(path,n):
    if len(path)!=n:
        return False
    C=[0 for x in range(n)]
    for p in path:
        C[p]+=1
    if max(C)==1 and min(C)==1:
        return True
    else:
        return False

def existsPath(start,end,X):
    if not X[start] or not X[end]:
        return False
    if X[start][0]==end:
        return True
    p=[start]
    p.append(X[start][0])
    while(len(X[p[-1]])==2):
        if X[p[-1]][0]==p[-2]:
            p.append(X[p[-1]][1])
        else:
            p.append(X[p[-1]][0])
        if p[-1]==end:
            return True
    return False

def assign(path,n):
    bestPath=[]
    for i in range(n):
        bestPath.append(path[i])
    return bestPath

degree=[0 for x in range(n)]
edge_path=[]
l=0
cost=0
D={}
for i in range(n):
    D[i]=[]
while(len(edge_path)<n and l<len(edges)):
    if degree[edges[l][0]]<2 and degree[edges[l][1]]<2 and existsPath(edges[l][0],edges[l][1],D)==False:
        edge_path.append(edges[l])
        cost+=edges[l][2]
        D[edges[l][0]].append(edges[l][1])
        D[edges[l][1]].append(edges[l][0])
        degree[edges[l][0]]+=1
        degree[edges[l][1]]+=1
    l+=1

for i in range(n):
    if len(D[i])==1:
        path=[i]
        break

for i in range(1,n):
    if D[path[-1]][0] not in path:
        path.append(D[path[-1]][0])
    elif D[path[-1]][1] not in path:
        path.append(D[path[-1]][1])

printPath(path,n)
bestPath=assign(path,n)
bestCost=costPath(path,edge)

def swapNodes(path,x,y):
    t=path[x]
    path[x]=path[y]
    path[y]=t
    return path

def swapEdge(path,x,y,n):
    A=[]
    for i in range(x+1):
        A.append(path[i])
    for i in range(y-1,x,-1):
        A.append(path[i])
    for i in range(y,len(path)):
        A.append(path[i])
    return A

def optimize(path,bestPath,bestCost,edge,n):
    C=[]
    for v in path:
        C.append(v)
    for i in range(n-1):
        for j in range(i+1,n):
            C=swapNodes(C,i,j)
            c=costPath(C,edge)
            C=swapNodes(C,j,i)
            if c<bestCost:
                path=swapNodes(path,i,j)
                C=swapNodes(C,i,j)
                bestPath=assign(path,n)
                bestCost=c
                printPath(path,n)

    c=bestCost
    p=c+1
    while(abs(p-c)>=1):
        p=c
        for i in range(n-1):
            for j in range(i+1,n):
                v=edge[path[i]][path[i+1]]+edge[path[j-1]][path[j]]
                s=edge[path[i]][path[j-1]]+edge[path[i+1]][path[j]]
                if s<v:
                    path=swapEdge(path,i,j,n)
                    v=costPath(path,edge)
                    if v<bestCost:
                        bestPath=assign(path,n)
                        printPath(path,n)
                        bestCost=v
        c=costPath(path,edge)
    return bestPath,bestCost

bestPath,bestCost=optimize(path,bestPath,bestCost,edge,n)
printPath(bestPath,n)

# Nearest Neighbour + Optimization 

cost=float('inf')
for k in range(n):
    v=k
    p=[v]
    for i in range(1,n):
        m=max(edge[v])+1
        ind=-1
        for j in range(n):
            if edge[v][j]<m and v!=j and (j not in p):
                m=edge[v][j]
                ind=j
        p.append(ind)
        v=ind
    c=costPath(p,edge)
    if c<cost:
        P=[]
        for i in range(n):
            P.append(p[i])
        cost=c

bestPath,bestCost=optimize(P,bestPath,bestCost,edge,n)
printPath(bestPath,n)
