from primes import is_prime

def supervisor():
    n = 7_777_777_777_777_753
    primo = is_prime(n)
    e_nao_e = 'é' if primo else 'não é'
    print(n, e_nao_e, 'primo' )

if __name__ == '__main__':
    supervisor()
