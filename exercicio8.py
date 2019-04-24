nome = input('Digite seu nome: ')
login = input('Digite o login: ')
senha = input('Digite a senha: ')
dtNasc = input('Digite sua data de nsaciment: ')
prem = input('Premium? (S/N)')

if prem == 's' or prem == 'S':
    prem = True
else:
    prem = False

print('Nome:'+nome)
print('Login:'+login)
print('Senha:'+senha)
print('Data de Nascimento:'+dtNasc)
print('Premium:'+prem)