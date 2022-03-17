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

informacion = {
    'Costa': ('Guayaquil', 'Manta'),
    'Sierra': ('Quito', 'Ambato', 'Loja'),
    'Oriente': ('Tena', 'Nueva Loja')
}

# new_region = input('Ingrese nueva región:')

# new_cities = []
# for new_city in range(2):
#     new_cities.append(input('Ingrese ciudades'))

informacion['Insular'] = ('Puerto Ayora', 'Puerto Villamil')

# print(informacion)

def total_por_region(region):

    if region not in informacion.keys():
        return 'region no existe'

    ciudades_region = informacion[region]

    total_consumo = 0
    for ciudad_region in ciudades_region:
        for planta in consumo_energia.keys():
            for ciudad in consumo_energia[planta].keys():
                if ciudad_region ==  ciudad:
                    total_consumo += sum(consumo_energia[planta][ciudad]['consumos']) * consumo_energia[planta][ciudad]['tarifa']

    return total_consumo


# print('Costa:',total_por_region('Costa'))
# print('Sierra:',total_por_region('Sierra'))
# print('Orinte:',total_por_region('Oriente'))
# print('Insular:',total_por_region('Insular'))

# print(sum(consumo_energia['Sopladora']['Guayaquil']['consumos'])+sum(consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos'])+sum(consumo_energia['Sopladora']['Manta']['consumos']))


def total_consumo_por_planta_ciudad(planta, ciudad):
    if planta not in consumo_energia.keys():
        return 'La planta ' + planta + ' no existe'

    if ciudad not in consumo_energia[planta].keys():
        return 'La planta ' + planta + ' no proveé energía a la ciudad de ' + ciudad

    total_consumo = sum(consumo_energia[planta][ciudad]['consumos'])
    return total_consumo

op = -1
while op != 0:

    print('<1> Total de energía consumida por planta y ciudad')
    print('<3> Total por región')
    print('<0> Salir')

    op = int(input('Ingrese opción:'))

    if op == 1:
        planta = input('Ingrese el nombre de la planta (Coca Codo Sinclair, Sopladora):')
        ciudad = input('Ingrese el nombre de la ciudad:')

        total = total_consumo_por_planta_ciudad(planta, ciudad)

        if type(total) == int:
            print('El consumo de energía en la ciudad de {} fue de {} MWh en la planta {}'.format(ciudad, total, planta))
        else:
            print(total)

    if op == 3:
        region = input('Ingrese región:')
        total = total_por_region(region)
        print(region, ':', total, '\n')


# total_consumo = total_consumo_por_planta_ciudad(planta, ciudad)
# print('El consumo de energía en la ciudad de {} fue de {} MWh en la planta {}'.format(ciudad, total_consumo, planta))

# ciudad = 'Guayaquil'
# total_consumo = total_consumo_por_planta_ciudad(planta, ciudad)
# print('El consumo de energía en la ciudad de {} fue de {} MWh en la planta {}'.format(ciudad, total_consumo, planta))

# print(total_consumo_por_planta_ciudad(planta, ciudad))

# print(planta in consumo_energia.keys())
# print(ciudad in consumo_energia[planta].keys())