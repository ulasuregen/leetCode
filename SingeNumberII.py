################################################################################################
# Given an integer array nums where every element appears three times except for one,
# which appears exactly once. Find the single element and return it.

# Input: nums = [2,2,3,2]
# Output: 3

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99

# Contraints 
# 1 <= nums.length <= 3 * 104
# -2^31 <= nums[i] <= 2^31 - 1
# !!! You must implement a solution with a linear runtime complexity and use only constant extra space. !!!

################################################################################################

# My First Attempt
def singleNumber1(nums):
        bitList = [0 for _ in range(33)]
    

        for n in nums:
            bit_arr = list(format(abs(n), '032b'))
            if n < 0:
                bit_arr.append('1')
            else:
                bit_arr.append('0')

            bitList = [a+int(b) for a,b in zip(bitList, bit_arr)]
        
        bitList = [str(n % 3) for n in bitList]

        res = int(''.join(bitList[:-1]),2)
        
        return -res if int(bitList[-1]) else res

# It just was counting set bits 
# Eg :- [2,2,2,3,4,4,4]
# binary form :- 010
# 010
# 010
# 011
# 100
# 100
# 100
# Total :- 3 4 1

# And then taking modulo 3 of each bit.
# The downside appears when handling negative numbers.
# I need to add an extra bit for it, 
# and it is also complicated to jump between bits, strings, and integers.

################################################################################################

# AMAZING SOLUTION !!!
def singleNumber2(nums):
        ones = 0
        twos = 0
        for i in range(len(nums)):
            ones = (ones ^ nums[i]) & ~twos
            twos = (twos ^ nums[i]) & ~ones
        return ones

# Just focus on a one bit now and oberseve what happens to it 
# first, may be bunch of 0's come in 
# this does not affect ones and twos, so they remain 0 and 0 
# (0 ^ 0) & ~0 = 0    (ones)
# (0 ^ 0) & ~0 = 0    (twos)
# ---------
# then first 1 come in 
# (0 ^ 1) & ~0 = 1    (ones)
# (0 ^ 1) & ~1 = 0    (twos)
# ---------
# a bunch of 0's come in again probably 
# (1 ^ 0) & ~0 = 1    (ones)
# (0 ^ 0) & ~1 = 0    (twos)
# ---------
# second coming 1
# (1 ^ 1) & ~0 = 0    (ones)
# (0 ^ 1) & ~0 = 1    (twos)
# ---------
# a bunch of 0's come in
# (0 ^ 0) & ~1 = 0    (ones)
# (1 ^ 0) & ~0 = 1    (twos)
# ---------
# third time coming 1
# (0 ^ 1) & ~1 = 0    (ones)
# (1 ^ 1) & ~0 = 0    (twos)
# which is the initial setting we had; thus, at every third occurrence of 1,
# we return to the initial setting, which is exactly what is needed in the first place to solve the question !

# To visualize: `ones` and `twos` start at 0.
# If the incoming bit is 0, nothing changes.
# If the incoming bit is 1:
#   - If the upper level is already set, do nothing (third occurrence).
#   - Otherwise, toggle the current level.
#   - If this is the second occurrence, update the upper level.

