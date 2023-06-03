class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dp(curr, path):
            if curr > target:
                return
            if curr == target:
                res.append(path.copy())
                return
            for num in candidates:
                if len(path) == 0 or num >= path[-1]:
                    path.append(num)
                    dp(curr + num, path)
                    path.pop()
        
        dp(0, [])
        return res