
#######################################################

#Write a program to do the following:Given an array of random numbers, push all the zeros of a given array to the start of the array.
# The order of all other elements should be same.

#Example
#1: Input: {1, 2, 0, 4, 3, 0, 5, 0}
#Output: {0, 0, 0, 1, 2, 4, 3, 5}

#Example
#2:Input: {1, 2, 0, 0, 0, -1, 6}
#Output: {0, 0, 0, 1, 2, -1, 6}

#Example
#3:Input: {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}
#Output: {0, 0, 0, 0, 1, 9, 8, 4, 2, 7, 6}
###########################################
# ran the loop through reverse order
# swap the elements in the same position until the first zero element was found
#if the elements has non zero it swap the index

class Solution:
    def shiftposition(self, nums):
        pos = len(nums) - 1

        for i in reversed(range(len(nums))):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos -= 1

        return (nums)


if __name__ == '__main__':
    array = [1, 2, 0, 0, 0, -1, 6]
    sol = Solution()
    a = sol.shiftposition(array)
    print(a)
