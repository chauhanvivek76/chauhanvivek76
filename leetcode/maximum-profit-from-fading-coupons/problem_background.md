# Question Background: Maximum Profit from Fading Coupons

This document provides the necessary background context, motivation, and educational value of the problem to satisfy LeetCode's question contribution requirements.

---

## 1. Real-World Motivation & Context
In modern e-commerce platforms (e.g., Amazon, Shopify, or loyalty systems), users are frequently awarded dynamic, time-sensitive coupons. 
* Many coupons have a "fading" property—they are valid only for a certain number of transactions before they expire.
* Every time a user makes a transaction, the expiration counters of their unused coupons decrement by 1.
* A coupon's value is often capped at the price of the item to which it is applied (an item's price cannot go below $0$).

To help shoppers maximize their savings (or to help platforms build recommendation algorithms that suggest optimal check-out ordering), we must solve a resource-allocation optimization problem. This problem models that exact scenario: ordering a list of purchases and matching them with fading coupons to maximize the total discount.

---

## 2. Educational & Algorithmic Value
This problem is an excellent fit for LeetCode's medium-difficulty category because it teaches and tests several core computer science concepts:

### A. Greedy Scheduling (Matroid Theory)
Candidates must realize that the coupon selection process maps to the classic **Unit-Job Scheduling with Deadlines** problem. 
* Because scheduling unit-time jobs with deadlines forms a **Matroid**, the greedy strategy (processing slots backwards using a Max-Heap) is mathematically guaranteed to find the globally optimal subset of coupons.
* This reinforces the candidate's understanding of greedy choice properties and how to prove them.

### B. Monotonic Pairing (Rearrangement Inequality)
Candidates must prove that once $k$ coupons are selected, the optimal way to pair them with items is to sort both the $k$ largest prices and the $k$ coupons in ascending order and match them one-to-one.
* This introduces candidates to a discrete application of the **Rearrangement Inequality** under a non-linear bounding function ($\min(P, D)$).

### C. Complexity Bounding and Data Structures
To pass within the $2$-second limit for $10^5$ items:
* A naive $O(N^2)$ simulation will Time Limit Exceeded (TLE).
* Candidates must design an $O(N \log N + M \log M)$ algorithm using **Bucketing (for grouping deadlines)** and a **Priority Queue / Max-Heap** to manage active coupons.

---

## 3. Uniqueness on LeetCode
While LeetCode has several scheduling and greedy problems (like *Task Scheduler* or *Minimum Number of Taps to Open to Water a Garden*), it lacks a problem that combines:
1. **Unit deadline scheduling** (where deadlines decrement with each step).
2. **Multi-dimensional pairing** under a non-linear upper bound constraint ($\min(P, D)$).

This combination presents a fresh, elegant challenge that cannot be solved by simply copy-pasting code from existing LeetCode solutions, making it an excellent candidate for technical interviews and contests.
