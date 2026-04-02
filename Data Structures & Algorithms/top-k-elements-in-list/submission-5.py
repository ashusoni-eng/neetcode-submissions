class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for n in nums:
            seen[n] = seen.get(n,0) + 1
        
        arr = sorted(seen.keys(), key=lambda x : seen[x], reverse = True)

        return arr[0:k]
        