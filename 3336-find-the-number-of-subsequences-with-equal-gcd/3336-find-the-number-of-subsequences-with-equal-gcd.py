class Solution:
    MOD = 10 ** 9 + 7

    def subsequencePairCount(self, nums: List[int]) -> int:

        @cache
        def solve(i, first, second):
            # first = GCD of first subsequence
            # second = GCD of second subsequence

            if i == len(nums):
                return int(first != 0 and second != 0 and first == second)

            # Don't include current element
            skip = solve(i + 1, first, second)

            # Include in first subsequence
            take1 = solve(i + 1, math.gcd(first, nums[i]), second)

            # Include in second subsequence
            take2 = solve(i + 1, first, math.gcd(second, nums[i]))

            return (skip + take1 + take2) % self.MOD

        return solve(0, 0, 0)
        