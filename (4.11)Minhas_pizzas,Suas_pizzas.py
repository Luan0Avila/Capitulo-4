minhas_pizzas = ['calabresa', 'catupiry', 'mussarela']
pizzas_amigos = minhas_pizzas[:]

print ('Minhas pizzas favoritas são:')
for pizza in minhas_pizzas:
    print (pizza,'\n')

print ('As pizzas favoritas dos meus amigos são:')
for pizza in pizzas_amigos:
    print(pizza,'\n')

minhas_pizzas.append('peperoni')
pizzas_amigos.append('atum')

print('Minhas pizzas favoritas são:')
for pizza in minhas_pizzas:
    print(pizza, '\n')

print('As pizzas favoritas dos meus amigos são:')
for pizza in pizzas_amigos:
    print(pizza, '\n')