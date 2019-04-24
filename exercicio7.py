meninos = ['Jon','Bran','Tyrion','Joffrey','Jaime','Khal Drogo','Theon','Mindinho','Hodor','Eddard Stark']
meninas = ['Daenerys','Arya','Cersei','Sansa','Brienne','Gilly','Missandei','Meera','Catelyn Stark','Shae']

print('Possiveis Pares:\n')

for menino in meninos:
    for menina in meninas:
        print(menino +' e '+menina)

    print('\n')

for menina in meninas:
    for menino in meninos:
        print(menina +' e '+menino)
    print('\n')
