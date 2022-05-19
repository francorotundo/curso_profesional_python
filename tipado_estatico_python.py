#Para declarar una variable y asignar el tipo de valor
# <nombre de variable> : <tipo de valor> = <valor>

a : int = 5
b : str = 'Hola'
c : bool = True

print(a,b,c)

#Para asignar los tipos de valores dentro de un Diccionario o Lista

from typing import Dict, List, Tuple

numbers: Tuple[int, float, int] = (1, 0.5, 1)

positives: List[int] = [1, 2, 3, 4, 5]

users: Dict[str, int] = {'argentina': 1, 'mexico': 34, 'colombia': 45}

countries: List[Dict[str, str]] = [
                                    {'name': 'Argentina',  
                                    'people': '450000'}, 
                                    {'name': 'Mexico', 
                                    'people': '9000000'
                                    }
                                    ]
