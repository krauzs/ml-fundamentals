import pandas as pd

df = pd.read_csv("titanic.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.isna().sum())
df = df.drop(columns=['Cabin'])
df['Age'] = df['Age'].fillna(df['Age'].median())
df = df.dropna(subset=['Embarked'])
print(df.isna().sum())
print(df.shape)