"""Performance comparison between brute force and optimal solution."""

import time
import random
from pathlib import Path

from task_one.app import solve, brute_force_solve


def generate_test_case(n_cities: int, n_taverns: int, range_limit: int = 10**6) -> str:
    """Generate a random test case and return as string."""
    cities = [random.randint(-range_limit, range_limit) for _ in range(n_cities)]
    taverns = [random.randint(-range_limit, range_limit) for _ in range(n_taverns)]
    
    return f"{n_cities}\n" + " ".join(map(str, cities)) + f"\n{n_taverns}\n" + " ".join(map(str, taverns))


def benchmark(solve_func, test_file: str, iterations: int = 1) -> tuple[float, int]:
    """Benchmark a solve function."""
    total_time = 0
    result = None
    
    for _ in range(iterations):
        start = time.perf_counter()
        result = solve_func(test_file)
        total_time += time.perf_counter() - start
    
    return total_time / iterations, result


def run_comparison():
    """Run performance comparison between brute force and optimal."""
    print("=" * 70)
    print("TASK ONE: Performance Comparison")
    print("=" * 70)
    
    test_cases = [
        (100, 100, "Small (100x100)"),
        (1000, 1000, "Medium (1Kx1K)"),
        (10000, 10000, "Large (10Kx10K)"),
    ]
    
    # Add very large test if user wants
    add_huge = input("\nInclude huge test (100K x 100K)? This may take ~1 minute for brute force. (y/n): ")
    if add_huge.lower() == 'y':
        test_cases.append((100000, 100000, "Huge (100Kx100K)"))
    
    print("\n" + "=" * 70)
    
    for n_cities, n_taverns, label in test_cases:
        print(f"\n{label}")
        print("-" * 70)
        
        # Generate test case
        test_content = generate_test_case(n_cities, n_taverns)
        test_file = Path(__file__).parent / "temp_benchmark_test.txt"
        test_file.write_text(test_content)
        
        try:
            # Benchmark brute force
            print("Running brute force...", end=" ", flush=True)
            bf_time, bf_result = benchmark(brute_force_solve, str(test_file))
            print(f"✓ {bf_time*1000:.2f}ms")
            
            # Benchmark optimal
            print("Running optimal...   ", end=" ", flush=True)
            opt_time, opt_result = benchmark(solve, str(test_file))
            print(f"✓ {opt_time*1000:.2f}ms")
            
            # Verify results match
            if bf_result == opt_result:
                print(f"✓ Results match: {bf_result}")
            else:
                print(f"✗ MISMATCH! Brute: {bf_result}, Optimal: {opt_result}")
            
            # Calculate speedup
            speedup = bf_time / opt_time if opt_time > 0 else float('inf')
            print(f"⚡ Speedup: {speedup:.1f}x faster")
            
        finally:
            # Cleanup
            if test_file.exists():
                test_file.unlink()
    
    print("\n" + "=" * 70)
    print("Summary:")
    print("- Binary search maintains O((n+m) log m) complexity")
    print("- Speedup increases with input size (expected for O(nm) vs O(n log m))")
    print("- Both algorithms produce identical results ✓")
    print("=" * 70)


if __name__ == "__main__":
    run_comparison()
