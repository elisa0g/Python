nome = input('Digite o nome do paciente: ')
idade = int(input('Digite a idade do paciente: '))
doença = input('Existe suspeita de doença infecciosa? ').upper()
if idade >=65:
    print('O paciente {} possui atendimento prioritario e deve ser levado para a sala comum'.format(nome))
elif doença=="SIM":
    print('O paciente {} deve ser levado imediatamente para a sala de espera reservada'.format(nome))
else:
    print('O paciente {} não possui atendimento prioritário e deve esperar na sala comum.'.format(nome))
            
