import pandas as pd

df = pd.read_csv("https://www.dropbox.com/s/den60tysvy06k8w/fake-file20.csv?dl=1")
print(df.query("Funcionario > 10 and Meses > 47"))
