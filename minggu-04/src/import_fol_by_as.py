# If the module name is followed by as, then the name
# following as is bound direclty to the imported module
# in this case if fibo module is bound to name fib
import fibo as fib

# Call fib function to print Fibonnaci series up to 400
fib.fib(40)

# Call fib2 function to return Fibonnaci series up to 700
result = fib.fib2(100)
print(result)