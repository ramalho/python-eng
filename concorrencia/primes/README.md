

# Python 3.10 v. PyPy3 3.8 [7.3]


```
$ python3 --version
Python 3.10.12
$ time python3 primes.py
2 True
142702110479723 True
299593572317531 True
3333333333333301 True
3333333333333333 False
3333335652092209 False
4444444444444423 True
4444444444444444 False
4444444488888889 False
5555553133149889 False
5555555555555503 True
5555555555555555 False
6666666666666666 False
6666666666666719 True
6666667141414921 False
7777777536340681 False
7777777777777753 True
7777777777777777 False
9999999999999917 True
9999999999999999 False

real    0m12.517s
user    0m12.517s
sys     0m0.000s

$ pypy3 --version
Python 3.8.13 (7.3.9+dfsg-1, Apr 01 2022, 21:41:47)
[PyPy 7.3.9 with GCC 11.2.0]
$ time pypy3 primes.py
2 True
142702110479723 True
299593572317531 True
3333333333333301 True
3333333333333333 False
3333335652092209 False
4444444444444423 True
4444444444444444 False
4444444488888889 False
5555553133149889 False
5555555555555503 True
5555555555555555 False
6666666666666666 False
6666666666666719 True
6666667141414921 False
7777777536340681 False
7777777777777753 True
7777777777777777 False
9999999999999917 True
9999999999999999 False

real    0m0.631s
user    0m0.621s
sys     0m0.010s

```


# Python v. Go

```
$ time python3.10 primes.py > /dev/null

real    0m13.432s
user    0m13.432s
sys     0m0.000s

$ time pypy3 primes.py > /dev/null

real    0m0.643s
user    0m0.643s
sys     0m0.000s

$ time go run primes.go > /dev/null

real    0m0.767s
user    0m0.728s
sys     0m0.123s

$ go build primes.go
$ time ./primes > /dev/null

real    0m0.600s
user    0m0.601s
sys     0m0.000s
```