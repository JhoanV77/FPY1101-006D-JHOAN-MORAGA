''' 
Este algoritmo tiene la funcion de administrar y manejar el stock de la tienda llamada 'aqui vendemos'
'''

import os
print('*'+ 30)

producto = {'escoba', 'huevo', 'leche'}

menup = ['ver stock de producto', 'añadir nuevo producto', 'ajustar stock', 'eliminar producto', 'salir']

while True:
    for ind, opt in enumerate(menup):
        print(f'{ind + 1}. {opt}')
        ans = (input('que quiere hacer ?\n'))
    if ans == 1:
        os.system('cls')
        for clave, valor in producto.items():
            print(f'')
    elif ans == 2:
        os.system('cls')
        while True:
                 nombre = str(input('ingrese el nombre del producto que desea añadir\n').replace) 
                 if not nombre.replace(' ','').isalpha():
                     print('error: solo caracteres alfabeticos')
                     continue
                 else:
                      os.system('cls')
                      print('producto añadido')
                      break
        while True:
             try:
                  break
                  
             
    elif ans == 3:
        os.system('cls')
        while True:
             nombre = str('ingrese el nombre del producto')
                  
    elif ans == 4:
        os.system('cls')
        while True:
                 nombre = str(input('ingrese el producto que desea eliminar'))
                 if 

    elif ans == 5:
        os.system('cls')
        exit('has salido exitosamente adios!\n')
    else:
        os.systeam('cls')
        print('error: opcion no valida')
        continue
    