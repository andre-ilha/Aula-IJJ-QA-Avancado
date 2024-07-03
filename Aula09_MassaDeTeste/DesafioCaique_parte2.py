import pandas as pd

df = pd.read_csv('.\Aula-IJJ-QA-Avancado\Aula09_MassaDeTeste\DesafioCaique_Parte2_DadosFicticios.csv')
#print(df)

#com idade maior que 40 anos
idade40 = df[df['idade'] > 40]
print('Pessoas acima de 40 anos')
print(idade40)

#com renda maior de 5 mil
renda5000 = df[df['renda'] > 5000]
print('\nPessoas com renda acima de R$5.000,00')
print(renda5000)

#com renda maior de 15 mil
renda15000 = df[df['renda'] > 15000]
print('\nPessoas com renda acima de R$15.000,00')
print(renda15000)

