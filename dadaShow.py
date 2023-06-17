import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados.csv', delimiter=',')

print(df.columns)
keyword_counts = df['keyWord'].value_counts()
print(keyword_counts)
print("total = ", keyword_counts.sum())

