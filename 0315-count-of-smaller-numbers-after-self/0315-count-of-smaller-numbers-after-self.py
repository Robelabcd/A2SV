class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        indices = list(range(n))  #original indices

        def merge_sort(left, right):
            if right - left <= 1:  
                return
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid, right)
            
            temp = []
            i, j = left, mid
            while i < mid and j < right:
                if nums[indices[i]] <= nums[indices[j]]:
                    temp.append(indices[i])
                    counts[indices[i]] += j - mid
                    i += 1
                else:
                    temp.append(indices[j])
                    j += 1
            
            while i < mid:
                temp.append(indices[i])
                counts[indices[i]] += j - mid
                i += 1
            while j < right:
                temp.append(indices[j])
                j += 1
            
            indices[left:right] = temp

        merge_sort(0, n)
        return counts