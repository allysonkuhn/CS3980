#fib.py

from functools import lru_cache
import time
import matplotlib.pyplot as plt

times = []                                                              # List to store execution times for each Fibonacci calculation
ns = []                                                                 # List to store the corresponding Fibonacci indices (n values)

def timer(func):
    """Decorator to measure execution time of a function."""
    
    def wrapper(n):
        start = time.perf_counter()
        result = func(n)                                                # Call the original function and store the result
        end = time.perf_counter()
        elapsed = end - start                                           # Calculate the elapsed time for the function execution 
        
        print(f"Finished in {elapsed:.8f}s: f({n}) -> {result}")
        
        ns.append(n)                                                    # Append the Fibonacci index (n) to the list of indices
        times.append(elapsed)                                           # Append the elapsed time to the list of times                                       
        
        return result
    return wrapper


@lru_cache
@timer
def fib(n: int) -> int:
    """Compute nth Fibonacci number recursively."""
    if n <= 1:
        return n
    
    return fib(n-1) + fib(n-2)                                          # Recursive calls to compute the Fibonacci number, which will be cached by the lru_cache decorator to optimize performance


if __name__ == "__main__":
    fib(100)

    plt.figure(figsize=(10, 6))
    plt.plot(ns, times, linewidth=2)
    plt.xlabel("n (Fibonacci index)")
    plt.ylabel("Time (seconds)")
    plt.title("Execution Time of Fibonacci with LRU Cache")
    plt.grid(True, alpha=0.3)
    plt.savefig("fib.png", dpi=150, bbox_inches='tight')