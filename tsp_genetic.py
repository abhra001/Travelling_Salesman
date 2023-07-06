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

def costPath(path,edge):
    cost=edge[path[-1]][path[0]]
    for j in range(1,n):
        cost+=edge[path[j-1]][path[j]]
    return cost

def OrderX(path1,path2,n):
    i=random.randint(1,n-2)
    j=random.randint(1,n-2)
    l=min(i,j)
    r=max(i,j)
    C1=[]
    j=0
    while(not C1 or len(C1)<l):
        if path2[j] not in path1[l:r+1]:
            C1.append(path2[j])
        j+=1
    for i in range(l,r+1):
        C1.append(path1[i])
    while(not C1 or len(C1)<n):
        if path2[j] not in path1[l:r+1]:
            C1.append(path2[j])
        j+=1    
    C2=[]
    j=0
    while(not C2 or len(C2)<l):
        if path1[j] not in path2[l:r+1]:
            C2.append(path1[j])
        j+=1
    for i in range(l,r+1):
        C2.append(path2[i])
    while(not C2 or len(C2)<n):
        if path1[j] not in path2[l:r+1]:
            C2.append(path1[j])
        j+=1
    return C1,C2

size=4
P=[]
for k in range(n**3):
    Z=[]
    for p in P:
        Z.append(1/costPath(p,edge))
    Zp=[]
    for i in range(size):
        Zp.append(Z[i]/sum(Z))
    for i in range(1,size):
        Zp[i]=Zp[i-1]+Zp[i]
    r=random.uniform(0,1)
    X=[]
    for i in range(size):
        for j in range(size):
            if r<Zp[j]:
                break
        X.append(P[j])
    V1=random.sample(range(size),int(size/2))
    V2=[]
    for i in range(size):
        if i not in V1:
            V2.append(i)
    C=[]
    for i in range(int(size/2)):
        c1,c2=OrderX(X[V1[i]],X[V2[i]],n)
        C.append(c1)
        C.append(c2)
    Z=[]
    for x in X:
        Z.append(1/costPath(x,edge))
    ind1=0
    for i in range(1,size):
        if Z[ind1]>Z[i]:
            ind1=i
    Zc=[]
    for c in C:
        Zc.append(1/costPath(c,edge))
    ind2=0
    for i in range(1,size):
        if Zc[ind1]>Zc[i]:
            ind2=i
    X[ind1]=X[ind2]
    P=X