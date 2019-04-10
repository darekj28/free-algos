

def subsets(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        return  [[nums[0]] + x for x in subsets(nums[1:])] + [x for x in subsets(nums[1:])]

if __name__ == "__main__":
	all_subsets = subsets(range(0,5))
	for subset in all_subsets:
		print(subset)