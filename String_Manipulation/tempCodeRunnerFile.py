class Solution:
    def findGoodPairs(self, a, n, k):
        ways=0
        array=a
        array.extend(a)
        for i in range (0,len(array)):
            if a[i+3]:
                if a[i]==a[i+3]:
                    ways+=1
        return ways

if __name__=='__main__':
    tc=int(input())
    while tc > 0:
        n, k=map(int,input().split())
        a=list(map(int, input().split()))
        ob=Solution()
        ans=ob.findGoodPairs(a,n,k)
        print(ans)
        tc-=1