import re
import matplotlib  as mt
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from collections import Counter



with open('./base/Mente-Milionaria.txt', 'r',encoding='utf8') as arquivo:
    livro = arquivo.read()

                                                                                        #dados = livro.replace('.','').replace(',','').replace('?','') opçao de troca.
regex = re.compile("[a-z-àâäãéêíôõóüuç]+")
dados = regex.findall(livro.lower())

                                                                                                    #total de palavras
                                                                                                #print(len(set(livro)))

#frequencia
                                                                                                #print(dados)
frequencia = Counter(dados).most_common()
frequencia30 = dict(Counter(dados).most_common(30))
frequencia10 = Counter(dados).most_common(10)

                                                                                                    #print(frequencia)
tabela = dict()
posicoes = list()
inicio = 0

while inicio < len(frequencia):
    posicao = 10

    for indice, item in enumerate(frequencia):
        inicio +=1
        if indice == posicao-1:
            posicoes.append(f'Posicao: {posicao} palavra: {item[0]}')
            tabela[item[0]] = item[1]

            posicao*=10


#criando arquivo para armazenar resultados
with open('./relatorios/analise em texto.txt','w') as arquivo:
    arquivo.write(f'Total de palavras distintas: {len(set(dados))}\n'
                  f'Total de palavras: {len(dados)}\n\n'
                  f'10+ Palavras: \n')
    for indice, par in enumerate(frequencia10):
        arquivo.write(f'{indice +1}ª {par}\n')

    #print(posicoes)


#pegando as palavras nas posicoes multiplas de 10

contagem = 0
tabela = {}
posicoes = []

while contagem < len(frequencia):
    posicao = 10
    for indice, item in enumerate(frequencia):
        contagem +=1
        if indice == posicao-1:
            posicoes.append((f'Posicao: {posicao} \nPalavras: {item[0]}'))
            tabela[item[0]] = item[1]
            posicao *= 10

df= pd.DataFrame({
    'Palavra': frequencia30.keys(),
    'Quantidade': frequencia30.values()
})

#print(dados) #erro na linha 70


#criando grafico

x = posicoes
y = list(tabela.values())

#criando DataFrame

df1 = pd.DataFrame({
    'Palavra': x,
    'Quantidade': y

})

print(df1)

fig, ax = plt.subplots(figsize=(8,4))
grafico = ax.bar(x= x, height= 'Quantidade', data=df1)


ax.set_title('Analise ZipF',fontsize=14, pad=20, color='blue')
ax.set_ylabel('Quantidade', fontsize=12, labelpad=5, color='blue')
ax.set_xlabel('Palavras', fontsize=12, labelpad=5, color= 'blue')
ax.set_xticks(x)
ax.set_xticklabels(df1['Palavra'])
ax.bar_label(grafico, size=10, label_type='edge')


plt.show()


