def inverte(palavra):
    cont = len(palavra)-1
    new = ""
    while cont >= 0:
        new = new + palavra[cont]
        cont-=1
    return new

palavra = input('Digite uma palavra: ')

print(inverte(palavra))