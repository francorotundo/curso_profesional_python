def is_prime(numero: int) -> bool:
    c: int = 1
    for i in range(2, numero+1): 
        if numero%i == 0: c += 1
    if c>2: return False
    else: return True

def run():
    print(is_prime(11))

if __name__ == '__main__':
    run()
