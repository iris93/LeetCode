class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        totallen = len1+len2
        halflen = int(totallen/2)
        i = 0
        j = 0
        result = {}
        while i<len1 or j <len2:
            if i == len1:
                result[i+j] = nums2[j]
                j = j+1;
            elif j == len2:
                result[i+j] = nums1[i]
                i = i+1;
            elif nums1[i] > nums2[j]:
                result[i+j] = nums2[j]
                j = j+1;
            else:
                result[i+j] = nums1[i]
                i = i+1;
        Median = 0.5*(result[halflen]+result[totallen-1-halflen])
        return Median
print 0.5*(2+3)
