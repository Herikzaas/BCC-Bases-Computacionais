import pandas as pd

df = pd.read_csv("https://www.dropbox.com/s/kdbsu1hyo7l2zhx/fake-file14.csv?dl=1")
print(df.sort_values(by=["Genero"], ascending=[False]))