import pandas as pd
df = pd.read_csv("https://www.dropbox.com/s/ablk7bwibhc8g6x/ManipulacaoDados_Planilha1.csv?dl=1")
df = df.sort_values(by = ["Nota","Ano"], ascending = [False,True])
print(df)