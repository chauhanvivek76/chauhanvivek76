import json
import subprocess
import os
import random
import time
from solution import Solution

def generate_runner_cpp():
    runner_code = """
#include <iostream>
#include <vector>
#include "solution.cpp"

int main() {
    int n, m;
    if (!(std::cin >> n >> m)) return 0;
    std::vector<int> prices(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> prices[i];
    }
    std::vector<int> discounts(m);
    for (int i = 0; i < m; ++i) {
        std::cin >> discounts[i];
    }
    std::vector<int> expires(m);
    for (int i = 0; i < m; ++i) {
        std::cin >> expires[i];
    }
    
    Solution solver;
    std::cout << solver.maxTotalDiscount(prices, discounts, expires) << std::endl;
    return 0;
}
"""
    with open("runner.cpp", "w") as f:
        f.write(runner_code)

def run_cpp_solver(prices, discounts, expires):
    # Formulate stdin input
    input_data = f"{len(prices)} {len(discounts)}\n"
    input_data += " ".join(map(str, prices)) + "\n"
    input_data += " ".join(map(str, discounts)) + "\n"
    input_data += " ".join(map(str, expires)) + "\n"
    
    # Run the compiled binary
    process = subprocess.Popen(["./runner"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=input_data)
    if process.returncode != 0:
        raise RuntimeError(f"C++ runner failed: {stderr}")
    return int(stdout.strip())

def main():
    # 1. Compile C++ solution
    print("Compiling C++ solution...")
    generate_runner_cpp()
    try:
        subprocess.run(["g++", "-O3", "runner.cpp", "-o", "runner"], check=True, capture_output=True)
        print("C++ solution compiled successfully.")
    except Exception as e:
        print(f"Error compiling C++: {e}")
        return

    # 2. Load test cases
    with open("test_cases.json", "r") as f:
        test_cases = json.load(f)

    # 3. Run validation tests
    py_solver = Solution()
    failed = False
    
    print("\n--- Running Validation Tests ---")
    for tc in test_cases:
        name = tc["name"]
        prices = tc["prices"]
        discounts = tc["discounts"]
        expires = tc["expires"]
        expected = tc["expected"]
        
        # Test Python
        try:
            py_res = py_solver.maxTotalDiscount(list(prices), list(discounts), list(expires))
        except Exception as e:
            py_res = f"ERROR: {e}"
            
        # Test C++
        try:
            cpp_res = run_cpp_solver(prices, discounts, expires)
        except Exception as e:
            cpp_res = f"ERROR: {e}"
            
        py_status = "PASS" if py_res == expected else "FAIL"
        cpp_status = "PASS" if cpp_res == expected else "FAIL"
        
        print(f"Test '{name}':")
        print(f"  Expected: {expected}")
        print(f"  Python:   {py_res} ({py_status})")
        print(f"  C++:      {cpp_res} ({cpp_status})")
        
        if py_status == "FAIL" or cpp_status == "FAIL":
            failed = True

    # 4. Large scale benchmark (N = 10^5, M = 10^5)
    print("\n--- Running Large Scale Benchmark (N = 10^5, M = 10^5) ---")
    n = 100000
    m = 100000
    prices = [random.randint(1, 10**9) for _ in range(n)]
    discounts = [random.randint(1, 10**9) for _ in range(m)]
    expires = [random.randint(1, n + 50000) for _ in range(m)]
    
    # Measure Python time
    start = time.time()
    try:
        py_res = py_solver.maxTotalDiscount(list(prices), list(discounts), list(expires))
        py_time = time.time() - start
        print(f"Python solved in {py_time:.4f} seconds (Result: {py_res})")
    except Exception as e:
        print(f"Python failed on large benchmark: {e}")
        
    # Measure C++ time
    start = time.time()
    try:
        cpp_res = run_cpp_solver(prices, discounts, expires)
        cpp_time = time.time() - start
        print(f"C++ solved in {cpp_time:.4f} seconds (Result: {cpp_res})")
        if py_res == cpp_res:
            print("Python and C++ results match on the large benchmark!")
        else:
            print(f"WARNING: Results mismatch! Python: {py_res}, C++: {cpp_res}")
            failed = True
    except Exception as e:
        print(f"C++ failed on large benchmark: {e}")

    # Cleanup
    if os.path.exists("runner"):
        os.remove("runner")
    if os.path.exists("runner.cpp"):
        os.remove("runner.cpp")
        
    if failed:
        print("\nVerification FAILED.")
    else:
        print("\nAll checks passed successfully!")

if __name__ == "__main__":
    main()
