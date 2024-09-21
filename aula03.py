#codigo para verificar se adolescentes estão liberados para assistir filme 

print('Pronto para a sessão? antes disso, Qual a sua idade?')

idade = int(input())

if idade >= 18:
    print('entrada liberada! Bom filme')
elif idade >=16:
    print('Você está acompanhado de um responsável maior de idade?')
    resposta = input().upper()

    if resposta == 'sim': 
        print('Entrada liberada, Bom filme ')
    else: 
        print('você só pode ver o filme acompanhado pois é menor de 18 anos')
else: 
    print('Não é permitido entrada de menores de 16 anos')

