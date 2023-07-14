def two_sum(nums, target)
    map = {}
    nums.each_with_index do |num, index|
        complement = target - num
        if map.include?(complement)
            return [map[complement], index]
        end
        map[num] = index
    end
end
