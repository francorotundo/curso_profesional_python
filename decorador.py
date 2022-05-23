def decorador(func):
    def envoltura():
        print('Esto de añade a mi función original')
        func ()
    return envoltura

# def saludo():
#     print('hola')

# saludo = decorador(saludo)

@decorador #Es igual a la linea de codigo de la linea anterior
def saludo():
    print('Hola')

saludo()

#Other example

def mayuscula(func):    
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayuscula
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje.'

print(mensaje('Franco'))
