class Solution:
    def sortArray(self, nums):
        temp = [0] * len(nums)

        def merge_sort(left, right):
            if left >= right:
                return

            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)

            merge(left, mid, right)

        def merge(left, mid, right):
            i = left
            j = mid + 1
            k = left

            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1

            while i <= mid:
                temp[k] = nums[i]
                i += 1
                k += 1

            while j <= right:
                temp[k] = nums[j]
                j += 1
                k += 1

            for i in range(left, right + 1):
                nums[i] = temp[i]

        merge_sort(0, len(nums) - 1)
        return nums