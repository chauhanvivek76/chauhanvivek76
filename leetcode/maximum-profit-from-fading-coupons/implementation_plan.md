# Implementation Plan - LeetCode Problem Proposal: "Maximum Profit from Fading Coupons"

We will design and document a complete, high-quality LeetCode problem proposal for **"Maximum Profit from Fading Coupons"**. This includes the problem description, example cases, constraints, a rigorous correctness proof of the greedy + max-heap approach, reference solutions in Python and C++, a test case generator, and a local verification script.

## Proposed Files

We will create a structured folder containing all submission components:
- [problem_description.md](file:///Users/vivekchauhan/.gemini/antigravity/brain/b54db6f3-2e38-4bf2-bac0-9d7fe73a7bf7/problem_description.md): The official problem statement, examples, and constraints.
- [solution.py](file:///Users/vivekchauhan/.gemini/antigravity/brain/b54db6f3-2e38-4bf2-bac0-9d7fe73a7bf7/solution.py): Clean Python solution with detailed comments.
- [solution.cpp](file:///Users/vivekchauhan/.gemini/antigravity/brain/b54db6f3-2e38-4bf2-bac0-9d7fe73a7bf7/solution.cpp): Optimal C++ solution.
- [editorial.md](file:///Users/vivekchauhan/.gemini/antigravity/brain/b54db6f3-2e38-4bf2-bac0-9d7fe73a7bf7/editorial.md): Mathematical proof of the greedy choice and step-by-step explanation.
- [test_cases.json](file:///Users/vivekchauhan/.gemini/antigravity/brain/b54db6f3-2e38-4bf2-bac0-9d7fe73a7bf7/test_cases.json): A set of test cases including normal, edge (single item/coupon, all expiring immediately), and large-scale random test cases.
- [verify.py](file:///Users/vivekchauhan/.gemini/antigravity/brain/b54db6f3-2e38-4bf2-bac0-9d7fe73a7bf7/verify.py): Script to validate solutions against the test cases.

---

## Proposed Changes

### [NEW] [problem_description.md](file:///Users/vivekchauhan/.gemini/antigravity/brain/b54db6f3-2e38-4bf2-bac0-9d7fe73a7bf7/problem_description.md)
Contains the LeetCode-style problem statement:
- **Title**: Maximum Profit from Fading Coupons
- **Task**: Find the maximum total discount obtained by ordering $N$ purchases and applying $M$ coupons with deadlines.
- **Constraints**: $N, M \le 10^5$, values up to $10^9$.
- **Examples**: Two detailed examples with explanations.

### [NEW] [solution.py](file:///Users/vivekchauhan/.gemini/antigravity/brain/b54db6f3-2e38-4bf2-bac0-9d7fe73a7bf7/solution.py)
Python implementation using:
1. Effective deadline bounding: `expires[i] = min(expires[i], n)`.
2. Deadline bucketing / grouping.
3. Max-Heap (simulated with `heapq` using negative values) to select the optimal subset of coupons.
4. Sorting both the selected coupons and `prices` to maximize the paired sum: $\sum \min(price_i, discount_i)$.

### [NEW] [solution.cpp](file:///Users/vivekchauhan/.gemini/antigravity/brain/b54db6f3-2e38-4bf2-bac0-9d7fe73a7bf7/solution.cpp)
C++ implementation using `std::priority_queue` and standard library sorts, ensuring it compiles and runs within $O(N \log N + M \log M)$ time and $O(N + M)$ space.

### [NEW] [editorial.md](file:///Users/vivekchauhan/.gemini/antigravity/brain/b54db6f3-2e38-4bf2-bac0-9d7fe73a7bf7/editorial.md)
Detailed explanation of:
- Why the scheduling problem reduces to a Matroid optimization (independent unit jobs with deadlines).
- Why the greedy selection of discounts is globally optimal.
- Proof of the sorted pairing strategy (Rearrangement Inequality variant).
- Complexity analysis.

### [NEW] [verify.py](file:///Users/vivekchauhan/.gemini/antigravity/brain/b54db6f3-2e38-4bf2-bac0-9d7fe73a7bf7/verify.py) & [test_cases.json](file:///Users/vivekchauhan/.gemini/antigravity/brain/b54db6f3-2e38-4bf2-bac0-9d7fe73a7bf7/test_cases.json)
Automated validation to verify that:
- The Python and C++ implementations yield identical results.
- Solutions run fast on large inputs ($10^5$ items and coupons).
- Edge cases (like empty lists, huge numbers, all coupons expiring at $t=1$) are correctly handled.

---

## Verification Plan

### Automated Tests
- Run `verify.py` to check the correctness of both Python and C++ solutions on all test cases.
- We will measure runtime on a generated test case of size $10^5$ to guarantee it meets LeetCode's 2-second limit.
