# @lc app=leetcode id=952 lang=python3
class Solution:
    def largestComponentSize(self, nums):
        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent, size, i, j):
            root_i = find(parent, i)
            root_j = find(parent, j)
            if root_i != root_j:
                if size[root_i] < size[root_j]:
                    parent[root_i] = root_j
                    size[root_j] += size[root_i]
                else:
                    parent[root_j] = root_i
                    size[root_i] += size[root_j]

        def generate_primes(n):
            primes = []
            is_prime = [True] * (n + 1)
            p = 2
            while p * p <= n:
                if is_prime[p]:
                    for i in range(p * p, n + 1, p):
                        is_prime[i] = False
                p += 1
            for i in range(2, n + 1):
                if is_prime[i]:
                    primes.append(i)
            return primes

        primes = generate_primes(max(nums))
        prime_index = {prime: i for i, prime in enumerate(primes)}

        n = len(nums)
        parent = list(range(n))
        size = [1] * n

        for num in nums:
            for prime in primes:
                if prime > num:
                    break
                if num % prime == 0:
                    union(parent, size, nums.index(num), nums.index(prime))

        max_size = max(size)
        return max_size


solution = Solution()
print(solution.largestComponentSize([4, 6, 15, 35]))  # Output: 4
print(solution.largestComponentSize([20, 50, 9, 63]))  # Output: 2
print(solution.largestComponentSize([2, 3, 6, 7, 4, 12, 21, 39]))  # Output: 8