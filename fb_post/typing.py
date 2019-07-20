from typing import Generator


def fib(n: int) -> Generator:
    a: int = 0
    b: int = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print([n for n in fib(17)])
