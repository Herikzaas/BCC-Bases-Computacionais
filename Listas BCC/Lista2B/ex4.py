import pandas as pd

df = pd.read_csv("https://www.dropbox.com/s/ceqfz524q4rc10l/fake-file17.csv?dl=1")

print(df.groupby("Genero")["Meses"].mean())