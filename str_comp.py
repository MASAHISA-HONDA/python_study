# -*- coding: utf-8 -*-
import sys

while True:
    mozi = input("入力")
    mozi = mozi*10000
    temp = {"a":10,\
                "b":11,\
                "c":12,\
                "d":13,\
                "e":14,\
                "f":15,\
                "g":16,\
                "h":17,\
                "i":18,\
                "j":19,\
                "k":20,\
                "l":21,\
                "m":22,\
                "n":23,\
                "o":24,\
                "p":25,\
                "q":26,\
                "r":27,\
                "s":28,\
                "t":29,\
                "u":30,\
                "v":31,\
                "w":32,\
                "x":33,\
                "y":34,\
                "z":35,\
                " ":36,\
                "!":37,\
                " ":38,\
                "#":39,\
                "$":40,\
                "%":41,\
                "&":42,\
                "'":43,\
                "(":45,\
                ")":46,\
                "-":47,\
                "_":48,\
                "@":49,\
                ",":50,\
                ".":51,\
                "/":52,\
                "=":53,\
                "+":54,\
                }
    mozi_string = 1
    if not mozi:
        break
    else:
        for now in mozi:
            mozi_string <<= 6
            mozi_string |= temp[now]
        print("元のサイズ："+ str(sys.getsizeof(mozi))+ "bytes")
        print("圧縮後:" + str(sys.getsizeof(mozi_string)) + "bytes")
        comp =  (1 - sys.getsizeof(mozi_string)/sys.getsizeof(mozi))*100
        print("圧縮率:" + str(round(comp,0)) + "%")
        print()