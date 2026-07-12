class Solution(object):
    def fib(self, n):

        if n==0:
            return 0

        if n==1:
            return 1

        i=0
        j=1

        for a in range (2, n+1):
            k=i+j
            i=j
            j=k
        return k



