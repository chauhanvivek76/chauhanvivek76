import heapq
from typing import List

class Solution:
    def maxTotalDiscount(self, prices: List[int], discounts: List[int], expires: List[int]) -> int:
        n = len(prices)
        m = len(discounts)
        
        # Step 1: Bound coupon expiration counters.
        # Since we make exactly n purchases, any coupon with expires[j] > n
        # can be treated as if it expires at purchase n.
        effective_expires = [min(exp, n) for exp in expires]
        
        # Step 2: Group coupons by their effective deadlines.
        # buckets[t] will contain all discounts that expire at step t.
        buckets = [[] for _ in range(n + 1)]
        for i in range(m):
            buckets[effective_expires[i]].append(discounts[i])
            
        # Step 3: Select the best possible subset of coupons using a Max-Heap.
        # We iterate backwards from step n down to 1.
        # At step t, any coupon with expires >= t is eligible.
        selected_discounts = []
        max_heap = []  # Python's heapq is a min-heap; we push negative values to simulate a max-heap.
        
        for t in range(n, 0, -1):
            # Add all coupons that expire at step t to the heap
            for discount in buckets[t]:
                heapq.heappush(max_heap, -discount)
            
            # Greedily pick the coupon with the largest discount
            if max_heap:
                selected_discounts.append(-heapq.heappop(max_heap))
                
        # Step 4: Pair selected discounts with the largest prices.
        # Sort both prices and selected discounts in ascending order.
        prices.sort()
        selected_discounts.sort()
        
        # If we selected k coupons (k <= n), we pair them with the k largest prices
        # in ascending order to maximize the sum of min(price, discount).
        total_discount = 0
        k = len(selected_discounts)
        for i in range(k):
            price = prices[n - k + i]
            discount = selected_discounts[i]
            total_discount += min(price, discount)
            
        return total_discount
