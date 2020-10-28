def fib(n): # write Fibonnaci series up to n
    """Print a Fibonnaci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)