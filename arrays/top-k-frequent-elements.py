# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# use dict to make use of keys, values 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        return sorted(counts, key=counts.get, reverse=True)[:k]

  # returns k amount of keys with highest values  ***NOTE 'key=counts.get'
