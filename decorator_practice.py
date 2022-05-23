from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kargs):
        initial_time = datetime.now()
        func(*args, **kargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Pasaron ' + str(time_elapsed.total_seconds()) + ' segundos.')
    return wrapper

@execution_time
def random_time():
    for _ in range(1, 100000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    print(a + b)

@execution_time
def saludo(nombre: str = 'Cesar') -> str:
    print('Hola ' + nombre)

random_time()
suma(5, 7)
saludo('Franco')