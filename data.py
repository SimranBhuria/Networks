import networkx as nx
import matplotlib.pyplot as plt


import pylab
import pickle

edge_list=[]
fin=open('CA-AstroPh.txt')
for line in fin:
  if '#' not in line:  
    l=line.strip()
    f=tuple(l.split())
    edge_list.append(f)
    

G=pickle.load(open('Astrophysics.pickle', 'rb'))


neighbors=G.neighbors_iter
degrees=G.degree()
# sort nodes by degree
nodes=sorted(degrees,key=degrees.get)
shells=[0]
current=0
for i,v in enumerate(nodes):
    if degrees[v]>current:
            shells.extend([i]*(degrees[v]-current))
            current=degrees[v]
nodeposition = dict((v,pos) for pos,v in enumerate(nodes))
    # initial guesses for core is degree
core=degrees
nbrs=dict((v,set(neighbors(v))) for v in G)
for v in nodes:
       for u in nbrs[v]:
            if core[u] > core[v]:
                nbrs[u].remove(v)
                pos=nodeposition[u]
                s_begin=shells[core[u]]
                nodeposition[u]=s_begin
                nodeposition[nodes[s_begin]]=pos
                nodes[s_begin],nodes[pos]=nodes[pos],nodes[s_begin]
                shells[core[u]]+=1
                core[u]-=1
print(core)    
