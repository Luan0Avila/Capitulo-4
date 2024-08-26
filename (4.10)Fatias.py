animais = ['gato', 'cachorro', 'coelho','papagaio','sapo']

print ("os três primeiros elementos da lista são:")

for animal in animais[:3]:
    print (animal)

print("\nos três elementos no meio da lista são:")

for animal in animais[1:4]:
    print(animal)


print("\nos três ultimos elementos da lista são:")

for animal in animais[2:]:
    print(animal)
