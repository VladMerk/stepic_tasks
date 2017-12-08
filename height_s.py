import pandas as pd

df = pd.read_csv('dataset_3380_5.txt', sep='\t', names=['Class', 'Name', 'Height'])
course = df[['Class','Height']]
avarage = course.groupby('Class').mean()
print(avarage)
