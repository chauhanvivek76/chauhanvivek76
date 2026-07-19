#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    long long maxTotalDiscount(std::vector<int>& prices, std::vector<int>& discounts, std::vector<int>& expires) {
        int n = prices.size();
        int m = discounts.size();
        
        // Step 1: Group coupons by their effective deadlines.
        // Since we only have n purchases, a deadline > n is effectively n.
        std::vector<std::vector<int>> buckets(n + 1);
        for (int i = 0; i < m; ++i) {
            int effective_expire = std::min(expires[i], n);
            buckets[effective_expire].push_back(discounts[i]);
        }
        
        // Step 2: Select the best coupons using a max-heap (priority_queue).
        // Iterate backwards from step n down to 1.
        std::priority_queue<int> max_heap;
        std::vector<int> selected_discounts;
        selected_discounts.reserve(n);
        
        for (int t = n; t >= 1; --t) {
            for (int discount : buckets[t]) {
                max_heap.push(discount);
            }
            if (!max_heap.empty()) {
                selected_discounts.push_back(max_heap.top());
                max_heap.pop();
            }
        }
        
        // Step 3: Sort prices and selected discounts in ascending order.
        std::sort(prices.begin(), prices.end());
        std::sort(selected_discounts.begin(), selected_discounts.end());
        
        // Step 4: Pair them up. We use long long to prevent overflow.
        long long total_discount = 0;
        int k = selected_discounts.size();
        for (int i = 0; i < k; ++i) {
            long long price = prices[n - k + i];
            long long discount = selected_discounts[i];
            total_discount += std::min(price, discount);
        }
        
        return total_discount;
    }
};
