class Solution:
    def catMouseGame(self, graph):
        n = len(graph)
        dp = [[[-1] * n for _ in range(n)] for _ in range(2*n)]
        
        return self.helper(graph, dp, 0, 1, 2)# 0-steps, 1=mouse's position, 2=cat's position
    
    def helper(self, graph, dp, t, m, c):
        if t == 2*len(graph): return 0 
		# termine as a draw! since both mouse and cat moved n steps (totally 2n steps) 
		# and still no winner or loser, then it is a draw
		
        if dp[t][m][c] != -1: return dp[t][m][c] # read from cache
        
        if m == 0: # m's position = hole, so mouse win
            dp[t][m][c] = 1 # mouse win
            return 1
        if m == c: # cat and mouse are at the same position, so cat win
            dp[t][m][c] = 2 # cat win
            return 2
        mouseTurn = (t % 2 == 0)
        if mouseTurn:
            catWin = True
            for i in range(len(graph[m])):
                nextRes = self.helper(graph, dp, t+1, graph[m][i], c)
                if nextRes == 1: # find a way that mouse win
                    dp[t][m][c] = 1
                    return 1
                elif nextRes != 2: # find a way that cat can not win
                    catWin = False
            if catWin:
                dp[t][m][c] = 2
                return 2 # under mouse's all available choices, cat will win, then return 2
            else:
                dp[t][m][c] = 0
                return 0
        else:
            mouseWin = True
            for i in range(len(graph[c])):
                if graph[c][i] == 0: continue # cat can not enter hole
                nextRes = self.helper(graph, dp, t+1, m, graph[c][i])
                if nextRes == 2: # find a way that cat can win
                    dp[t][m][c] = 2
                    return 2
                elif nextRes != 1: # find a way that mouse can not win
                    mouseWin = False
            if mouseWin:
                dp[t][m][c] = 1
                return 1 # under cat's al available choices, mouse will win, then return 1
            else:
                dp[t][m][c] = 0
                return 0
