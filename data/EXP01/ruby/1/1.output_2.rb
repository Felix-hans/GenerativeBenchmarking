def two_sum(nums, target)
    num_hash = {}
    
    nums.each_with_index do |num, index|
        complement = target - num
        if num_hash.include?(complement)
            return [num_hash[complement], index]
        end
        num_hash[num] = index
    end
    
    return []
end