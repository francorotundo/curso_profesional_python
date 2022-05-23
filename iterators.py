# #creando un iterador

# my_list = [1, 2, 3, 4, 5]
# my_iter = iter(my_list)

# #Iterando un iterador

# # print(next(my_iter))
# # print(next(my_iter))
# # print(next(my_iter))
# # print(next(my_iter))
# # print(next(my_iter))
# # print(next(my_iter))
# #Cuando no quedan datos, la excepción StopIteration es elevada.


# #Iterando un iterador
# while True:
#     try:
#         print(next(my_iter))
#     except StopIteration:
#         break

class EvenNumbers:

    #Clase que implementa un iterador de todos los números pares, o los números pares hasta un máximo

    def __init__(self, max = None):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        
        else:
            raise StopIteration
