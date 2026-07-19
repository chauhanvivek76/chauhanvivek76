# Editorial: Maximum Profit from Fading Coupons

## Intuition

The problem requires us to pair a set of items with a set of coupons to maximize the total discount. However, we have two main challenges:
1. **Deadlines:** Each coupon has an expiration counter. Since we purchase items one by one, a coupon used at the $t$-th purchase must have an expiration counter $\ge t$.
2. **Min-Discount Cap:** The discount we get by applying a coupon of value $D$ to an item of price $P$ is limited to $\min(P, D)$ (the price cannot go below zero).

We can decouple this problem into two independent steps:
1. **Coupon Selection:** Find the "best" set of at most $n$ coupons that can be legally scheduled without violating their expiration limits.
2. **Optimal Pairing:** Pair the selected coupons with the items in a way that maximizes the total discount.

---

## 1. Coupon Selection (Greedy with Max-Heap)

Since we have exactly $n$ items, we have $n$ available purchase slots, which we can label from $1$ to $n$. A coupon with expiration $E_j$ can be scheduled in any slot $s \le E_j$. If $E_j > n$, we can cap it to $n$, since we will never make more than $n$ purchases.

To select the most valuable coupons, we can work backwards from slot $n$ down to $1$:
* At slot $t$, any coupon with an expiration $\ge t$ is eligible to be scheduled.
* To maximize the discount, we should greedily pick the eligible coupon with the largest nominal discount.
* We can implement this by grouping coupons by their effective deadlines and maintaining a **Max-Heap** of available coupon values.

### Proof of Correctness (Scheduling Matroid)

This scheduling problem can be modeled as finding a maximum-weight independent set in a **Scheduling Matroid**:
* Let $U$ be the set of coupons.
* A subset of coupons $I \subseteq U$ is *independent* if there exists an assignment of coupons in $I$ to distinct slots in $\{1, \dots, n\}$ such that each coupon is placed in a slot $\le \text{expires}[j]$.
* Matroid theory guarantees that the greedy algorithm (using a max-heap) finds an independent set $D$ that lexicographically dominates any other independent set $D'$ of the same size. That is, if we sort the elements of both sets in ascending order:
  $$d_i \ge d'_i \quad \text{for all } 1 \le i \le |D|$$
* Since the actual discount function $\min(P, D)$ is monotonically non-decreasing with respect to $D$, choosing a set of coupon values that element-wise dominates any other valid set of coupons will always yield a total discount that is at least as large.

---

## 2. Optimal Pairing (Rearrangement Inequality)

Once we have selected a set of $k$ coupons ($k \le n$) with values $d_1 \le d_2 \le \dots \le d_k$, we must pair them with $k$ items.
* **Which items to choose:** To maximize $\sum \min(p_i, d_i)$, we should pair our coupons with the $k$ largest available prices in `prices`. If we chose any smaller price, the sum would only decrease or stay the same.
* **How to pair them:** Sort both the $k$ largest prices and the $k$ selected discounts in ascending order, and pair them one-to-one (i.e., pair the $i$-th smallest price with the $i$-th smallest discount).

### Mathematical Proof of Sorted Pairing

We want to show that for any two prices $P_1 \le P_2$ and two discounts $D_1 \le D_2$, the sorted pairing is always optimal:
$$\min(P_1, D_1) + \min(P_2, D_2) \ge \min(P_1, D_2) + \min(P_2, D_1)$$

**Case Analysis:**
1. If $P_1 \le D_1$:
   * Since $P_1 \le D_1 \le D_2$, we have $\min(P_1, D_1) = P_1$ and $\min(P_1, D_2) = P_1$.
   * The inequality reduces to:
     $$P_1 + \min(P_2, D_2) \ge P_1 + \min(P_2, D_1) \implies \min(P_2, D_2) \ge \min(P_2, D_1)$$
   * This is true because $D_2 \ge D_1$ and the $\min$ function is monotonic.
2. If $P_1 > D_1$:
   * Since $P_2 \ge P_1 > D_1$, we have $\min(P_2, D_1) = D_1$ and $\min(P_1, D_1) = D_1$.
   * The inequality reduces to:
     $$D_1 + \min(P_2, D_2) \ge \min(P_1, D_2) + D_1 \implies \min(P_2, D_2) \ge \min(P_1, D_2)$$
   * This is true because $P_2 \ge P_1$ and the $\min$ function is monotonic.

In both cases, sorting and pairing the elements in ascending order yields the optimal sum. By induction, this holds for any $k$ elements.

---

## Complexity Analysis

* **Time Complexity:**
  1. **Bounding and Grouping:** Bounding deadlines takes $O(M)$ time. Creating the buckets takes $O(M)$ time.
  2. **Greedy Scheduling:** Each of the $M$ coupons is pushed to and popped from the Max-Heap at most once. Total heap operations take $O(M \log M)$ time.
  3. **Sorting:** Sorting `prices` takes $O(N \log N)$ time. Sorting the selected coupons takes $O(N \log N)$ time.
  4. **Pairing:** Iterating and summing takes $O(N)$ time.
  
  **Total Time Complexity:** $O(N \log N + M \log M)$, which easily runs within the 2-second limit for $N, M = 10^5$.

* **Space Complexity:**
  * The buckets require $O(N + M)$ space.
  * The heap contains at most $M$ items, requiring $O(M)$ space.
  * The selected coupons list requires $O(N)$ space.
  
  **Total Space Complexity:** $O(N + M)$ auxiliary space.
