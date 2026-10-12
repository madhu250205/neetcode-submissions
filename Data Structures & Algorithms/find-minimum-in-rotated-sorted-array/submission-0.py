class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # If the subsegment is already sorted, the leftmost element is the minimum of this partition
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])

            # Decide which half to search
            if nums[mid] >= nums[l]:
                # Left side is sorted, so minimum must be in the right unsorted half
                l = mid + 1
            else:
                # Right side is sorted, so minimum must be in the left unsorted half
                r = mid - 1

        return res