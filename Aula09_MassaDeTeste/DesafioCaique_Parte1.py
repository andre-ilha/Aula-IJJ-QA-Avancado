import pandas as pd

dados = {
    'Nome' : ['João','Marta','Ary','Mateus','Michelle','Claudio','Otavio'],
    'Idade' : [51,37,23,24,33,45,32],
    'Cidade' : ['Recife','Recife','Recife','Salvador','Salvador','São Paulo','Manaus']
}

df = pd.DataFrame(data=dados)

#print(df)

moradores_recife = df[df['Cidade'] == 'Recife']

print('Moradores de Recife')
print(moradores_recife)