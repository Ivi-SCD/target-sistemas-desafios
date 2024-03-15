def fibonacci(n):
    fib_array = [0,1]
    while fib_array[-1] < n:
        fib_array.append(fib_array[-1] + fib_array[-2])
    return fib_array

def pertence_a_fibonacci(num):
    fib_array = fibonacci(num)
    if num in fib_array:
        return True, fib_array
    return False, fib_array

numero = 30
numero_pertence, fib_array = pertence_a_fibonacci(numero)

if numero_pertence:
     print(f"{numero} pertence à sequência de Fibonacci: {fib_array}")
else:
    print(f"{numero} não pertence à sequência de Fibonacci: {fib_array}")
    