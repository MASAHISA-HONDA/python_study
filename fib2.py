def fib2(n):
    if n<2 :
        return n
    return fib2(n-2)+fib2(n-1)

if __name__ == "__main__":
    print("フィボナッチ関数の計算")
    print("項=5")
    print(fib2(5))
    print("項=11")
    print(fib2(11))
    print("項=0")
    print(fib2(0))