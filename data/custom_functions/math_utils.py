def moving_average(nums, window):
    return [sum(nums[i:i+window])/window for i in range(len(nums)-window+1)]