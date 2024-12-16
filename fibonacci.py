def fibonacci_sequence():
    """Generator function that yields numbers in the Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def get_fibonacci_terms(n):
    """Return a list of the first n numbers in the Fibonacci sequence.
    
    Args:
        n (int): Number of terms to generate (must be > 0)
        
    Returns:
        list: First n numbers in the Fibonacci sequence
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Number of terms must be a positive integer")
        
    fib_gen = fibonacci_sequence()
    return [next(fib_gen) for _ in range(n)]

if __name__ == "__main__":
    # Example usage
    try:
        terms = get_fibonacci_terms(10)
        print(f"First 10 Fibonacci numbers: {terms}")
    except ValueError as e:
        print(f"Error: {e}")
