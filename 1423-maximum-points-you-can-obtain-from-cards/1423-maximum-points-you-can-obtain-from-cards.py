class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)

        window_size = n - k

        total = sum(cardPoints)
        window_sum = sum(cardPoints[:window_size])
        min_sum = window_sum

        for right in range(window_size,n):
            window_sum += cardPoints[right]
            window_sum -= cardPoints[right - window_size]

            min_sum = min(min_sum,window_sum)

        return total - min_sum