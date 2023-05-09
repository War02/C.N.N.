#Declaração de variáveis iniciais
i = 0
media = 0
media_da_materia = 0
nome = 0
notas = 0
geral_notas = []
soma = 0
rec = 0
maior_nota = 0 

# Interagindo com o usuário
nome = input('Digite o nome do aluno: ')
qtde_provas = int(input('Informe a quantidade de provas dadas no bimestre: ')) 
media_da_materia = float(input('Informe a média mínima para ser aprovado: '))

# Estrutura de repetição para que o usuário possa inserir as notas 
for i in range (0,qtde_provas):
    notas = float(input('Informe a nota ' + str(i + 1) + ": "))
    i = i + 1
    soma += notas 
    geral_notas.append(notas) 

#Armazenando a maior nota
maior_nota = max(geral_notas, key=float)

# Houve simulado ?
p_sim= int(input('Digite 1 se ocorreu o simulado e 0 se não ocorreu: \n'))

if p_sim == 1:
    simulado = int(input('Digite a nota do simulado: '))
    media = (soma+simulado)/(qtde_provas+1)

else:
    media = (soma)/(qtde_provas)

# Estrutura de repetição para saber se o aluno foi aprovado ou reprovado
if media >= media_da_materia:
    print('\t ---------- Aluno aprovado ----------')
    print('\t ---------- MÉDIA :', media, '----------')

else: # Em caso de reprovação, incluí-se uma nova nota
    print('\t ---------- Aluno reprovado ---------- ') 
    print('\t ---------- MÉDIA :', media, '----------')

    rec = float(input('\n Informe a nota da recuperação: '))
    media = (maior_nota + rec)/(2)
    print('\t---------- A nova média de', nome,'é: ', media, '----------')

# --------------- Ideias à serem implementadas: --------------- 
# Uma função que calcule média da sala
# Encontrar uma maneira de atribuir cada nota ao seu respectivo aluno
# Definir cada tipo de atribuição de nota para cada matéria 
# Transformar o código em algo mais apresentável e mais funcional
