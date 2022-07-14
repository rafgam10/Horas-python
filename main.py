horas = int(input('Digite um horário (0-23): '))

if horas<12:
    print('bom dia.')
elif horas<18:
    print('boa tarde')
else :
    print('boa noite')
