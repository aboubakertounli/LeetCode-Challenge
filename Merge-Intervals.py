class Solution:
    def merge(self,l):
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
#exemple
s=Solution()
print(s.merge([[1,3],[2,6],[15,18],[8,10]]))
