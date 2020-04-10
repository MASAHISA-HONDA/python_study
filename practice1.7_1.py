from typing import Dict
import fib3
import time
import sys

while True:     
    n = input("\n項の数を入力 → ")
    n = int(n)
    ans:dict = {}

    #マスターコード
    t1 = time.time()
    master = fib3.fib3(n-1)
    t2 = time.time()
    print(sys.getsizeof(master))

    t_master = t2 -t1
    print('\nマスターコードによる実行結果: '+str(master))
    print('マスターコードの実行時間: '+str(t_master))

    #今回作成したコード
    t3 = time.time()
    for i in range(n):
        if i == 0:
            ans[i] = 0
        elif i == 1:
            ans[i] =1
            
        else:
            ans[i] = ans[i-2] + ans[i-1]
    this_time = ans[n-1]
    t4 = time.time()

    t_this_time = t1004 -t3
    print('今回の実行結果: ' +str(this_time))
    print('今回の実行時間: '+str(t_this_time))

    #コードの検証
    error = abs(this_time - master) / master
    t_delta = t_master - t_this_time
    t_delta = float(t_delta) *10**6

    print('\n誤差: ' +str(error))
    print('実行時間差: ' +str(round(t_delta,2)) + '[ns]')


    