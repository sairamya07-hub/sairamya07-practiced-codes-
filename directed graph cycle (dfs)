class Solution:
    def isCyclic(self, V, edges):
        # code here
        def dfs(node):
            vis[node]=1
            pathvis[node]=1
            for adjNode in adj[node]:
                if(vis[adjNode]==0):
                    if(dfs(adjNode)):
                        return True
                elif(vis[adjNode]==1):
                    if(pathvis[adjNode]==1):
                        return True
            pathvis[node]=0
            return
        adj=[]
        for _ in range(0,V):
            adj.append([])
        for u,v in edges:
            adj[u].append(v)
        vis=[0]*V
        pathvis=[0]*V
        for n in range(0,V):
            if(vis[n]==0):
                if(dfs(n)):
                    return True
        return False
