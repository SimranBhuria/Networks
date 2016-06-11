
import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import pylab
import pickle


G=nx.erdos_renyi_graph(100,0.50)
nx.set_edge_attributes(G,'Counter',0)

nx.set_edge_attributes(G,'Weight', 2)

for i in range(10):
    

    nx.set_node_attributes(G,'Infected',False)
    nx.set_edge_attributes(G,'Infected',False)




    n=math.floor(G.number_of_nodes()/10)
    infect=[]
    i=1
    while(i<=n):
        index=random.choice(G.nodes())
        if index in infect:
            continue  
        else:
            infect.append(index)
            G.node[index]['Infected']=True
            
            i=i+1




       
    while(len(infect)>0):
        f_active=[]
        for m in infect:
           f=G.neighbors(m)
           random.shuffle(f)
           for j in f:
            
              r=random.uniform(0,1)
              if(r<=0.85):
              
                if(G.node[j]['Infected']==False):
                    G.node[j]['Infected']=True
                    G.edge[m][j]['Infected']=True
                    a=G.edge[m][j]['Counter']
                    G.edge[m][j]['Counter']=a+1
                    
                    f_active.append(j)  
           infect=[]
           for k in f_active:
                infect.append(k)
            
            
        
            
    
                
   
    
        
  

    

    

  

f=[]
for u,v in G.edges():
    data=G.edge[u][v]['Counter']
    f.append(data)
            
          
def histogram(s):
    d = dict()
    for c in s:
      if c not in d:
          d[c] = 1
      else:
          d[c] += 1
    return d            
    
f_values=histogram(f)
    #key:No. of times infected, value: No. of edges infected that many times


for key,value in sorted(f_values.items()):
      print(key,value)
            
            
x=[]
y=[]
for key,value in sorted(f_values.items()):
      x.append(value)
      y.append(key)

a=max(x)
b=max(y)  

plt.plot(y,x,'ro')
plt.axis([0, b+2, 0, a+4])
plt.show() 
           
           
        
           
      