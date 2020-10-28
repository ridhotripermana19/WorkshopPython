# Fibonacci numbers module
# Print the Fibonnaci series up to n
def fib(n):
    ''' Write Fibonnacci series up to n and print the result'''
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a+b
    print()

# Fibonacci numbers module
# Return the Fibbonaci series up to n as result
def fib2(n):
    ''' Write Fibonnacci series up to n and return the result value'''
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# Make a file usable as a script only if the module
# is executed as the "main" file
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))