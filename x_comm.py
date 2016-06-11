import networkx as nx
import matplotlib.pyplot as plt
import math
import random
import pylab
import pickle


n=5 #initial number of nodes in a community
G=nx.Graph()


def create_community():
   
    curr_node=0	
    for k in range (10):
        for i in range (k*n,((k+1)*n)):
            G.add_node(curr_node)
            G.node[curr_node]['community']=k	
			
            for j in range (k*n,i): 
                G.add_edge(i,j)
            curr_node = curr_node + 1
            
create_community()            
r1=3
r2=12 #range of incoming edges
f=0.7 #fraction of edges each node makes in its own community
no_of_edges=random.randint(2,12)
intra=math.ceil(f*no_of_edges)

inter=no_of_edges-intra


def add_edges(node,comm):
        
        n=0
        for i in G.nodes():
            if(G.node[i]['community']==comm):
                  n=n+1
            
            
        G.add_node(node)
        G.node[node]['community']=comm    
        # Target nodes for new edges
        targets=list(range(intra))
    # List of existing nodes, with nodes repeated once for each adjacent edge
        repeated_nodes=[]
    # Start adding the other n-m nodes. The first node is m.
        source=intra
        while source<n:
        # Add edges to m nodes from the source.
           G.add_edges_from(zip([source]*intra,targets))
        # Add one node to the list for each new edge just created.
           repeated_nodes.extend(targets)
        # And the new node "source" has m edges to add to the list.
           repeated_nodes.extend([source]*intra)
        # Now choose m unique nodes from the existing nodes
        # Pick uniformly from repeated_nodes (preferential attachement)
           targets = random.sample(repeated_nodes,intra)
           source += 1
           
        k=0
        for i in G.nodes():
            if(G.node[i]['community']!=comm):
                  k=k+1
            
            
        
        # Target nodes for new edges
        targets1=list(range(inter))
    # List of existing nodes, with nodes repeated once for each adjacent edge
        repeated_nodes1=[]
    # Start adding the other n-m nodes. The first node is m.
        source1=inter
        while source<n:
        # Add edges to m nodes from the source.
           G.add_edges_from(zip([source1]*inter,targets))
        # Add one node to the list for each new edge just created.
           repeated_nodes1.extend(targets1)
        # And the new node "source" has m edges to add to the list.
           repeated_nodes.extend([source1]*inter)
        # Now choose m unique nodes from the existing nodes
        # Pick uniformly from repeated_nodes (preferential attachement)
           targets1 = random.sample(repeated_nodes1,inter)
           source1 += 1   
           
New_nodes=2
count=1
num=50
while (count<=New_nodes):
	i=0
	while (i<=9):			
		add_edges(num,i)		
		
		num=num+1
		i=i+1
	
	
	count= count + 1	        
        

        
nx.draw(G)
plt.show()

degrees  = G.degree() 
d=[]
for key,value in sorted(degrees.items()):
     d.append(value)

def histogram(s):
    d = dict()
    for c in s:
      if c not in d:
          d[c] = 1
      else:
          d[c] += 1
    return d            
    
f_values=histogram(d)
print(f_values)
x=[]
y=[]
for key,value in sorted(f_values.items()):
      x.append(value)
      y.append(key)
  
plt.figure()
plt.plot(x,y,'ro-') 

plt.xlabel('Degree')
plt.ylabel('Number of nodes')
plt.show()