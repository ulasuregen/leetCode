#Brilliant Algorithm !!! 
def allSubsets(nums):
    all_subsets = [[]]

    for x in nums:
        all_subsets += [s + [x] for s in all_subsets]
    
    return all_subsets


nums = [1,2,3,4]
print(allSubsets(nums))


# My first attempt involved iterating over all binary sequences.
# Here is my solution. The one above is not mine :'( unfortunately lol 

def subsets( nums):
    all_permutations = []
    n = len(nums)
    binary = [0 for i in range(n)]
    
    for i in range(2**n):
        all_permutations.append([])

        for b in reversed(range(len(binary))):
            if(binary[b] == 1):
                all_permutations[-1].append(nums[b])
            
        for b in reversed(range(len(binary))):
            if(binary[b] == 0):
                binary[b] = 1
                break
            else:
                binary[b] = 0
        
    return all_permutations

nums = [1,2,3,4]
print(subsets(nums))