# @lc app=leetcode id=767 lang=python3
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        pq = [(-f, ch) for ch, f in freq.items()]
        heapq.heapify(pq)

        result = ""
        prev_freq, prev_ch = 0, None

        while pq:
            curr_freq, curr_ch = heapq.heappop(pq)
            result += curr_ch

            if prev_freq < 0:
                heapq.heappush(pq, (prev_freq, prev_ch))

            curr_freq += 1
            prev_freq, prev_ch = curr_freq, curr_ch

            if len(pq) == 1 and pq[0][0] < -1:
                return ""

        return result