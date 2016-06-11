import networkx as nx
import matplotlib.pyplot as plt
import math
import random
import pylab
import pickle


n=3 #initial number of nodes in a community
G=nx.Graph()


def create_community():
   
    curr_node=0	
    for k in range (3):
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
no_of_edges=random.uniform(2,12)
intra=math.ceil(f*no_of_edges)
inter=no_of_edges-intra

def edge_exists(G, v1, v2):
    try:
        e = G[v1][v2] 
        exists=1
        return exists
    except KeyError:
        exists=0
        return exists

def add_edges(comm,num):
        G.add_node(num)			
        G.node[num]['community']=comm
        
        
        Prob=[]
        sum=0
        counter_same=0
        
        
        for i in range (G.number_of_nodes()):
            if(G.node[i]['community']==comm):
                counter_same=counter_same+1
                sum=sum+G.degree(i)
                Prob.append(G.degree(i)/sum)
            
       
        cummulative=[0]
        i=0
        for i in range(1,counter_same+1):
            cummulative.append(cummulative[i-1]+Prob[i-1])
            t=1

        #now the node has to make intra number of connections
        while(t<=intra):
            r=random.uniform(0,1)
            m=0
            for every in cummulative:
                if(r<=every):
                  
                    break
                m=m+1
            j=m-1	 
            link=0	
            counted_nodes=-1
            while(1):
                if (G.node[link]['community']!=comm):
                    link=link+1	
                    continue
                else:
                    counted_nodes=counted_nodes+1
                        
                if(counted_nodes==j):
                    break

                else:
                    link=link+1

            f = edge_exists(G, num, link)	
            
            if(f==0):	
                G.add_edge(num,link)
                print('Connected to node')
                
                t=t+1
        
        G.add_node(num)			
        G.node[num]['community']=comm
        
        
        Prob=[]
        sum=0
        counter_same=0
        
        
        for i in range (G.number_of_nodes()):
            if(G.node[i]['community']!=comm):
                counter_same=counter_same+1
                sum=sum+G.degree(i)
                Prob.append(G.degree(i)/sum)
            
       
        cummulative=[0]
        i=0
        for i in range(1,counter_same+1):
            cummulative.append(cum[i-1]+Prob[i-1])
            t=1

        
        while(t<=inter):
            r=random.uniform(0,1)
            m=0
            for every in cummulative:
                if(r<=every):
                  
                    break
                m=m+1
            j=m-1	 
            link=0	
            counted_nodes=-1
            while(1):
                if (G.node[link]['community']==comm):
                    link=link+1	
                    continue
                else:
                    counted_nodes=counted_nodes+1
                        
                if(counted_nodes==j):
                    break

                else:
                    link=link+1

            f = edge_exists(G, num, link)	
            
            if(f==0):	
                G.add_edge(num,link)
                print('Connected to node')
                
                t=t+1
        
New_nodes=1
count=1
num=9
while (count<=New_nodes):
	i=0
	while (i<=2):			
		add_edges(i,num)		
		
		num=num+1
		i=i+1
	
	
	count= count + 1	        
        

nx.draw(G)
plt.show()                 