# Task One: Taverns - Solution Analysis

## Problem Summary
Find the maximum distance from any city to its nearest tavern on a 1D number line.

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | 10^5 Operations |
|----------|----------------|------------------|-----------------|
| Brute Force | O(n × m) | O(n) | ~10^10 ops (10-100s) |
| **Binary Search** | **O((n+m) log m)** | **O(n)** | **~10^6 ops (<0.01s)** |

### Why Binary Search Wins

**Brute Force Problem:**
- For each city, checks EVERY tavern
- 100,000 cities × 100,000 taverns = 10 billion comparisons
- Even at 1 billion ops/sec, this takes 10+ seconds

**Binary Search Solution:**
- Sort taverns once: 100,000 × log(100,000) ≈ 1.7 million ops
- For each city, binary search: 100,000 × log(100,000) ≈ 1.7 million ops  
- Total: ~3.4 million operations → **~3,000x faster!**

## Algorithm Visualization

### Example Walkthrough
```
Sorted Taverns: [0, 1, 3, 6, 7, 8, 9, 10]
City at position 4:

Step 1: Binary search finds insertion index
  [0, 1, 3, | 6, 7, 8, 9, 10]
           idx=3 (4 would go here)

Step 2: Check neighbors
  Left:  taverns[2] = 3  →  |4-3| = 1  ✓ (nearest)
  Right: taverns[3] = 6  →  |4-6| = 2

Step 3: Minimum distance = 1
```

### Why Only Two Candidates?

**Mathematical Proof:**
Given sorted taverns `t₁ ≤ t₂ ≤ ... ≤ tₘ` and city `c`:

Let `tᵢ ≤ c < tᵢ₊₁`

For any tavern `tⱼ where j < i`:
- `|c - tⱼ| = c - tⱼ` (since tⱼ < c)
- `|c - tᵢ| = c - tᵢ` (since tᵢ < c)
- `tⱼ < tᵢ < c` implies `c - tⱼ > c - tᵢ`
- Therefore `tᵢ` is always closer than any earlier tavern

Similarly for `j > i+1`, `tᵢ₊₁` is always closer.

**Conclusion:** Only immediate neighbors matter!

## Binary Search Deep Dive

### Python's `bisect_left`

```python
bisect_left([0, 1, 3, 6, 7, 8, 9, 10], 4)
# Returns: 3 (index where 4 should be inserted)
```

**Key Property:**
- If `city` is at position `idx`, then:
  - `taverns[idx-1] ≤ city` (left neighbor)
  - `taverns[idx] ≥ city` (right neighbor)

### Edge Cases Handled

1. **City before all taverns** (`idx = 0`):
   - No left neighbor
   - Only check `taverns[0]`

2. **City after all taverns** (`idx = len(taverns)`):
   - No right neighbor
   - Only check `taverns[-1]`

3. **City exactly at tavern**:
   - Either left or right will have distance 0
   - min(0, something) = 0 ✓

4. **Single tavern**:
   - Always check it (covered by idx bounds)

## Competitive Programming Tips

### 1. **Always Sort for Range Queries**
When dealing with "nearest" problems on a line:
- Sorting enables O(log n) lookups
- Cost is O(n log n) but amortized across queries

### 2. **Binary Search Variations**
```python
import bisect

# Find leftmost position
idx = bisect.bisect_left(arr, val)

# Find rightmost position  
idx = bisect.bisect_right(arr, val)

# Find exact match
idx = bisect.bisect_left(arr, val)
if idx < len(arr) and arr[idx] == val:
    # Found exact match
```

### 3. **Two-Pointer Alternative**
For this problem, you could also use two pointers:
```python
sorted_cities = sorted(unique_cities)
i, j = 0, 0  # pointers for cities and taverns

for city in sorted_cities:
    # Move j to nearest tavern
    while j < len(taverns) and taverns[j] < city:
        j += 1
    # Check neighbors at j-1 and j
```
**Same O((n+m) log(n+m)) complexity** due to sorting both arrays.

### 4. **When to Use Each Approach**

| Scenario | Best Approach |
|----------|--------------|
| One sorted, one query set | Binary search (this problem) |
| Both need processing | Two pointers |
| Online queries (streaming) | Binary search trees / segment trees |
| 2D nearest neighbor | KD-trees, quadtrees |

## Performance Benchmarks

### Expected Times (Python)

| Input Size | Brute Force | Binary Search | Speedup |
|------------|-------------|---------------|---------|
| n=100, m=100 | <1ms | <1ms | ~1x |
| n=1K, m=1K | ~10ms | <1ms | ~10x |
| n=10K, m=10K | ~1s | ~5ms | ~200x |
| n=100K, m=100K | ~100s | ~50ms | **~2000x** |

### Why Binary Search Scales

```
Brute Force: O(n × m)
  10x input → 100x time (quadratic scaling)

Binary Search: O(n log m + m log m)  
  10x input → ~13x time (logarithmic scaling)
```

## Code Optimizations Used

1. **Set for deduplication**: O(n) instead of O(n²) list uniqueness
2. **Single sort**: Only taverns need sorting (queries remain unsorted)
3. **Early termination**: `min_distance` could break early if 0 found (marginal gain)
4. **In-place operations**: No extra arrays created

## Further Optimizations (Overkill for This Problem)

### If n, m were 10^6+:
1. **Parallel processing**: Divide cities into chunks, process in parallel
2. **SIMD operations**: Use NumPy for vectorized distance calculations
3. **Cache optimization**: Process cities in sorted order for better cache locality

### Space-Time Tradeoffs:
- Could precompute distance matrix: O(n×m) space for O(1) queries
- Not worth it here since we only query once per city

## Conclusion

**This binary search solution is the standard optimal approach** for nearest neighbor problems on a 1D line. It's:
- ✅ **Fast**: O((n+m) log m) vs O(n×m)
- ✅ **Simple**: Uses standard library (`bisect`)
- ✅ **Robust**: Handles all edge cases
- ✅ **Scalable**: Works up to maximum constraints

**For the competition, this solution should be:**
- Fast enough for any test case (under 100ms)
- Memory efficient (under 10MB)
- Easy to debug and verify

No further optimization needed! 🏆
