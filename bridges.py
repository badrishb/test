n=4
con=[[0,1],[1,2],[2,0],[1,3]]
g=[{} for i in range(n)]
for pair in con:
    g[pair[0]][pair[1]]=1
    g[pair[1]][pair[0]]=1
st=[0]
vis=[0]*n
low=[0]*n
disc=[float('inf')]*n
count=0
ans=[]
ed=[]
# print(g)
while(len(st)>0):
    if(vis[st[-1]]==0):
        node=st[-1]
        if(disc[node]>count):
            disc[node]=count
            low[node]=count
            count+=1
        temp=len(ed)-1
        for nei in g[node]:
            if(disc[nei]>disc[node] and vis[nei]==0 ):
                ed.append((node,nei))
                st.append(nei)
            else:
                if(len(ed)>0):
                    print(">",node,nei,ed,low[node],disc[nei])
                if not(len(ed)==0 or nei==ed[temp][0]):
                    low[node]=min(low[node],low[nei])
        if(st[-1]==node):
            vis[node]=1
            if(len(st)>1 and low[node]>disc[ed[-1][0]]):
                print(node,low[node],ed,disc[ed[-1][0]])
                ans.append(ed[-1])        

    else:
        if(len(ed)>0):
            ed.pop()
        st.pop()
print(ans)
        

