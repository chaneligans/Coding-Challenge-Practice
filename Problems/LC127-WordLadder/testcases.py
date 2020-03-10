from WordLadder import Solution
sol = Solution()

val = sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print(val==5,"Test 1: expected output: 5, actual output:", val)

val = sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])
print(val==0,"Test 2: expected output: 0, actual output:", val)
