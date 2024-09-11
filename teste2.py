def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

# Exemplo de uso
numero = 21  # Número a ser verificado
if is_fibonacci(numero):
    print(f"O número {numero} pertence a sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence a sequência de Fibonacci.")
