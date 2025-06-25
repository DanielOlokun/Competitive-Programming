# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
#Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

   #  APPROACH 1 --- > this is the brute force solution --- > O(n1 x n2)
        result = []

        for num in nums1:

            index = nums2.index(num)

            for next_num in nums2[index + 1:]:
                if next_num > num:
                    result.append(next_num)
                    break
            else:
                result.append(-1)

        return result

    # APPROACH 2 ---> more efiicient solution --- > O(n + m)

# fyi - When I say 'match' -- > I mean next greater number

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        next_greater = {}    # dict to store num + next num greater
        stack = []    # keeps track of nums we have not found a match for - temporarily. Therefore, anything left here after necessary iterations, will get a '-1' as per q.

        for num in nums2:
            while stack and num > stack[-1]:    # while stack not empty and current num > top of stack, last number seen on stack without a match
              # these next 2 lines -- > when we have found the match
                prev = stack.pop()    # pop from stack
                next_greater[prev] = num  # the 'popped' num is matched with number in nums1
            # out of while loop -- > we have not found a match so we jus push to stack
            stack.append(num)

        for num in stack:
            next_greater[num] = -1    # any remaining num in stack gets -1  --- > no next greater element found

        return [next_greater[num] for num in nums1]  # simple list comp to get the next greater elements that were matched in next greater dict/hash map
