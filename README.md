# Proyecto-2---consumo

```python
consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
 },
}
tot_coca_codo_g = (120 + 55 + 32 + 120 + 75 + 32 + 150 + 55 + 32 + 120 + 97 + 32)
tot_coca_codo_q = (400 + 432 + 400 + 420 + 432 + 460 + 432 + 400 + 432 + 300 + 213)
tot_sopladora_g = (310 + 220 + 321 + 310 + 220 + 321 + 310 + 220 + 321 + 310 + 220 + 321)
tot_sopladora_q = (400 + 432 + 587 + 400 + 432 + 587 + 400 + 432 + 587 + 400 + 432 + 587)
tot_sopladora_l = (50 + 32 + 32 + 50 + 32 + 32 + 50 + 32 + 32 + 50 + 32 + 32)

informacion = {
 'costa': ('Guayaquil', 'Manta'),
 'sierra': ('Quito', 'Ambato', 'Loja'),
 'oriente': ('Tena', 'Nueva Loja')
}

costa = tot_coca_codo_g + tot_sopladora_g
sierra = tot_sopladora_q + tot_coca_codo_q + tot_sopladora_l
oriente = ('No existe una planta en el oriente')

print('''
    ------------------------------
          PLANTAS ENERGETICAS
    ------------------------------
    ''')
print('(1). El total de Megavatios en Planta y Ciudad ')
print('(2). El total de Energia por Ciudad ')
print('(3). El dinero que recauda por Region ')
print('(4). Escriba (salida) para Salir del programa')
opcion = input('Escoja una opcion: ')

if opcion == 'salida':
    exit

#1. Solicite al usuario el nombre de una planta y de una ciudad y presente el total de
#megavatios de consumos para dicha ciudad en dicha planta.
elif opcion == '1':
    
    print('''
    ===============================
        EL TOTAL DE MEGAVATIOS
               PLANTAS
    Coca Codo Sinclair,Sopladora
              CIUDADES
    Guayaquil,Quito,Loja
    ===============================
    ''')

    n_planta = input('Ingrese el nombre de la planta: ')

    if n_planta == 'Coca Codo Sinclair':
        n_ciudad = input('Ingrese el nombre de la ciudad: ')

        if n_ciudad == 'Quito':
            print('Total de Megavatios de consumo en Coca Codo Sinclair, Quito: ', tot_coca_codo_q, 'Megavatios')
            print('Con tarifa de: ', consumo_energia['Coca Codo Sinclair']['Quito']['tarifa'])
        elif n_ciudad == 'Guayaquil':
            print('Total de Megavatios de consumo en Coca Codo Sinclair, Guayaquil: ', tot_coca_codo_g, 'Megavatios')
            print('Con tarifa de: ', consumo_energia['Coca Codo Sinclair']['Guayaquil']['tarifa'])
        elif n_ciudad =='Loja':
            print("No hay una planta de Coca Codo Sinclair en Loja")
    print()

    if n_planta == 'Sopladora':
        n_ciudad = input('Ingrese el nombre de la ciudad: ')

        if n_ciudad == 'Quito':
            print('Total de MMegavatios de consumo en Sopladora, Quito: ', tot_sopladora_q, 'Megavatios')
            print('Con tarifa de: ', consumo_energia['Sopladora']['Quito']['tarifa'])
        elif n_ciudad == 'Guayaquil':
            print('Total de Megavatios de consumo en Sopladora, Guayaquil: ', tot_sopladora_g, 'Megavatios')
            print('Con tarifa de: ', consumo_energia['Sopladora']['Guayaquil']['tarifa'])
        elif n_ciudad == 'Loja':
            print('Total de Megavatios de consumo en Sopladora, Loja: ', tot_sopladora_l)
            print('Con tarifa de: ', consumo_energia['Sopladora']['Loja']['tarifa'])
    else:
        print("Digite correctamente la primera en mayuscula")

    exit
    

    

#2. Solicite al usuario el nombre de una ciudad y presente un nuevo diccionario cuyas claves
#son los nombres de las plantas generadoras y el valor es el total megavatios que cada
#planta le ha dado a ciudad. Si la planta no entrega energía a la ciudad entonces esa planta
#no debería aparecer en el nuevo diccionario  
elif opcion == '2':
    print('''
    
    TOTAL DE ENERGIA DADA A CADA
       CIUDAD POR CADA PLANTA
               CIUDADES
    Guayaquil
    Quito
    Loja
    Ambato
    Tena
    Nueva loja
    
    '''),

    n_ciudad2 = input('Ingrese el nombre de la ciudad: ')

    if n_ciudad2 == 'Guayaquil':
        print('Total de Megavatios, Coca Codo Sinclair: ', tot_coca_codo_g, 'Megavatios')
        print('Total de Megavatios, Sopladora:', tot_sopladora_g, 'Megavatios')
    elif n_ciudad2 == 'Quito':
        print('Total de Megavatios, Coca Codo Sinclair: ', tot_coca_codo_q, 'Megavatios')
        print('Total de Megavatios, Sopladora:', tot_sopladora_q, 'Megavatios')
    elif n_ciudad2 == 'Loja':
        print('Total de MMegavatios, Sopladora:', tot_sopladora_l, 'Megavatios')
    else:
        print('Ninguna planta otorga energía la ciudad seleccionada')
    print()

    exit


#3. Solicite el nombre de una región al usuario y presente cuento dinero ha recaudado la
#región
elif opcion == '3':
    print('''
    -------------------------------
         El DINERO RECAUDADO 
              REGIONES
    Costa
    Sierra
    Oriente
    -------------------------------
    '''),

    n_region = input('Ingrese nombre de Región: ')

    if n_region == 'Costa':
        print('Total Recaudado en la Región Costa: ', costa, '$')
    elif n_region == 'Sierra':
        print('Total Recaudado en la Región Sierra: ', sierra, '$')
    elif n_region == 'Oriente':
        print(oriente)
    else:
        print("Escriba correctamente la primera letra en mayuscula")
    exit
    
```
    
    
    
    
    
# proyecto funciones
```python
consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84}
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Tena': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Manta': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Puerto Ayora': { 'consumos': (50, 50),'tarifa': 10}
 },
}

datos = {
    'Costa': ('Guayaquil', 'Manta'),
    'Sierra': ('Quito', 'Ambato', 'Loja'),
    'Oriente': ('Tena', 'Nueva Loja')
}

def total_por_region(region):

    if region not in datos.keys():
        return 'region no existe'

    ciudades_region = datos[region]

    total_consumo = 0
    for ciudad_region in ciudades_region:
        for planta in consumo_energia.keys():
            for ciudad in consumo_energia[planta].keys():
                if ciudad_region ==  ciudad:
                    total_consumo += sum(consumo_energia[planta][ciudad]['consumos']) * consumo_energia[planta][ciudad]['tarifa']

    return total_consumo

def total_consumo_por_planta_ciudad(planta, ciudad):
    if planta not in consumo_energia.keys():
        return 'La planta ' + planta + ' no existe'

    if ciudad not in consumo_energia[planta].keys():
        return 'La planta ' + planta + ' no proveé energía a la ciudad de ' + ciudad

    total_consumo = sum(consumo_energia[planta][ciudad]['consumos'])
    return total_consumo

op = -1
while op != 0:

    print('(1) Total de energía consumida por la planta y la ciudad')
    print('(2) Total por cada región')
    print('(0) Salir')

    op = int(input('Ingrese una opción:'))

    if op == 1:
        planta = input('Ingrese el nombre de la planta que necesita (Coca Codo Sinclair, Sopladora):')
        ciudad = input('Ingrese el nombre de la ciudad:')

        total = total_consumo_por_planta_ciudad(planta, ciudad)

        if type(total) == int:
            print('El consumo de energía en la ciudad de {} fue de {} MWh en la planta {}'.format(ciudad, total, planta))
        else:
            print(total)

    if op == 2:
        region = input('Ingrese la región:')
        total = total_por_region(region)
        print("la",region,'produce un total de:', total, '\n')
```
