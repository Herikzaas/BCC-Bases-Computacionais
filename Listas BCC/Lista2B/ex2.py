import pandas as pd

df = pd.read_csv("https://www.dropbox.com/s/qvhsd1mr7dddks5/fake-file04.csv?dl=1")
print(df.sort_values(by = ["Genero","Meses"], ascending = [False,False]))

