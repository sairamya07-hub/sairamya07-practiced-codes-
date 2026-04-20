from collections import deque
class Solution:
	def isCycle(self, V, edges):
		adj = [] 
		for _ in range(V):
		    adj.append([])
		for n,m in edges:
		    adj[n].append(m)
		    adj[m].append(n)
		vis = [0]*V
		for n in range(0,V):   # unconnected graphs 
		    if(vis[n] == 0):
        		vis[n] = 1 
        		q = deque([]) 
        		q.append((n,-1)) 
        		while(len(q)>0):
        		    node,parent = q.popleft() 
        		    for i in adj[node]:
        		        if(vis[i] == 0):
        		            vis[i] = 1 
        		            q.append((i,node)) 
        		        elif(vis[i] == 1):
        		            if(i!=parent):
        		                return True 
        return False
