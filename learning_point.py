import pandas as pd

df = pd.read_csv('dataset_3363_4.txt', sep=';', names=['Фамилия','Математика', 'Физика', 'Русский язык'])
mat = df['Математика'].mean()

phis = df['Физика'].mean()

rus = df['Русский язык'].mean()

df['Среднее ученика'] = (df['Математика'] + df['Физика'] + df['Русский язык']) / 3

mean_learn = df['Среднее ученика']

with open('result.txt', 'w') as file:
    for value in mean_learn:
        file.write(str(value)+'\n')
    file.write(str(mat)+' '+str(phis)+' '+str(rus))


