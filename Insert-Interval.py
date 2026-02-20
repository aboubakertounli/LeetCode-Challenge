class Solution:
    def insert(self, intervals , newInterval):
        l=intervals.copy()
        l.append(newInterval)
        m=sorted(l, key=lambda i:i[0])
        print(m)
        i=0
        while i<len(m)-1:
            if  m[i][1] >= m[i+1][1]:
                m.remove(m[i+1])
            elif m[i][1] >= m[i+1][0] :
                m[i][1]=m[i+1][1]
            else:
                i+=1
        return m
example=Solution()
print(example.insert([[1,3],[6,9]],[2,5]))
# output: [[1,5],[6,9]]
print(example.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
# output: [[1,2],[3,10],[12,16]]
print(example.insert([[1,5]],[2,3]))
# output: [[1,5]]
print(example.insert([[1,5]],[2,7]))
# output: [[1,7]]