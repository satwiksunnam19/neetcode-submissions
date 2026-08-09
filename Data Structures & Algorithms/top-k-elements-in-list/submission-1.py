from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        # freq_dict=dict(freq)
        # print(freq_dict)
        sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k])
        sorted_freq=list(sorted_freq.keys())
        return sorted_freq
