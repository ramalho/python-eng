# Concurrent benchmarks

## Interpreter versions

```
$ python3 --version
Python 3.10.12
$ pypy3 --version
Python 3.8.13 (7.3.9+dfsg-1, Apr 01 2022, 21:41:47)
[PyPy 7.3.9 with GCC 11.2.0]
```

## Sample run

Script compatible with Python 3.8 (supported by PyPy 7.3.9)

```
$ pypy3 n_primos_proc_py38.py
Checking 20 numbers with 16 processes:
               2  P  0.000004s
3333333333333333     0.000004s
4444444444444444     0.000006s
5555555555555555     0.000046s
6666666666666666     0.000012s
7777777777777777     0.000044s
9999999999999999     0.000005s
 142702110479723  P  0.015781s
 299593572317531  P  0.020436s
4444444488888889     0.063057s
5555555555555503  P  0.065277s
3333333333333301  P  0.083176s
3333335652092209     0.085459s
7777777777777753  P  0.090459s
4444444444444423  P  0.100379s
6666667141414921     0.099932s
5555553133149889     0.111482s
6666666666666719  P  0.116083s
7777777536340681     0.116376s
9999999999999917  P  0.129154s
20 checks in 0.14s
```

## Python 3.10 v. PyPy3 3.8 [7.3]

Running on Ubuntu 22.04 (WSL 2, Windows 11), Intel Core i9.

```
$ python3 n_primes_proc_py38.py | (head -1 && tail -1)
Checking 20 numbers with 16 processes:
20 checks in 3.18s
$ pypy3 n_primes_proc_py38.py | (head -1 && tail -1)
Checking 20 numbers with 16 processes:
20 checks in 0.16s
```

* This Core i9 has 16 logical cores (8 actual cores × 2 thanks to Hyperthreading™).
* Pypy3 is much faster than CPython for this task.

Running on MacOS 13.5, Apple M2 Max:

```
% python3.11 n_primes_proc.py | (head -1 && tail -1)
Checking 20 numbers with 12 processes:
20 checks in 1.12s
% pypy3 n_primes_proc.py | (head -1 && tail -1)
Checking 20 numbers with 12 processes:
20 checks in 0.15s
```

* This M2 Max has 12 cores.
* CPython is almost 3x faster on M2 Max than on Core i9.
* The performance of Pypy is nearly the same on M2 Max and Core i9.

## Python 3.9 v. Python 3.11

Running on Raspberri Pi 4 (8GB).

```
$ python3.9 n_primes_proc.py | (head -1 && tail -1)
Checking 20 numbers with 4 processes:
20 checks in 37.09s
$ python3.11 n_primes_proc.py | (head -1 && tail -1)
Checking 20 numbers with 4 processes:
20 checks in 24.91s
```

* This Raspberry Pi has 3 cores.
* Python 3.11 is significantly faster than 3.9.

# Sequential benchmarks

## Python 3.10 v. PyPy3 3.8 [7.3]


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

$ time pypy3 primes.py > /dev/null

real    0m0.631s
user    0m0.621s
sys     0m0.010s

```

## Raspberri Pi 4 (8GB)

```
$ python3 --version
Python 3.9.2
$ time python3 primes.py > /dev/null

real    2m0.255s
user    0m0.204s
sys     0m0.029s
```


## Python v. Go

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