import pandas as pd

df = pd.read_csv("https://www.dropbox.com/s/ndh81l021ny4ror/fake-file07.csv?dl=1")
print(df.query("Idade > 42"))