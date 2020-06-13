import numpy as np
import sys

def stochastic(graph):
    return np.divide(graph,graph.sum(axis=0),out=np.zeros_like(graph),where=graph.sum(axis=0)!=0)
    
f = open(sys.argv[1],"r")
beta = float(sys.argv[2])
epson = float(sys.argv[3])
n = int(f.readline())

#reading graph and building adjency matrix
G=np.zeros((n,n))
for line in f:
    nodes=line.strip().split(' ')
    G[int(nodes[0])][int(nodes[1])]=1

f.close()

#bulding stochastic matrix
M=stochastic(G)

#finding nodes with in-degree=0
out_nodes=[]
for i in range(0,n):
    result= np.sum(M[:,i])
    if result==0 :
        out_nodes.append(i)      

#starting r with 1/n value
aux=1/n
r=np.matrix(np.full((1,n),aux))
r = np.transpose(r)
r_old=r

#page rank algorithm  
for i in range(1,100):
    
    r = beta * M * r
    r[out_nodes[:]]=0
    r += (1-r.sum(axis=0))/n
    print(str('iteration ') + str(i)) 
    print(r)
    print()
    if (abs(r_old-r)<epson).all():
        break
    r_old=r
print('final result')    
print(r)    

