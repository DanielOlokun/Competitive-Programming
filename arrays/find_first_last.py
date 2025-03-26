
# How i solved the question
def searchRange(self, nums, target):
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            first = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

                if nums[mid] == target:
                    first = mid

            return first

        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            last = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

                if nums[mid] == target:
                    last = mid

            return last
        return [find_first(nums, target), find_last(nums, target)]

# another way of doing it

import bisect

def search_range(nums, target):
    left = bisect.bisect_left(nums, target)  # Find first occurrence (or insert position)
    right = bisect.bisect_right(nums, target) - 1  # Find last occurrence

    if left <= right and left < len(nums) and nums[left] == target:
        return [left, right]
    else:
        return [-1, -1]

# both are O(log n)
# import bisect is very useful for working with sorted arrays -- **NB**
