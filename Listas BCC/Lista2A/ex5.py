import pandas as pd
df = pd.read_csv("https://www.dropbox.com/s/ablk7bwibhc8g6x/ManipulacaoDados_Planilha1.csv?dl=1")
print(df.groupby("Nota")["Duração"].min())