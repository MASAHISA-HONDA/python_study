def calculate_pi(n_temp :int) -> float:
    #numerator=分子
    #denominator=分母
    numerator:float = 4.0
    denominator:float = 1.0
    operation:float = 1.0
    pi:float = 0.0

    for _ in range(n_temp):
        pi += operation * (numerator/denominator)
        operation *= -1.0
        denominator += 2.0
    return pi

if __name__=="__main__":
    print("円周率の計算")
    print("項=1000000")
    print(calculate_pi(1000000))