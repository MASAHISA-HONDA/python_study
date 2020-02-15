from typing import Generator

def fib6(n:int) -> Generator[int,None,None]:
    yield 0
    if n >0 :
        yield
    last:int = 0
    next:int = 1
    for _ in range(1,n):
        last,next = next,last+next
        yield next

if __name__ == "__main__":
    for i in fib6(100):
        print(i)