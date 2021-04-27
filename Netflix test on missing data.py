import pandas as pd

data=pd.read_csv("netflix_titles.csv")

print(data.info())


cleaned_data=data.fillna(0)

missingdata=data.isnull().sum()
print(missingdata)

print(cleaned_data.info())
