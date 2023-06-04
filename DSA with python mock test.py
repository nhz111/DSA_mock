Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]


def moveZeroes(nums):
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    nums[left:] = [0] * (len(nums) - left)

# Example usage

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  


# Output: [1, 3, 12, 0, 0]

Example 2:
Input: nums = [0]
Output: [0]

def moveZeroes(nums):
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    nums[left:] = [0] * (len(nums) - left)

# Example usage
nums = [0]
moveZeroes(nums)
print(nums)  

# Output: [0]


########################################################################

# first unique character

def firstUniqChar(s):
    char_freq = {}

    # Count character frequencies
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    # Find first unique character
    for i, char in enumerate(s):
        if char_freq[char] == 1:
            return i

    return -1

# Example usage
s = "leetcode"
print(firstUniqChar(s))  

# Output: 0

s = "loveleetcode"
print(firstUniqChar(s))  

# Output: 2

s = "aabb"
print(firstUniqChar(s)) 
 
# Output: -1



