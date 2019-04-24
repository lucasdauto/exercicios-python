

def inform():
    notas = []
    nome = input('Digite nome do Aluno:')

    i = 0
    while i < 3:
        notas.append(int(input('Digite a nota:')))
        i+=1
    return media(notas,nome)

def media(notas = [0,0,0],nome = ''):
    media = 0

    for nota in notas:
        media += float(nota)
    
    media = float(media/3)
    return resultado(media,nome)

def resultado(media = 0, nome = ''):
    if media >= 6:
        print('O aluno '+nome+' está aprovado!\nMedia: '+str(media))
    else:
        print('O aluno '+nome+' está reprovado!\nMedia: '+str(media))


inform()


