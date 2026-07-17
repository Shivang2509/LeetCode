class Solution(object):
    def intersect(self, nums1, nums2):
        stack=[]
        ans=[]
        for i in nums1:
            stack.append(i)

        for a in nums2:
            if a in stack:
                ans.append(a)
                stack.remove(a)

        return ans

        