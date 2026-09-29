class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        greater = {}

        for x in nums2:
            while stack and x > stack[-1]:
                small = stack.pop()
                greater[small] = x
            stack.append(x)

        result = []

        for s in nums1:
            result.append(greater.get(s,-1))

        return result