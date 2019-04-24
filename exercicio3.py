from random import randrange

cont = 1
senha = ""
tentar = True

while cont <= 5:
    senha = senha + str(randrange(0, 9))

    cont+=1
    
while tentar:
    password = input('Digite a senha: ')

    cont = 0

    if senha == password:
            print("Senha Correnta!!!")
            break
        
    else:    
        newpassword = ""  
        while cont < 5:
            if senha[cont] == password[cont]:
                newpassword = newpassword + 'O'
            elif password[cont] in senha:
                newpassword = newpassword + '-'
            else:
                newpassword = newpassword + 'x'
            cont+=1
        password = newpassword
            
        print(password)
