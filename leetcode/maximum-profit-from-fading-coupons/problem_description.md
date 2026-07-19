# Maximum Profit from Fading Coupons

**Difficulty:** Medium  
**Topics:** Array, Greedy, Sorting, Heap (Priority Queue)

---

## Problem Description

You have `n` items you want to buy. The price of the `i`-th item is `prices[i]`.

You are also given two integer arrays `discounts` and `expires`, both of length `m`. The `j`-th coupon offers a discount of `discounts[j]` dollars, but it has an expiration counter of `expires[j]` purchases. This means that you can only use the `j`-th coupon within your first `expires[j]` purchases (i.e., at or before the `expires[j]`-th item is bought).

* Each time you buy an item, the expiration counters of all unused coupons decrement by `1`.
* When a coupon's counter reaches `0`, it expires and can no longer be used.
* You can buy the items in any order you choose.
* You can apply at most one coupon to each item.
* If you apply a coupon with discount `D` to an item with price `P`, the final price of the item becomes `max(0, P - D)`. The actual discount obtained is `min(P, D)`.

Return *the **maximum total discount** you can obtain after purchasing all `n` items*.

---

### Example 1

**Input:**  
`prices = [100, 80]`  
`discounts = [50, 60]`  
`expires = [1, 2]`  

**Output:**  
`110`  

**Explanation:**  
* **Purchase 1:** Buy the item with price `80`, and apply the `0`-th coupon (discount = `50`, expires = `1`). The actual discount is `min(80, 50) = 50`.
* **Purchase 2:** Buy the item with price `100`, and apply the `1`-st coupon (discount = `60`, expires = `2`). The actual discount is `min(100, 60) = 60`.
* The total discount is `50 + 60 = 110`.
* *Note:* If we bought the `100` item first with the `50` coupon, and the `80` item second, the `60` coupon could still be used (since its expiration is `2`), but the total discount would be `min(100, 50) + min(80, 60) = 50 + 60 = 110`. If we bought the `100` item first with the `60` coupon, the `50` coupon would expire (as `expires[0] = 1`), leaving us unable to use it on the second item.

---

### Example 2

**Input:**  
`prices = [10, 20, 30]`  
`discounts = [15, 25]`  
`expires = [1, 1]`  

**Output:**  
`25`  

**Explanation:**  
* Both coupons expire after the `1`-st purchase. Therefore, we can use at most one coupon on the first purchase. The remaining two purchases must be paid in full without any coupons.
* To maximize the discount, we buy the item with price `30` first and apply the coupon with discount `25`. The actual discount is `min(30, 25) = 25`.
* The total discount is `25`.

---

## Constraints

* `n == prices.length`
* `m == discounts.length == expires.length`
* `1 <= n, m <= 10^5`
* `1 <= prices[i] <= 10^9`
* `1 <= discounts[j] <= 10^9`
* `1 <= expires[j] <= 10^9`
