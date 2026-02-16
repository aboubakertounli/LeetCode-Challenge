import heapq
def topKFrequent(nums, k):
        d={}
        for i in nums:
            if i not in d: d[i]=1
            else : d[i]+=1
        heap = []
        for num, freq in d.items():
            heapq.heappush(heap, (freq, num))  # push tuple (freq, num)
            if len(heap) > k:
                heapq.heappop(heap)            # remove smallest frequency
        return [num for freq, num in heap]

# Example usage:
nums = [1,1,1,2,2,3]
k = 2
result = topKFrequent(nums, k)
print(result)  # Output: [1, 2] (the top 2 frequent elements are 1 and 2)
nums = [1]
k = 1
result = topKFrequent(nums, k)
print(result)  # Output: [1] (the top 1 frequent element is 1)
nums = [1,2]
k = 2
result = topKFrequent(nums, k)
print(result)  # Output: [1, 2] (the top 2 frequent elements are 1 and 2)